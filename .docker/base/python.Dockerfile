FROM python:3.10

RUN apt-get update && apt-get install -y \
    libopenblas-dev \
    bash \
    curl \
    wget \
    unzip \
    chromium \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN useradd -m python
WORKDIR /home/python

COPY python/app/requirements.txt /home/python/requirements.txt
RUN pip install --no-cache-dir -r /home/python/requirements.txt

USER python

CMD ["tail", "-f", "/dev/null"]
