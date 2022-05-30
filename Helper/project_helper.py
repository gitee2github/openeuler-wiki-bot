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
from utils.log import logger
from utils.weblib import get_all_pattern_strings_from_a_url
from utils.constant import SRC_OPENEULER


FORMAT_ISSUE = r"(src-openeuler/{}/issues/.*\?from=project-issue)"
PATTERN_PAGE_NUM = r"/src-openeuler/tensorflow/issues?page=\d"


class ProjectHelp(object):

    @staticmethod
    def get_all_issues(project):
        logger.info("Start to get all issues of a project.")
        PATTERN_ISSUE = FORMAT_ISSUE.format(project.get_name())
        issue_strings = get_all_pattern_strings_from_a_url(SRC_OPENEULER + project.get_name() + "/issues", PATTERN_ISSUE)
        print(issue_strings)
        logger.info("End to get all issues of a project.")
