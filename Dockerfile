# Railpack installs Python with mise. Python 3.9 is end of life, so mise has
# no precompiled python@3.9.15 and the Railway image build fails immediately.
# Django 2.2 only runs on Python 3.9 and earlier, so keep that runtime here.
FROM python:3.9.15-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Shell form so Railway's PORT is expanded at runtime. Exec form leaves it literal.
CMD /bin/sh -c "python manage.py migrate --noinput && exec gunicorn serahssite.wsgi:application --bind 0.0.0.0:${PORT:-8080}"
