FROM rendyprojects/killerxbase:latest

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install \
    python3 python3-dev python3-dev python3-pip python3-venv 

RUN apt-get install git curl python3-pip ffmpeg -y
ARG USER=root
USER $USER
RUN python3 -m venv venv
WORKDIR /app
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN git clone -b beta https://github.com/TeamKillerX/KillerX-Base 
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "-m", "KillerXBase"]
