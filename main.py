#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI
import uvicorn
# import gunicorn
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware


from config.setting import settings
from basic.errors import http_error_handler, http422_error_handler
from basic.logger import logger
from db.database import connect_mongo, connect_es
from api import router as api_router

app = FastAPI(docs_url=settings.DOCS_URL, openapi_url=settings.OPENAPI_URL, redoc_url=settings.REDOC_URL)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
async def on_startup() -> None:
    app.state.mgo_client, app.state.mgo_collections = await connect_mongo()
    app.state.es = await connect_es()
    logger.info('连接数据库成功...')


@app.on_event('shutdown')
async def on_shutdown() -> None:
    app.state.mgo_client.close()
    app.state.es.close()
    logger.info('关闭数据库, app退出')


app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(RequestValidationError, http422_error_handler)

app.include_router(api_router, prefix=settings.API_PREFIX)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=settings.APP_PORT, workers=settings.APP_WORKERS)
