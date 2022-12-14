FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python3 download_model.py

EXPOSE 80

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=80", "--server.address=0.0.0.0"]
