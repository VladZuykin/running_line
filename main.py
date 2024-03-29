import moviepy.editor as mpy
import moviepy.video.fx.all as vfx
from moviepy.Clip import Clip
from typing import Tuple

from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


def generate_running_line(text: str, duration: float, res: Tuple[int, int] = (100, 100), fontsize=50,
                          font="Arial", textcolor="white"):
    text_clip: mpy.TextClip = mpy.TextClip(text, fontsize=fontsize, color=textcolor, font=font).set_duration(duration)
    scrolled_text_clip: Clip = vfx.scroll(text_clip, w=res[0], x_start=0, x_speed=text_clip.w / duration)
    surface_clip = mpy.ColorClip(size=res, color=(0, 0, 0), duration=duration)
    res_clip = CompositeVideoClip([surface_clip, scrolled_text_clip.set_position("center")], size=res)
    return res_clip


if __name__ == '__main__':
    clip = generate_running_line("hello world", 3)
    clip.write_videofile("running_line.mp4", fps=20)
