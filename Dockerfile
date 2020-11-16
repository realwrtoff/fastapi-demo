FROM daocloud.io/centos:7 as builder

# Install Python 3.6 在进行安装时，使用&&连接多行的原因时：减少镜像层数量，压缩镜像体积
RUN yum -y install epel-release gcc \
    && yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && yum -y install https://mirrors.aliyun.com/ius/ius-release-el7.rpm \
    && yum -y install python36u \
    && yum -y install python36u-pip \
    && yum -y install python36u-devel \
    # clean up cache
    && yum -y clean all

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt -i http://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn

#定义时区参数
ENV TZ=Asia/Shanghai
#设置时区
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV app /app
# not .., do u know why ?
ADD . ${app}

WORKDIR ${app}
# 使用gunicorn更加成熟和稳定,虽然用["python", "main.py"]也可以运行
CMD ["gunicorn", "main:app", "-w", "4", "-b", "0.0.0.0:8080", "-k", "uvicorn.workers.UvicornWorker"]
