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
# Author: Sinever
# Create: 2022-02-27
# Description: This is a wiki bot tool for assisting community governance
# ******************************************************************************/


class Developer(object):

    def __init__(self, name):
        self.__name = name
        self.__comments = []
        self.__created_issues = []
        self.__summited_prs = []

    def add_comment(self, comment):
        self.__comments.append(comment)

    def add_created_issue(self, created_issue):
        self.__created_issues.append(created_issue)

    def add_summited_pr(self, summited_pr):
        self.__summited_prs.append(summited_pr)

    def get_name(self):
        return self.__name

    def get_comments(self):
        return self.__comments

    def get_created_issues(self):
        return self.__created_issues

    def get_summited_prs(self):
        return self.__summited_prs
