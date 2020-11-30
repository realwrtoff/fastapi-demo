#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from typing import Optional
from fastapi import APIRouter, Depends
from basic import deps, response_code
from config.setting import settings
from public.util import md5

router = APIRouter()


@router.get("/login")
async def login(
        username: str,
        password: str,
        mgo_collections=Depends(deps.get_mgo_collections)):
    query = {'username': username, 'password': password}
    count = await mgo_collections[settings.USER_COLLECTION].count_documents(query)
    data = {
        'token': md5(),
        'count': count
    }
    return response_code.resp_200(data=data)
