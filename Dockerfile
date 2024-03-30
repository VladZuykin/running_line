FROM python:3.11.8-alpine3.19
WORKDIR /app
COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install poetry && poetry config virtualenvs.in-project true && poetry install --no-root
RUN apk add imagemagick && apk add ffmpeg

# Fonts
RUN apk add font-terminus font-inconsolata font-dejavu font-noto font-noto-cjk font-awesome font-noto-extra
RUN apk add font-vollkorn font-misc-cyrillic font-mutt-misc font-screen-cyrillic font-winitzki-cyrillic font-cronyx-cyrillic

RUN .venv/bin/python3 manage.py makemigrations && .venv/bin/python3 manage.py migrate
CMD [".venv/bin/python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000