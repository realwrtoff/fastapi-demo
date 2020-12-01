#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aioredis
import aiomysql
from motor.motor_asyncio import AsyncIOMotorClient
from config.setting import settings


async def connect_mongo():
    mgo_client = AsyncIOMotorClient(settings.MONGO_URI)
    mgo_db = mgo_client[settings.MONGO_DB]
    mgo_collections = {
        settings.MONGO_XRKMM_COLLECTION: mgo_db[settings.MONGO_XRKMM_COLLECTION],
        settings.MONGO_XIAOHAPI_COLLECTION: mgo_db[settings.MONGO_XIAOHAPI_COLLECTION],
        settings.COMPANY_COLLECTION: mgo_db[settings.COMPANY_COLLECTION],
        settings.USER_COLLECTION: mgo_db[settings.USER_COLLECTION],
        settings.ZXB_COLLECTION: mgo_db[settings.ZXB_COLLECTION],
    }
    return mgo_client, mgo_collections


async def connect_redis():
    redis_pool = await aioredis.create_redis_pool(settings.REDIS_URI)
    return redis_pool


async def connect_mysql():
    mysql_pool = await aiomysql.create_pool(settings)
    return mysql_pool
