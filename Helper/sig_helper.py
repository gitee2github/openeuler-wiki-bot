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

from Helper.package_helper import PackageHelper


URL_SIG = "https://gitee.com/openeuler/community/tree/master/sig/"
PATTERN_SIG = r'"/openeuler/community/tree/master/sig/(.*)"'
PATTERN_MAINTAINER = r"- (.*?)&#x000A;"

BlockList = [
    "openeuler/blog",
]


class SigHelper(object):

    @staticmethod
    def init_sig_info(sig_list):
        print("===== Start Init Sig Info... =====")
        tmp_sig = None

        # 获取sig列表
        page = urllib.request.urlopen(URL_SIG)
        contents = page.read().decode('utf-8')
        pattern = re.compile(PATTERN_SIG)
        signames = pattern.findall(contents)
        for signame in signames[1:]:
            sig = Sig(signame)
            sig_list.append(sig)

        # 获取每个sig的各种信息
        for sig in sig_list:
            url_maintainer = URL_SIG + sig.get_sig_name() + "/OWNERS"
            page = urllib.request.urlopen(url_maintainer)
            contents = page.read().decode('utf-8')
            pattern = re.compile(PATTERN_MAINTAINER)
            maintainer_names = pattern.findall(contents)
            print(sig.get_sig_name(), maintainer_names)
            for maintainer_name in maintainer_names:
                maintainer = Developer(maintainer_name)
                sig.add_maintainer(maintainer)

        print("===== Init Sig Info Done =====")

    @staticmethod
    def process_sig_issue(sig_list):
        print("===== Start Process Sig Issue =====")
        for sig in sig_list:
            for package in sig.get_package_list():
                PackageHelper.generate_issue_info(package)
        print("===== Process Sig Issue Done =====")

    @staticmethod
    def process_sig_pr(sig_list):
        print("===== Start Process Sig Pull Request =====")
        for sig in sig_list:
            for package in sig.get_package_list():
                PackageHelper.generate_pr_info(package)
        print("===== Process Sig Pull Request Done =====")
