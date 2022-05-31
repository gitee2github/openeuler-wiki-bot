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
#import bs4

from model.Issue import Issue
from model.PullRequest import PullRequest


class PackageHelper(object):

    @staticmethod
    def generate_issue_info(package):
        issue_url = package.get_url() + "/issues"
        print("Issue_URL: ", issue_url)
        page = urllib.request.urlopen(issue_url)
        contents = page.read().decode('utf-8')

        # parse html
        soup = bs4.BeautifulSoup(contents, 'html.parser')
        elem_list = soup.find_all('a', attrs=['class', 'title'], href=True)
        for elem in elem_list:
            issue_title = elem.attrs['title'].strip()
            issue_url = "https://gitee.com" + elem.attrs['href']
            issue = Issue(issue_title, issue_url)
            package.add_issue(issue)
            print(issue_title, issue_url)

    @staticmethod
    def generate_pr_info(package):
        pr_url = package.get_url() + "/pulls"
        print("PullRequest URL: ", pr_url)
        page = urllib.request.urlopen(pr_url)
        contents = page.read().decode('utf-8')

        # parse html
        soup = bs4.BeautifulSoup(contents, 'html.parser')
        elem_list = soup.find_all('a', attrs=['class', 'title'], href=True)
        for elem in elem_list:
            pr_title = elem.attrs['title'].strip()
            pr_url = "https://gitee.com" + elem.attrs['href']
            pr = PullRequest(pr_title, pr_url)
            package.add_pr(pr)
            print(pr_title, pr_url)
