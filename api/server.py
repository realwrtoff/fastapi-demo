#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import APIRouter
from typing import Optional
from basic import response_code

router = APIRouter()


@router.get("/click", )
async def click(
        channel_id: str,
        call_back_url: str,
        idfa: Optional[str] = ''
):
    return response_code.resp_200(data={
        'channelId': channel_id,
        'callBackUrl': call_back_url,
        'idfa': idfa
    })


@router.get("/callback", )
async def callback(
        click_id: str,
        idfa: Optional[str] = ''
):
    return response_code.resp_200(data={
        'click_id': click_id,
        'idfa': idfa
    })
