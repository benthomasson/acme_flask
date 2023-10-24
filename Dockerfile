FROM registry.access.redhat.com/ubi8/python-39
USER 0
COPY requirements.txt /opt/app-root/src/
RUN pip install -r /opt/app-root/src/requirements.txt
COPY hello.py /opt/app-root/src/
COPY acme_tiny.py /opt/app-root/src/
COPY acme_flask.py /opt/app-root/src/
COPY entrypoint.sh /opt/app-root/src/
RUN mkdir challenges
RUN mkdir acme
RUN mkdir server
RUN chmod +x entrypoint.sh
RUN chmod +x entrypoint.sh
EXPOSE 80
EXPOSE 443
WORKDIR /opt/app-root/src/
CMD ["./entrypoint.sh"]
