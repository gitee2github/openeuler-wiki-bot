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


class StandReportHelper(object):

    @staticmethod
    def print_sig_list(sig_list):
        print("===== Start Print Sig List =====")
        print("Total sig num: ", len(sig_list))
        for sig in sig_list:
            print(sig.get_name())
            print("maintainers:")
            for maintainer in sig.get_maintainers():
                print(maintainer.get_name())
            print("projects:")
            for project in sig.get_projects():
                print(project.get_name())
                for issue in project.get_issues():
                    print(issue.get_url)
                for pr in project.get_pull_requests():
                    print(pr.get_url())
        print("===== Print Sig List Done =====")

