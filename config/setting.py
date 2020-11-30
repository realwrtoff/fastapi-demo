#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    # 生产模式配置
    DEBUG: bool = False
    # 项目文档
    TITLE: str = "FastAPI项目"
    DESCRIPTION: str = "采用fastapi查询mongodb练习项目"

    API_PREFIX = '/api'
    # 文档地址 生产环境关闭 None
    DOCS_URL: Optional[str] = '{}/docs'.format(API_PREFIX)
    # 文档关联请求数据接口 生产环境关闭 None
    OPENAPI_URL: Optional[str] = '{}/openapi.json'.format(API_PREFIX)
    # 生产环境关闭 redoc 文档
    REDOC_URL: Optional[str] = '{}/redoc'.format(API_PREFIX)

    MONGO_HOST: str = os.getenv('MONGO_HOST', '127.0.0.1')
    MONGO_PORT: int = int(os.getenv('MONGO_PORT', '27017'))
    MONGO_USER: str = os.getenv('MONGO_USER', '')
    MONGO_PASSWORD: str = os.getenv('MONGO_PASSWORD', '')
    MONGO_DB: str = os.getenv('MONGO_DB', 'test')
    if MONGO_USER is None or len(MONGO_USER) == 0:
        MONGO_URI = f'mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}'
    else:
        MONGO_URI = f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}'
    MONGO_XRKMM_COLLECTION: str = os.getenv('MONGO_XRKMM_COLLECTION', 'xrkmm_course')
    MONGO_XIAOHAPI_COLLECTION: str = os.getenv('MONGO_XIAOHAPI_COLLECTION', 'xiaohapi_course')
    COMPANY_COLLECTION: str = os.getenv('COMPANY_COLLECTION', 'company')

    APP_PORT = 8080
    APP_WORKERS = int(os.getenv('APP_WORKERS', '1'))


settings = Settings()
