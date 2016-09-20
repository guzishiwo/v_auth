FROM daocloud.io/library/ubuntu:trusty-20160711
MAINTAINER wu <wwu@vwms.cn>

COPY locale /etc/default/locale
RUN locale-gen en_US.UTF-8 &&\
  DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales
RUN apt-get update && apt-get install -y python-pip \
									     python-dev \
									     libmysqld-dev \ 
									     python-mysqldb


RUN pip install django==1.7
RUN pip install marshmallow
COPY taobaoauth /usr/src/app/
COPY init.sh /usr/src/app/
RUN chmod +x /usr/src/app/init.sh

RUN mkdir /var/we_build_auth/
RUN pip install pyjwt
WORKDIR /usr/src/app/

EXPOSE 80

CMD ["/usr/src/app/init.sh"]
