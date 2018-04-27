FROM centos/python-27-centos7

WORKDIR /home/cuadmin/Documents/TwitterAnalyticsPlus/app
USER root
COPY requirements.txt ./
COPY test.py ./
COPY sentiment.py ./
COPY simple_content.py ./
COPY content.py ./

RUN yum -y install epel-release
RUN yum -y install python-devel
RUN yum -y install python-pip
ENV LD_LIBRARY_PATH=/opt/rh/python27/root/usr/lib64
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./test.py" ]
