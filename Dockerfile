FROM python:3.9

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME venv

CMD ["python", "main.py"]
