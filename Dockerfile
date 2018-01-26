FROM alpine
MAINTAINER Bjoern Pohl "bjoern@datenwalze.de"
# flask
RUN apk add --no-cache bash uwsgi-python3 \
	&& pip3 install --upgrade pip \
	&& pip3 install flask

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
