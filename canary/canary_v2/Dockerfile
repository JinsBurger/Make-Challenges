FROM       ubuntu:16.04
MAINTAINER howzinuns@gmail.com

RUN useradd -m canary_v2
RUN chown -R root:root /home/canary_v2

ADD https://github.com/hOwD4yS/Make-pwn-problem/raw/master/canary_v2/problem /home/canary_v2/

RUN chmod -R 555 /home/canary_v2/
RUN apt-get -y update
RUN apt-get -y install socat screen ssh
RUN service ssh start