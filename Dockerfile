FROM python:3.9-slim-buster

# Stop Python from creating byte-code
ENV PYTHONDONTWRITEBYTECODE=1

# Update pip, setuptools and install dependencies
COPY ./requirements.txt /tmp/
RUN pip install --upgrade \
    pip \
    setuptools \
    && pip install --no-cache-dir -r /tmp/requirements.txt

# Copy source code
WORKDIR /usr/src/
COPY ./ ./

EXPOSE 8000/tcp

# Tell Docker that container is executable
ENTRYPOINT sh -c 'cd ./src/app/ && python server.py'
