FROM zalando/nikola

RUN apt-get install -y git
RUN pip3 install CherryPy

ADD run.sh /
ADD serve.py /

EXPOSE 8000

ENTRYPOINT ["/run.sh"]


