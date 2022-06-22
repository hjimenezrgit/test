FROM python:3.8

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
