FROM python:3.8-slim
MAINTAINER ostegura

COPY requirements*.txt ./
RUN pip install --no-cache-dir --upgrade wheel pip setuptools && \
    pip install --no-cache-dir -r requirements.txt
COPY . /app


WORKDIR /app
RUN chmod +x /app/entrypoint.sh
CMD ["./entrypoint.sh"]