FROM debian:12-slim

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl
RUN apt install -y git

RUN mkdir /venv

RUN useradd -u 1000 -m app
RUN chown -R app:app /venv

USER app
ENV PATH="/home/app/.local/bin/:$PATH"
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PROJECT_ENVIRONMENT=/venv

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN uv python install 3.13

WORKDIR /app

COPY pyproject.toml /app/
COPY uv.lock /app/
RUN uv sync --locked --no-dev

COPY . /app/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

ENTRYPOINT ["/app/docker-start.sh"]
