FROM python:3.10

WORKDIR /workspace

COPY requirements.txt . 
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "main.py"]
