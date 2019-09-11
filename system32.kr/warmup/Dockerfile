FROM       ubuntu:16.04
MAINTAINER howdays

RUN apt-get update
RUN apt-get install -y xinetd 
ENV TERM=linux

RUN useradd strange_file
RUN mkdir /home/strange_file
WORKDIR /home/strange_file

ADD problem /home/strange_file
ADD flag /home/strange_file
ADD attack /etc/xinetd.d

RUN chmod 460 /home/strange_file/*
RUN chown strange_file:root /home/strange_file/*
RUN chmod +x /home/strange_file/problem
RUN mkdir /home/strange_file/files
RUN chmod 777 /home/strange_file/files


RUN echo "attack 3000/tcp" >> /etc/services
EXPOSE 3000

CMD ["/usr/sbin/xinetd","-dontfork"]