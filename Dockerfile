FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5000"]
