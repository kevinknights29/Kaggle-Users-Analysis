# Use an official Python runtime as a parent image.
# See https://hub.docker.com/_/python for more information.
# To understand docker image tags, see https://forums.docker.com/t/differences-between-standard-docker-images-and-alpine-slim-versions/134973
FROM python:3.12.5-slim-bullseye

# Install system packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    # deps for downloading models
    curl \
    # deps for development
    git \
    openssh-client \
    # deps for python packages
    build-essential \
    python3-dev \
    libffi-dev \
    g++ \
    && apt-get clean

# Set the working directory to /opt/app
WORKDIR /opt/app

# Upgrade pip
RUN pip install --upgrade pip

# Install UV
# To learn more about UV, see https://github.com/astral-sh/uv
RUN pip install uv

# Copy the requirements file
COPY requirements.txt .

# Install dependencies from the requirements file
RUN uv pip install --system -r ./requirements.txt
