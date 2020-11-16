FROM python:3.8

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV app /app
ADD . ${app}
WORKDIR ${app}
RUN pip install --user -r requirements.txt  -i http://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn

# CMD ["python", "main.py"]

# 将使用gunicorn 更加成熟和稳定
ENV PATH ${PATH}:/root/.local/bin
CMD ["gunicorn", "main:app", "-w", "4", "-b", "0.0.0.0:8080", "-k", "uvicorn.workers.UvicornWorker"]
