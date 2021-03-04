FROM ubuntu:18.04

RUN apt-get update && apt-get install -y tzdata
ENV TZ=Asia/Tokyo

RUN apt-get update && apt-get -y install \
    python3 python3-pip libopencv-dev

RUN python3 -m pip install -U pip
RUN python3 -m pip --no-cache-dir install opencv-python