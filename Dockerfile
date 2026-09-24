FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py heating_cooling_degree_day_calculator.py .

EXPOSE 7860

CMD ["python", "app.py"]
