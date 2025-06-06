
FROM python:3.11-slim

WORKDIR /app

COPY app /app/app
COPY app.py /app/
COPY config.py /app/
COPY seed_admin.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
