from io import BytesIO

import datetime as dt

from django.core.exceptions import ValidationError
from django.http import HttpResponse, FileResponse, HttpResponseBadRequest
from django.shortcuts import render

from running_line_funcs import generate_running_line
from .models import RunningLineRequest


def running_line(request):
    text = request.GET.get("text", "Hello world!")
    obj = RunningLineRequest(text=text, date=dt.datetime.now())
    try:
        obj.full_clean()
    except ValidationError as e:
        return HttpResponseBadRequest(f"Ошибка, попробуйте сделать текст поменьше: {e}")

    clip = generate_running_line(text=text, duration=3, res=(100, 100), fontsize=36)
    filename = f"running_line.mp4"
    clip.write_videofile(filename, fps=60)

    with open(filename, "rb") as f:
        response = HttpResponse(FileResponse(f), content_type="application/mp4")
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    obj.save()
    return response


def index(request):
    objects = RunningLineRequest.objects.all().order_by('-id')[:5]
    return render(request, "index.html", {"objects": objects})
