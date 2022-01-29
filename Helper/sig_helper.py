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

from utils.Sig import Sig
from utils.Package import Package

from Helper.package_helper import PackageHelper


url_sigs = "https://gitee.com/openeuler/community/tree/master/sig"
sig_pattern = r"- name: (.*)"
openeuler_software_pattern = r'"/openeuler/community/tree/master/sig/(.*)"'
src_openeuler_software_pattern = r"- (src-openeuler/.*)"

BlockList = [
    "openeuler/blog",
]


class SigHelper(object):

    @staticmethod
    def init_sig_info(sig_list):
        print("===== Start Init Sig Info... =====")
        tmp_sig = None

        page = urllib.request.urlopen(url_sigs)
        contents = page.read().decode('utf-8')
        pattern = re.compile(openeuler_software_pattern)
        signames = pattern.findall(contents)
        for signame in signames[1:]:
            sig = Sig(signame)
            sig_list.append(sig)
        # print(sig_list)
        lines = contents.split("\n")
        for line in lines:
            result = re.search(openeuler_software_pattern, line)
            if result:
                # print("get one openeuler software: ", result.group(1))
                tmp_package = Package(result.group(1))
                if tmp_package.get_package_name() in BlockList:
                    # print(tmp_package.getSoftwareName(), " is blocked, skip and continue")
                    continue
                if tmp_sig:
                    tmp_sig.add_software(tmp_package)
                continue

            result = re.search(src_openeuler_software_pattern, line)
            if result:
                # print("get one src-openeuler software: ", result.group(1))
                tmp_package = Package(result.group(1))
                if tmp_package.get_package_name() in BlockList:
                    # print(tmp_package.getSoftwareName(), " is blocked, skip and continue")
                    continue
                if tmp_sig:
                    tmp_sig.add_software(tmp_package)
                continue
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
