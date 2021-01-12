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


class Sig(object):

    def __init__(self, sigName):
        self.__sigName = sigName
        self.__packages = []
        self.__maintainers = []
        self.__committers = []

    def add_software(self, software):
        self.__packages.append(software)

    def add_maintainer(self, maintainer):
        self.__maintainers.append(maintainer)

    def add_committer(self, committer):
        self.__committers.append(committer)

    def get_sig_name(self):
        return self.__sigName

    def get_package_list(self):
        return self.__packages


