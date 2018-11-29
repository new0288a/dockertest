From centos
RUN yum install -y vim
RUN yum install -y net-tools
RUN yum install -y iproute
ADD ./testing.sh /
RUN chmod 777 /testing.sh
CMD ["/testing.sh"]
