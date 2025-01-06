FROM pytorch/pytorch:2.2.2-cuda11.8-cudnn8-runtime as base

RUN apt-get update && apt-get upgrade -y

# Install dependencies
RUN apt-get install curl -y &&\
    apt-get install rsync -y &&\
    apt-get install git -y &&\
    rm -rf /var/lib/apt/lists/*

COPY ../requirements.txt requirements.txt

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt