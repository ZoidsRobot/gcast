FROM rendyprojects/python:latest

RUN sudo apt update && apt upgrade -y 
RUN sudo apt-get install -y curl git npm ffmpeg python3-pip neofetch
RUN git clone -b https://github.com/TeamKillerX/KillerX-Base /root/TeamKillerX
RUN mkdir /root/TeamKillerX
WORKDIR /root/TeamKillerX
COPY . /root/TeamKillerX
RUN pip3 install -r requirements.txt
CMD bash start
