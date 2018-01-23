#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2018/1/22 17:04
# @Author       : zenghao
# @File         : build_buildpack-deps.py
# @Software     : PyCharm
# @Description  : 基于当前的文件名后缀来构建docker镜像

import subprocess
import glob
import os

BASE_TAG = "registry.cn-shanghai.aliyuncs.com/russell-hub/buildpack-deps"
BASE_CMD = "docker build -t {} -f {} ."

if __name__ == '__main__':
    # TODO 从命令行获取路径
    files = glob.glob(os.path.join(".", "buildpack-deps.*"))
    for f in files:
        version = f.split("Dockerfile.")[-1]
        tag = "{}:{}".format(BASE_TAG, version)
        cmd = BASE_CMD.format(tag, f)
        print("cmd:{}".format(cmd))
        p = os.popen(cmd)
        x = p.readlines()
        for line in x:
            print line
