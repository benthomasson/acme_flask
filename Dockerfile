FROM registry.access.redhat.com/ubi8/python-39
USER 1001
COPY requirements.txt /opt/app-root/src/
RUN pip install -r /opt/app-root/src/requirements.txt
COPY forwarder.py /opt/app-root/src/
EXPOSE 80
WORKDIR /opt/app-root/src/
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80",  "-b", "0.0.0.0:443", "forwarder:app"]
