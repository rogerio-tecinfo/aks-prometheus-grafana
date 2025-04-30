FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY AzureResourceInventory_Report_2025-04-29_22_56.xlsx /app/
COPY . .

CMD ["python", "script-converter.py"]