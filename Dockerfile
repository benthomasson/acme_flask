FROM registry.access.redhat.com/ubi8/python-39
USER 1001
COPY requirements.txt /opt/app-root/src/
RUN pip install -r /opt/app-root/src/requirements.txt
COPY . /opt/app-root/src/
EXPOSE 8043
WORKDIR /opt/app-root/src/
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "forwarder:app"]
