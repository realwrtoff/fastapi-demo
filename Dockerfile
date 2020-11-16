FROM python:3.8

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV app /app
ADD . ${app}
WORKDIR ${app}
RUN pip install --user -r requirements.txt  -i http://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn

CMD ["python", "main.py"]
