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


class Package(object):

    def __init__(self, softwareName):
        self.__package_name = softwareName
        self.__issues = []
        self.__pull_requests = []

    def add_issue(self, issue):
        self.__issues.append(issue)

    def add_pr(self, pull_request):
        self.__pull_requests.append(pull_request)

    def get_package_name(self):
        return self.__package_name

    def get_url(self):
        return "https://gitee.com/" + self.__package_name

    def get_issue_list(self):
        return self.__issues

    def get_pr_list(self):
        return self.__pull_requests
