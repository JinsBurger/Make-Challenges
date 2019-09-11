FROM       ubuntu:16.04
MAINTAINER c2w2m2

RUN apt-get update
RUN apt-get install -y xinetd
RUN apt-get install -y netcat gdb python2.7
ENV TERM=linux

RUN useradd babygdb
RUN mkdir /home/babygdb
WORKDIR /home/babygdb

ADD run_gdb.py /home/babygdb
ADD flag /
ADD xinetd /etc/xinetd.d/babygdb

RUN chmod 460 /home/babygdb/*
RUN chown babygdb:root /home/babygdb/*

RUN echo "babygdb 3003/tcp" >> /etc/services
EXPOSE 3003

RUN service xinetd restart
CMD ["/usr/sbin/xinetd","-dontfork"]