#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import APIRouter

from api.login import router as user_router
from api.course import router as course_router
from api.company import router as company_router
from api.zxb import router as zxb_router
from api.server import router as server_router
from api.cmcc import router as cmcc_router


router = APIRouter()
'''
example:
    router.include_router(xxx, tags=["xxx"], prefix="/xxx")
'''
router.include_router(user_router, prefix='/user')
router.include_router(company_router, prefix='/company')
router.include_router(course_router, prefix='/course')
router.include_router(zxb_router, prefix='/zxb')
router.include_router(server_router, prefix='/server')
router.include_router(cmcc_router, prefix='/cmcc')
