#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional
from fastapi import APIRouter, Depends
from basic import deps, response_code
from config.setting import settings

router = APIRouter()


@router.get("/cmcc")
def cmcc_search(
        mobile: Optional[int] = 0,
        name: Optional[str] = '',
        cert_id: Optional[str] = '',
        es=Depends(deps.get_es)):
    condition = {}
    if mobile > 0:
        condition['mobile'] = mobile
    if len(name) > 0:
        condition['name'] = name
    if len(cert_id) > 0:
        condition['cert_id'] = cert_id
    query = {
        'query': {
            'term': condition
        }
    }
    res = es.search(index=settings.CMCC_ES_INDEX, body=query)
    num = res['hits']['total']['value']
    if num > 0:
        data = res['hits']['hits'][0]['_source']
    else:
        data = None
    return response_code.resp_200(data=data)


@router.get("/location")
async def mobile_location(mobile: int, mgo_collections=Depends(deps.get_mgo_collections)):
    prefix = int(mobile / 10000) if mobile > 1999999 else mobile
    rec = await mgo_collections[settings.MOBILE_PREFIX_COLLECTION].find_one({'prefix': prefix}, {'_id': 0})
    return response_code.resp_200(data=rec)
