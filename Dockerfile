FROM python:3.8.3-alpine3.11
WORKDIR /app
ENV app /app
ADD . ${app}
WORKDIR ${app}
RUN pip install -r requirements.txt -i http://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn
# 使用gunicorn更加成熟和稳定,虽然用["python", "main.py"]也可以运行
CMD ["gunicorn", "main:app", "-w", "4", "-b", "0.0.0.0:8080", "-k", "uvicorn.workers.UvicornWorker"]
