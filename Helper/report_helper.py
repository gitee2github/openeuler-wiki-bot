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

import xlsxwriter


class ReportHelper(object):

    @staticmethod
    def generate_sheet_sig(sig_sheet, sig_list):
        sig_sheet.write('A1', 'Sig')
        sig_sheet.write('B1', '软件包')
        sig_sheet.write('C1', '软件包URL')

        row = 1
        col = 0
        for sig in sig_list:
            for package in sig.get_package_list():
                sig_sheet.write(row, col, sig.get_sig_name())
                sig_sheet.write(row, col + 1, package.get_package_name())
                sig_sheet.write(row, col + 2, package.get_url())
                row = row + 1

    @staticmethod
    def generate_sheet_pr(pr_sheet, sig_list):
        pr_sheet.write('A1', 'Sig')
        pr_sheet.write('B1', '软件包')
        pr_sheet.write('C1', '软件包URL')
        pr_sheet.write('D1', 'PR title')
        pr_sheet.write('E1', 'PR url')

        row = 1
        col = 0
        for sig in sig_list:
            for package in sig.get_package_list():
                for pr in package.get_pr_list():
                    pr_sheet.write(row, col, sig.get_sig_name())
                    pr_sheet.write(row, col + 1, package.get_package_name())
                    pr_sheet.write(row, col + 2, package.get_url())
                    pr_sheet.write(row, col + 3, pr.get_title())
                    pr_sheet.write(row, col + 4, pr.get_url())
                    row = row + 1

    @staticmethod
    def generate_sheet_issue(issue_sheet, sig_list):
        issue_sheet.write('A1', 'Sig')
        issue_sheet.write('B1', '软件包')
        issue_sheet.write('C1', '软件包URL')
        issue_sheet.write('D1', 'Issue title')
        issue_sheet.write('E1', 'Issue url')

        row = 1
        col = 0
        for sig in sig_list:
            for package in sig.get_package_list():
                for issue in package.get_issue_list():
                    issue_sheet.write(row, col, sig.get_sig_name())
                    issue_sheet.write(row, col + 1, package.get_package_name())
                    issue_sheet.write(row, col + 2, package.get_url())
                    issue_sheet.write(row, col + 3, issue.get_title())
                    issue_sheet.write(row, col + 4, issue.get_url())
                    row = row + 1

    @staticmethod
    def generate_report(sig_list, file_path='sig_info.xlsx'):
        print("===== Start Generate Report =====")
        workbook = xlsxwriter.Workbook(file_path)
        sig_sheet = workbook.add_worksheet(name="sig_info")
        ReportHelper.generate_sheet_sig(sig_sheet, sig_list)

        pr_sheet = workbook.add_worksheet(name="pr_info")
        ReportHelper.generate_sheet_pr(pr_sheet, sig_list)

        issue_sheet = workbook.add_worksheet(name="issue_info")
        ReportHelper.generate_sheet_issue(issue_sheet, sig_list)

        workbook.close()
        print("===== Generate Report Done =====")
        print("Report file: ", file_path)

    @staticmethod
    def print_sig_list(sig_list):
        print("===== Start Print Sig List =====")
        print("Total sig num: ", len(sig_list))
        for sig in sig_list:
            print(sig.get_sig_name())
            for maintainer in sig.get_maintainers():
                print(maintainer.get_name())
        print("===== Print Sig List Done =====")

