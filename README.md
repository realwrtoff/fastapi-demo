# fastapi-demo
a learnning demo by fastapi &amp; mongo


#### Steps 
1. clone the code
```shell script
git clone https://github.com/realwrtoff/fastapi-demo.git
cd fastapi-demo
``` 
2. install requirements
```shell script
pip install -r requirements.txt 
# or
pip install -r requirements.txt -i http://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn
```
3. config your environment variables
```shell script
export MONGO_HOST=127.0.0.1
export MONGO_PORT=27017
export MONGO_DB=test
# if auth required, you need set
export MONGO_USER=your_user
export MONGO_PASSWORD=your_password
```
4. run app
```shell script
pthon3 main.py
# or 
gunicorn main:app -w 1 -b 0.0.0.0:8080 -k uvicorn.workers.UvicornWorker
```
5. use browser access the api
```shell script
http://127.0.0.1:8080/api/docs
http://127.0.0.1:8080/api/redoc
http://127.0.0.1:8080/api/course/xrkmm_course
http://127.0.0.1:8080/api/course/xrkmm_course?page=2&page_size=10
http://127.0.0.1:8080/api/course/xrkmm_course/{id}
```