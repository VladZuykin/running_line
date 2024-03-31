import datetime as dt

from django.core.exceptions import ValidationError
from django.http import HttpResponse, FileResponse, HttpResponseBadRequest
from django.shortcuts import render

from running_line_funcs import generate_running_line
from .models import RunningLineRequest


# Представление запроса бегущей строки
def running_line(request):
    text = request.GET.get("text", "Hello world!")
    duration = request.GET.get("duration", 3)
    width = request.GET.get("width", 100)
    height = request.GET.get("height", 100)
    fontsize = request.GET.get("fontsize", 40)
    fps = request.GET.get("fps", 30)

    try:
        obj = RunningLineRequest(
            text=text, duration=duration, height=height, width=width, fontsize=fontsize, fps=fps,
            date=dt.datetime.now())
        obj.full_clean()
        duration = float(duration)
        width, height = int(width), int(height)
        fontsize, fps = int(fontsize), int(fps)
    except ValidationError as e:
        return HttpResponseBadRequest(f"Ошибка, некоторые параметры имеют значения вне диапазона: {e}.")

    clip = generate_running_line(
        text=text, duration=duration, res=(width, height), fontsize=fontsize)
    filename = f"running_line.mp4"
    clip.write_videofile(filename, fps=fps)

    with open(filename, "rb") as f:
        response = HttpResponse(FileResponse(f), content_type="application/mp4")
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    obj.save()
    return response


def index(request):
    objects = RunningLineRequest.objects.all().order_by('-id')[:5]
    return render(request, "index.html", {"objects": objects})
