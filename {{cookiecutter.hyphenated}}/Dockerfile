FROM debian:12-slim

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl 
RUN apt install -y git

RUN mkdir /venv

# # Don't run your app as root.
RUN useradd -u 1000 -m app
RUN chown -R app:app /venv

USER app
ENV PATH="/home/app/.local/bin/:$PATH"
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PROJECT_ENVIRONMENT=/venv

# install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN uv python install 3.13

# Create app directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml /app/
COPY uv.lock /app/
RUN uv sync --locked

# Copy project
COPY manage.py /app/
COPY {{cookiecutter.underscored}} /app/{{cookiecutter.underscored}}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose port 8000
EXPOSE 8000

# Start server
CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]