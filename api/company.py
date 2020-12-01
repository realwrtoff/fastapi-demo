#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from typing import Optional
from fastapi import APIRouter, Depends
from basic import deps, response_code

router = APIRouter()


@router.get("/{collection}")
async def company_list(
        collection: str,
        province: Optional[str] = '',
        city: Optional[str] = '',
        page: Optional[int] = 1,
        page_size: Optional[int] = 10,
        check_status: Optional[int] = 0,
        mgo_collections=Depends(deps.get_mgo_collections)):
    if collection not in mgo_collections:
        return response_code.resp_4001(message=f'{collection} not support')
    records = []
    query = {}
    if len(province) > 0:
        query['province'] = province
    if len(city) > 0:
        query['city'] = city
    if check_status == 0:
        query['check_status'] = {'$exists': False}
    else:
        query['check_status'] = check_status
    count = await mgo_collections[collection].count_documents(query)
    pages = math.ceil(count/page_size)
    out_fields = {
        '_id': 0,
        'companyId': 1,
        'name': 1,
        'province': 1,
        'city': 1,
        'address': 1,
        'establishTime': 1,
        'legalPersonName': 1,
        'regCapital': 1,
        'regCapitalCurrency': 1
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
async def company(
        collection: str,
        company_id: int,
        check_status: Optional[int] = 0,
        mgo_collections=Depends(deps.get_mgo_collections)):
    if collection not in mgo_collections:
        return response_code.resp_4001(message=f'{collection} not support')
    query = {'companyId': company_id}
    if check_status == 0:
        # 默认查找
        rec = await mgo_collections[collection].find_one(query, {'_id': 0})
        return response_code.resp_200(data=rec)
    # 更新
    update = {'$set': {'check_status': check_status}}
    res = await mgo_collections[collection].update_one(query, update)
    if res.raw_result['nModified'] > 0:
        message = 'update success'
    else:
        message = 'nothing updated, nModified is the update rec count'
    return response_code.resp_200(message=message, data=res.raw_result)
