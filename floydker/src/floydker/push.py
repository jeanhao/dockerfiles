#!/usr/bin/env python
# -*- coding:utf-8 -*-

from subprocess import check_call, check_output
import os
import logging
import click
import click_log
from .utils import assert_image_tag_from_dockerfile

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.command()
@click.argument('dockerfile')
@click.option('--show-tag-only/--no-show-tag-only',
              help='skip build, only print out image tag name',
              default=False)
@click.option('-u', '--username', type=str)
@click.option('-p', '--password', type=str)
@click_log.simple_verbosity_option(logger)
def push(dockerfile, show_tag_only, username, password):
    image_tag = assert_image_tag_from_dockerfile(logger, dockerfile)
    if show_tag_only:
        print(image_tag)
        return

    dockerfile_dir = os.path.dirname(dockerfile)
    project_dir = os.path.dirname(dockerfile_dir)
    logger.info('--------------------------------------------')
    logger.info('[*] pushing %s with tag %s...', dockerfile, image_tag)
    logger.info('--------------------------------------------')
    if not username:
        username = os.environ.get("DOCKER_USERNAME")
    if not password:
        password = os.environ.get("DOCKER_PASSWORD")
    logging.info(check_call(
        "docker login --username={} --password={} registry.cn-shanghai.aliyuncs.com".format(username, password),
        shell=True))
    check_call('docker push {}'.format(image_tag), shell=True)


logger.info(check_output(['docker', 'images']))
