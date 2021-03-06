FROM python:alpine

ADD requirements.txt /app/requirements.txt
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev jpeg-dev zlib-dev libpng-dev \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && apk del build-deps
ADD . /app
WORKDIR /app

RUN python manage.py collectstatic

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=altessimo.production

CMD ["gunicorn", "--bind", ":8000", "altessimo.wsgi"]
