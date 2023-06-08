FROM python:3.10-slim

WORKDIR /shaqy-project

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    pip install Flask flask_sqlalchemy flask_login Flask-WTF WTForms wtforms.validators email_validator psycopg2-binary

COPY . .

CMD python server.py