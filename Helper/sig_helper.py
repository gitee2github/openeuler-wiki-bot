#!/usr/bin/python3
"""
This is a wiki bot tool for assisting community governance
"""
# ******************************************************************************
# Copyright (c) Huawei Technologies Co., Ltd. 2020-2020. All rights reserved.
# licensed under the Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#     http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
# PURPOSE.
# See the Mulan PSL v2 for more details.
# Author: Hubble_Zhu
# Create: 2021-01-12
# Description: This is a wiki bot tool for assisting community governance
# ******************************************************************************/

import urllib.request
import re

from model.Sig import Sig
from model.Maintainer import Maintainer
from model.Developer import Developer
from model.Project import Project

from Helper.package_helper import PackageHelper
from utils.log import logger

URL_SIG = "https://gitee.com/openeuler/community/tree/master/sig/"
PATH_MAINTAINER = "/OWNERS"
PATH_PROJECT = "/sig-info.yaml"
PATTERN_SIG = r'"/openeuler/community/tree/master/sig/(.*)"'
PATTERN_MAINTAINER = r"- (.*?)&#x000A;"
PATTERN_PROJECT = r"repo: src-openeuler/(.*?)&#x000A;"

BlockList = [
    "openeuler/blog",
]


class SigHelper(object):

    @staticmethod
    def init_sig_info(sig_list):
        logger.info("Start to get sig info.")
        # 获取sig列表
        SigHelper.get_all_sig_names(sig_list)

        # 获取每个sig的maintainer信息
        # SigHelper.get_all_maintainer_names(sig_list)

        # 获取每个sig的project信息
        SigHelper.get_all_project_names(sig_list)
        logger.info("End to get sig info.")

    @staticmethod
    def get_all_sig_names(sig_list):
        logger.info("Start to get all sig names.")
        names = SigHelper.get_all_object_names_from_a_url(URL_SIG, PATTERN_SIG)
        for name in names[1:]:
            sig = Sig(name)
            sig_list.append(sig)
        logger.info("End to get all sig names.")

    @staticmethod
    def get_all_maintainer_names(sig_list):
        logger.info("Start to get all maintainer names.")
        for sig in sig_list:
            url = URL_SIG + sig.get_name() + PATH_MAINTAINER
            names = SigHelper.get_all_object_names_from_a_url(url, PATTERN_MAINTAINER)
            for name in names:
                maintainer = Developer(name)
                sig.add_maintainer(maintainer)
        logger.info("End to get all maintainer names.")

    @staticmethod
    def get_all_object_names_from_a_url(url, pattern):
        logger.info("Start to get all object names from a url.")
        names = []
        try:
            page = urllib.request.urlopen(url)
            contents = page.read().decode('utf-8')
            compiled_pattern = re.compile(pattern)
            names = compiled_pattern.findall(contents)
        except urllib.error.URLError as e:
            logger.warning(e)
        logger.info("End to get all maintainer names.")
        return names

    @staticmethod
    def get_all_project_names(sig_list):
        logger.info("Start to get all project names.")
        for sig in sig_list:
            url = URL_SIG + sig.get_name() + PATH_PROJECT
            names = SigHelper.get_all_object_names_from_a_url(url, PATTERN_PROJECT)
            print(sig.get_name(), names)
            for name in names:
                project = Project(name)
                sig.add_project(project)
        logger.info("End to get all project names.")

    @staticmethod
    def process_sig_issue(sig_list):
        logger.info("Start to process get issue.")
        for sig in sig_list:
            for package in sig.get_package_list():
                PackageHelper.generate_issue_info(package)
        logger.info("End to process get issue.")

    @staticmethod
    def process_sig_pr(sig_list):
        logger.info("Start to process sig pull request.")
        for sig in sig_list:
            for package in sig.get_package_list():
                PackageHelper.generate_pr_info(package)
        logger.info("End to process sig pull request.")
