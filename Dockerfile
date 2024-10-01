FROM python:3.12-slim-bullseye AS base

LABEL maintainer="Florian ISAK <florian.isak@icloud.com>"

WORKDIR /app
# Install system dependencies
RUN apt-get update && apt-get -y install libpq-dev gcc g++ curl procps net-tools tini git

RUN addgroup --gid 1002 --system chaser_website_dev && \
    adduser --shell /bin/bash --disabled-password --uid 1002 --system chaser_website_dev

COPY pyproject.toml /app/pyproject.toml

# Set up the Python environment
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1

RUN pip install -U pip wheel

COPY . /app

FROM base AS development

WORKDIR /app

# Install the project dependencies
RUN pip install --no-cache-dir -e .

CMD ["fastapi", "dev"]

EXPOSE 8090

FROM base AS production

WORKDIR /app

RUN addgroup --gid 1001 --system chaser_website && \
    adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group chaser_website

USER chaser_website

WORKDIR /app

RUN pip install --no-cache-dir -e .

# Expose the application port
EXPOSE 8090

SHELL ["/bin/bash", "-c"]
CMD ["fastapi", "run"]