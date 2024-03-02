FROM python:3.11.7

COPY ./ /root
WORKDIR  /root
RUN pip install -r requirement.txt