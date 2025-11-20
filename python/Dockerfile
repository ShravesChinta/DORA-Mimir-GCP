FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY generate_dora_metrics.py .

CMD [ "python", "generate_dora_metrics.py" ]
