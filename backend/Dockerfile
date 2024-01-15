FROM python:3.11.4-alpine3.18

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "watch -n 1 'python app.py'"]
