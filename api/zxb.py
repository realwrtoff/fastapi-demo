#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from typing import Optional
from fastapi import APIRouter, Depends
from basic import deps, response_code

router = APIRouter()


@router.get("/{collection}")
async def zxb_list(
        collection: str,
        page: Optional[int] = 1,
        page_size: Optional[int] = 10,
        mgo_collections=Depends(deps.get_mgo_collections)):
    if collection not in mgo_collections:
        return response_code.resp_4001(message=f'{collection} not support')
    records = []
    query = {}
    count = await mgo_collections[collection].count_documents(query)
    pages = math.ceil(count/page_size)
    out_fields = {
        '_id': 0
    }
    cursor = mgo_collections[collection].\
        find(query, out_fields).\
        skip((page-1) * page_size).\
        limit(page_size)
    async for rec in cursor:
        records.append(rec)
    data = {
        'totalCount': count,
        'totalPage': pages,
        'list': records
    }
    return response_code.resp_200(data=data)


@router.get("/{collection}/{company_id}")
async def zxb_company(
        collection: str,
        company_id: int,
        mgo_collections=Depends(deps.get_mgo_collections)):
    if collection not in mgo_collections:
        return response_code.resp_4001(message=f'{collection} not support')
    query = {'companyId': company_id}
    rec = await mgo_collections[collection].find_one(query, {'_id': 0})
    return response_code.resp_200(data=rec)