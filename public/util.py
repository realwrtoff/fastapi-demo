#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import hashlib


def md5(target=None):
    if target is None:
        time_stamp = time.time()
        target = '{0}'.format(time_stamp)
    md5_obj = hashlib.md5()
    md5_obj.update(target.encode())
    return md5_obj.hexdigest()
