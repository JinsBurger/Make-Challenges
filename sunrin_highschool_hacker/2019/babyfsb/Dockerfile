FROM       ubuntu:16.04
MAINTAINER howdays

RUN apt-get update
RUN apt-get install -y xinetd
RUN apt-get install -y libseccomp-dev netcat 
ENV TERM=linux

RUN useradd babyfsb
RUN mkdir /home/babyfsb
WORKDIR /home/babyfsb

ADD problem /home/babyfsb
ADD flag /
ADD start.sh /home/babyfsb
ADD xinetd /etc/xinetd.d/babyfsb

RUN chmod 460 /home/babyfsb/*
RUN chown babyfsb:root /home/babyfsb/*
RUN chmod +x /home/babyfsb/problem
RUN chmod +x /home/babyfsb/start.sh


RUN echo "babyfsb 3000/tcp" >> /etc/services
EXPOSE 3000

RUN service xinetd restart
CMD ["/usr/sbin/xinetd","-dontfork"]