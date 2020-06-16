FROM openjdk:8 as BASE

RUN apt update && \
    apt install -y python3-pip && \
    apt install -y curl

RUN curl -O http://mirror.netinch.com/pub/apache/spark/spark-2.4.6/spark-2.4.6-bin-hadoop2.7.tgz
RUN tar xvf spark-2.4.6-bin-hadoop2.7.tgz

RUN mv spark-2.4.6-bin-hadoop2.7/ /opt/spark 

RUN echo "export SPARK_HOME=/opt/spark" >> ~/.bashrc
RUN echo "export PATH=$PATH:/opt/spark/bin:/opt/spark/sbin" >> ~/.bashrc

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR /spark-processor
COPY . .
