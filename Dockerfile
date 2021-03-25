FROM python:3.6
WORKDIR /user/souce/app

COPY setup.py ./
COPY app/__init__.py ./app/__init__.py

RUN pip install -e .

COPY . .

ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]
