FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi uvicorn openenv-core

EXPOSE 7860
ENV PYTHONPATH=/app


CMD ["python", "-m", "server.app"]