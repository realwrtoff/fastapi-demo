#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

统一响应状态码

"""

from typing import Union

from fastapi import status
from fastapi.responses import JSONResponse, Response


def resp_200(*, data: Union[list, dict, str] = None, message: str = "Success") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'message': message,
            'data': data,
        }
    )


def resp_500(*, data: Union[list, dict, str] = None, message: str = "Internal Server Error") -> Response:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            'code': 500,
            'message': message,
            'data': data,
        }
    )


# 请求参数格式错误
def resp_4001(*, data: Union[list, dict, str] = None,
              message: Union[list, dict, str] = "Request Validation Error") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 4001,
            'data': data,
            'message': message,
        }
    )


# 用户token过期
def resp_4002(*, data: Union[list, dict, str] = None, message: str = "Request Fail") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 4002,
            'data': data,
            'message': message,
        }
    )


# token认证失败
def resp_4003(*, data: Union[list, dict, str] = None, message: str = "Request Fail") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 4003,
            'data': data,
            'message': message,
        }
    )


# 内部验证数据错误
def resp_5002(*, data: Union[list, dict, str] = None, message: Union[list, dict, str] = "Request Fail") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 5002,
            'data': data,
            'message': message,
        }
    )
