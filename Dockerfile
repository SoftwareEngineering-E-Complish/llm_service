FROM python:3.11

WORKDIR /usr/src

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install -r requirements.txt

COPY app /usr/src/app/

COPY log_conf.yaml /usr/src/log_conf.yaml 


EXPOSE 8888

ENTRYPOINT ["uvicorn", "app.main:app","--log-config=log_conf.yaml" ]

CMD ["--host", "0.0.0.0", "--port", "8888 "]
