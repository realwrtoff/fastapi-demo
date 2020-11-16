#FROM python:3.8-apline
#
#ENV TZ=Asia/Shanghai
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
#
#ENV app /app
#ADD . ${app}
#WORKDIR ${app}
#RUN pip install -r requirements.txt  -i http://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn
#
## 使用gunicorn更加成熟和稳定,虽然用["python", "main.py"]也可以运行
#CMD ["gunicorn", "main:app", "-w", "4", "-b", "0.0.0.0:8080", "-k", "uvicorn.workers.UvicornWorker"]

FROM python:3.8.3-alpine3.11 as Build
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt -i http://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn

FROM python:3.8.3-alpine3.11
COPY --from=Build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
ENV app /app
ADD . ${app}
WORKDIR ${app}
# 使用gunicorn更加成熟和稳定,虽然用["python", "main.py"]也可以运行
CMD ["gunicorn", "main:app", "-w", "4", "-b", "0.0.0.0:8080", "-k", "uvicorn.workers.UvicornWorker"]
