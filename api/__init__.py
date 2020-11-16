#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import APIRouter

from api.course import router as course_router

router = APIRouter()
'''
example:
    router.include_router(xxx, tags=["xxx"], prefix="/xxx")
'''
router.include_router(course_router, prefix='/course')
