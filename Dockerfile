FROM alpine:3.24

WORKDIR /flask

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.

CMD ['python' '-m' 'flask' '--app' 'run']