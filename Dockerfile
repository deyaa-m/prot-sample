FROM python:3.8

COPY . /app

WORKDIR /app

RUN python3.8 -m pip install --upgrade pip \
	&& make install

CMD ["/usr/local/bin/python", "lang_det.py"]



