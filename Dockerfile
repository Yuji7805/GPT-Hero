ARG PYTHON_VERSION=3.11-slim-bullseye


FROM python:${PYTHON_VERSION}

# Install git
RUN apt-get update && apt-get install -y git

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

ENV SECRET_KEY "jVLVr7p8OMRsWnBCxk4iUYupqDrmVXLAT0Wm2CuOk6VYRgsoUY"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "GPTHero.wsgi"]
