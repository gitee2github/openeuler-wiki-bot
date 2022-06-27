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
# Create: 2022-05-16
# Description: This is a wiki bot tool for assisting community governance
# ******************************************************************************/
from model.Issue import Issue, IssueStatus
from model.PullRequest import PullRequest, PullRequestStatus

from utils.log import logger
from utils.weblib import get_all_pattern_strings_from_a_url
from utils.constant import SRC_OPENEULER, GITEE


'''
<a title="Submit spec file into this repository" class="title" href="/src-openeuler/aries-proxy-impl/issues/I243BJ?from=project-issue">Submit spec file into this repository
</a>
'''
FORMAT_ISSUE = r"(src-openeuler/{}/issues/.*\?from=project-issue)"
PATTERN_PAGE_NUM = r"/src-openeuler/tensorflow/issues?page=\d"

'''
<a class="title" title="Fix CVE-2022-23578 CVE-2021-41209 CVE-2021-41213 CVE-2021-41227..." href="/src-openeuler/tensorflow/pulls/51">Fix CVE-2022-23578 CVE-2021-41209 CVE-2021-41213 CVE-2021-41227...</a>
'''
FORMAT_PULLREQUEST = r"(src-openeuler/{}/pulls/\d)"


class ProjectHelp(object):

    @staticmethod
    def get_all_issues(project):
        logger.info("Start to get all issues of a project.")
        issues = []
        patten_issue = FORMAT_ISSUE.format(project.get_name())
        issue_strings = get_all_pattern_strings_from_a_url(SRC_OPENEULER + project.get_name() + "/issues", patten_issue)
        print(issue_strings)
        for e in issue_strings:
            issue = Issue('', GITEE + e, IssueStatus.OPEN)
            issues.append(issue)
        logger.info("End to get all issues of a project.")
        return issues

    @staticmethod
    def get_all_prs(project):
        logger.info("Start to get all pull requests of a project.")
        prs = []
        patten_pr = FORMAT_PULLREQUEST.format(project.get_name())
        pr_strings = get_all_pattern_strings_from_a_url(SRC_OPENEULER + project.get_name() + "/pulls", patten_pr)
        print(pr_strings)
        for e in pr_strings:
            pr = PullRequest('', GITEE + e, PullRequestStatus.OPEN)
            prs.append(pr)
        logger.info("End to get all pull requests of a project.")
        return prs


if __name__ == '__main__':
    from model.Project import Project
    project = Project("tensorflow")
    prs = ProjectHelp.get_all_prs(project)
    print(prs)
