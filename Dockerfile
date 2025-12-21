FROM python:3.10

WORKDIR /app

RUN pip install psycopg2-binary

COPY generator/generator.py .

CMD ["python", "generator.py"]
