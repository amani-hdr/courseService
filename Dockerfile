FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
ENV DJANGO_SETTINGS_MODULE=mini_projet_idl.settings
CMD gunicorn --bind 0.0.0.0:$PORT mini_projet_idl.wsgi:application