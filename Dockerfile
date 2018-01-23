FROM alpine
MAINTAINER Bjoern Pohl "bjoern@datenwalze.de"
# flask
RUN apk add --no-cache bash git uwsgi uwsgi-python py2-pip \
	&& pip2 install --upgrade pip \
	&& pip2 install flask

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]