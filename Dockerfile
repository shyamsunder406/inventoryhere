FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install pika
CMD ["python", "inventory.py"]
