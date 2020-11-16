#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import Optional
from fastapi import APIRouter, Depends
from basic import deps, response_code

router = APIRouter()


@router.get("/{collection}")
async def read_course_list(
        collection: str,
        page: Optional[int] = 1,
        page_size: Optional[int] = 10,
        mgo_collections=Depends(deps.get_mgo_collections)):
    if collection not in mgo_collections:
        return response_code.resp_4001(message=f'{collection} not support')
    records = []
    cursor = mgo_collections[collection].\
        find({}, {'_id': 0, 'id': 1}).\
        skip((page-1) * page_size).\
        limit(page_size)
    async for rec in cursor:
        records.append(rec['id'])
    return response_code.resp_200(data=records)


@router.get("/{collection}/{course_id}")
async def read_course_id(collection: str, course_id: int, mgo_collections=Depends(deps.get_mgo_collections)):
    if collection not in mgo_collections:
        return response_code.resp_4001(message=f'{collection} not support')
    rec = await mgo_collections[collection].find_one({'id': course_id}, {'_id': 0})
    return response_code.resp_200(data=rec)
