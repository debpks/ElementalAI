# FROM pytorch/pytorch:2.2.2-cuda11.8-cudnn8-runtime as base
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04 as base

RUN apt-get update && apt-get upgrade -y

# Install dependencies
RUN apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    curl \
    rsync \
    git

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip

RUN pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu118
# RUN pip insall tensorflow[and-cuda]==2.14.0
COPY ../requirements.txt requirements.txt 

RUN pip install -r requirements.txt

RUN pip install tensorflow==2.10.0
CMD ["python3"]