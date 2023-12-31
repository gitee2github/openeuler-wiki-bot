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
from utils.constant import SRC_OPENEULER


class Project(object):

    def __init__(self, name):
        self.__name = name
        self.__issues = []
        self.__pull_requests = []

    def add_issue(self, issue):
        self.__issues = issue

    def add_pr(self, pr):
        self.__pull_requests = pr

    def get_name(self):
        return self.__name

    def get_url(self):
        return SRC_OPENEULER + self.__name

    def get_issues(self):
        return self.__issues

    def get_pull_requests(self):
        return self.__pull_requests
