FROM python:3.11

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app/

EXPOSE 8888

ENTRYPOINT ["uvicorn", "app.main:app"]

CMD ["--host", "0.0.0.0", "--port", "8888 "]

