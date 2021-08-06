FROM python:3.8-slim-buster
WORKDIR /app
COPY api/requirements.txt .
RUN python -m pip install -r requirements.txt
COPY . .
EXPOSE 80
WORKDIR /app/api
CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:80", "api:app"]