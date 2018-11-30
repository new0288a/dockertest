From centos
RUN yum install -y epel-release
RUN yum install -y python python-pip
RUN pip install flask
ADD web.py /
ENTRYPOINT python web.py
