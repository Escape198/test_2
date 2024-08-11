FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libpq-dev gcc

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

ENV FLASK_APP=run.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
