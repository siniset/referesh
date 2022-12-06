FROM alpine:latest

RUN apk add python3 postgresql-client postgresql-dev curl bash gcc python3-dev libpq-dev musl-dev
RUN curl -sSL https://install.python-poetry.org | python -
WORKDIR /usr/src/app
ENV PATH="/root/.local/bin:${PATH}"
COPY . .
RUN poetry install

CMD ["poetry", "run", "invoke", "test"]
