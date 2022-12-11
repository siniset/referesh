FROM alpine:latest

RUN apk add python3 postgresql-client postgresql-dev curl bash gcc python3-dev libpq-dev musl-dev
RUN curl -sSL https://install.python-poetry.org | python -

WORKDIR /usr/src/app
ENV PATH="/root/.local/bin:${PATH}"

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root
COPY . .

EXPOSE 8080

CMD ["poetry", "run", "invoke", "launch"]
