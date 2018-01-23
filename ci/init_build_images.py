#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2018/1/22 15:17
# @Author       : zenghao
# @File         : init_build_images.py
# @Software     : PyCharm
# @Description  : 初始镜像构建

import click
import glob
import os
import multiprocessing
import subprocess
import commands


# 查找当前路径下所有以Dockerfile开头的文件
def search_docker_file(dirname):
    return glob.glob(os.path.join(dirname, "*", "Dockerfile*"))


def run_subprocess_and_log(f):
    cmd = "floydker build {}".format(f)
    subp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    while subp.returncode == None:
        line = subp.stdout.readline()
        if line:
            print line
    return subp.returncode


def log_ret_code(code):
    print("task finish,code is {}".format(code))


@click.command()
@click.argument('dirname')
@click.option("-p", "--parallel", default=multiprocessing.cpu_count(), type=int,
              help="parallel build num, default is cpu count")
def build(dirname, parallel):
    files = search_docker_file(os.path.abspath(dirname))
    if not files:
        print("no dockerfile found in path")
        return
    pool = multiprocessing.Pool(processes=parallel)
    for f in files:
        # run_subprocess_and_log(f)
        pool.apply_async(run_subprocess_and_log, (f,), callback=log_ret_code)
    pool.close()
    pool.join()


if __name__ == '__main__':
    build()
