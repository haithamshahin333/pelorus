FROM registry.access.redhat.com/ubi8/python-38
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["./gunicorn.sh"]