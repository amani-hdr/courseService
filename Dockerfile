FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
ENV DJANGO_SETTINGS_MODULE=mini_projet_idl.settings
ENTRYPOINT ["entrypoint.sh"]
