FROM python:3.8

COPY exporter.py /app/exporter.py

CMD [ "python", "/app/exporter.py" ]
