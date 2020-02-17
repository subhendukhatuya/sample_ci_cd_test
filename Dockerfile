FROM centos:7.5.1804
WORKDIR /
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y update
RUN yum install -y gcc gcc-c++
RUN yum install -y python36u python36u-libs python36u-devel python36u-pip
RUN python3.6 -m pip install -U pip
RUN python3.6 -m pip install Flask --no-cache-dir
RUN python3.6 -m pip install torch --no-cache-dir
RUN python3.6 -m pip install numpy -I
ADD src /src/
EXPOSE 5000
WORKDIR /src/
ENTRYPOINT ["python3.6", "api.py"]


