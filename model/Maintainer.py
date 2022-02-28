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

from model.Developer import Developer


class Maintainer(Developer):

    def __init__(self):
        self.__received_prs = []

    def add_received_pr(self, received_pr):
        self.__received_prs.append(received_pr)

    def get_received_pr(self):
        return self.__received_prs
