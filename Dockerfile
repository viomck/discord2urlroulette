FROM python:3.10

WORKDIR /usr/src/app

COPY main.py ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "sh", "./entrypoint.sh" ]
