#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
from types import FrameType
from typing import cast
from loguru import logger
from datetime import timedelta


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage(),
        )


# logging configuration
LOGGING_LEVEL = logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

# sink可自主配置
logger.configure(
    handlers=[
        {"sink": sys.stdout, "level": LOGGING_LEVEL},
        {"sink": './log/runtime.log', "level": LOGGING_LEVEL, "rotation": timedelta(hours=1)}]
)
