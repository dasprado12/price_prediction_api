FROM python:3.6
WORKDIR /user/souce/app

COPY setup.py ./
COPY price_prediction/__init__.py ./price_prediction/__init__.py

RUN pip install -e .

COPY . .

ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]
