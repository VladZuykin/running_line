import moviepy.editor as mpy
import moviepy.video.fx.all as vfx
import numpy as np
from typing import Tuple

from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


def horizontal_outer_scroll(clip, x_speed, width=None,
                            x_start=0, bg_color=(0, 0, 0), apply_to="mask"):
    bg_color = np.array(bg_color)
    # width - ширина "окна", которое "движется" по клипу с текстом.
    if width is None:
        width = clip.w
    # Увеличиваю клип с текстом на случай, если он будет меньше, чем ширина экрана.
    elif width > clip.w:
        surface_clip: mpy.ColorClip = mpy.ColorClip(size=(width, clip.size[1]), color=bg_color, duration=clip.duration)
        clip = CompositeVideoClip([surface_clip, clip.set_position("left", "center")], size=(width, clip.size[1]))

    def f(get_frame, t):
        frame: np.ndarray = get_frame(t)

        # Левые и правые концы клипа с текстом, которые хочу взять в данный момент
        left_x, right_x = int(x_start + t * x_speed), int(x_start + t * x_speed) + width
        if left_x > right_x:
            left_x, right_x = right_x, left_x

        # Если клип текста покрывает всё "окно"
        if left_x >= 0 and right_x < frame.shape[1]:
            return frame[:, left_x:right_x]

        if len(frame.shape) == 3:
            region_shape = (frame.shape[0], width, frame.shape[2])
            frame_region = np.ones(region_shape, frame.dtype)
            for i in range(3):
                frame_region[:, :, i] *= bg_color[i]
        else:
            region_shape = (frame.shape[0], width)
            frame_region = np.zeros(region_shape, frame.dtype)

        # Если "окно" наезжает на текст слева
        if int(x_start + t * x_speed) < 0:
            frame_region[:, width - right_x:] = frame[:, :right_x]
            return frame_region

        # Если "окно" выезжает справа от текста
        if right_x >= frame.shape[1] > left_x:
            frame_region[:, :frame.shape[1] - left_x] = frame[:, left_x:]
        return frame_region

    # Возвращаю "окно"
    return clip.fl(f, apply_to=apply_to)


def generate_running_line(text: str, duration: float, res: Tuple[int, int] = (100, 100), fontsize=40,
                          font="Arial", textcolor="white", bg_color=(0, 255, 0)):
    bg_color = np.array(bg_color)
    text_clip: mpy.TextClip = mpy.TextClip(text, fontsize=fontsize, color=textcolor, font=font).set_duration(duration)
    width = res[0]
    scrolled_text_clip = horizontal_outer_scroll(text_clip,
                                                 width=width,
                                                 x_start=-res[1],
                                                 x_speed=(text_clip.w + width) / duration)
    surface_clip: mpy.ColorClip = mpy.ColorClip(size=res, color=bg_color, duration=duration)
    res_clip = CompositeVideoClip([surface_clip, scrolled_text_clip.set_position("center")], size=res)
    return res_clip


if __name__ == '__main__':
    clip = generate_running_line("hello world", 3)
    clip.write_videofile("running_line.mp4", fps=60)
