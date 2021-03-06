#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import asyncpg.connection
import asyncpg.pool
from elasticsearch import Elasticsearch
from starlette.requests import Request


def get_mgo_collections(request: Request) -> asyncpg.pool.Pool:
    pool: asyncpg.pool.Pool = request.app.state.mgo_collections
    return pool


def get_es(request: Request) -> Elasticsearch:
    es: Elasticsearch = request.app.state.es
    return es
