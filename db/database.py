#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    }
    return mgo_client, mgo_collections
