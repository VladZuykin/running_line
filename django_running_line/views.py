from io import BytesIO

import django.core.handlers.wsgi
from django.http import HttpResponse, FileResponse

from main import generate_running_line


def running_line(request):
    text = request.GET.get("text", "Hello world!")
    clip = generate_running_line(text=text, duration=3, res=(100, 100), fontsize=36)
    filename = f"running_line.mp4"
    clip.write_videofile(filename, fps=60)
    with open(filename, "rb") as f:
        response = HttpResponse(FileResponse(f), content_type="application/mp4")
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
