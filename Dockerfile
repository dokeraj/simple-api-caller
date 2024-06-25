FROM python:alpine3.14

RUN pip install pyyaml
RUN pip3 install certifi
RUN pip3 install requests
RUN pip3 install six
RUN pip3 install wheel
RUN pip3 install environs
RUN pip3 install docker
RUN pip3 install dacite


RUN mkdir /yaml
RUN mkdir /entry
RUN mkdir /sqldb

ADD configInit.py /entry/
ADD main.py /entry/

WORKDIR /entry/
CMD [ "python", "-u", "main.py" ]