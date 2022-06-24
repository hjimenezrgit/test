FROM python:3.8

WORKDIR /opt/app

COPY . .

RUN apt update && apt install -y nfs-common

RUN pip install --no-cache-dir -r requirement.txt

RUN mkdir -p /opt/nfs

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
