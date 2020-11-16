FROM python:3.8

ENV app /app
ADD . ${app}
WORKDIR ${app}
RUN pip install --user -r requirements.txt  -i http://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn

CMD ["python", "main.py"]
