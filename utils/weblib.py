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

import urllib.request
import re

from utils.log import logger


def get_all_pattern_strings_from_a_url(url, pattern):
    logger.info("Start to get all object names from a url.")
    result = []
    try:
        page = urllib.request.urlopen(url)
        contents = page.read().decode('utf-8')
        compiled_pattern = re.compile(pattern)
        result = compiled_pattern.findall(contents)
    except urllib.error.URLError as e:
        logger.warning(e)
    logger.info("End to get all object names.")
    return result


FORMAT_ISSUE = r"(src-openeuler/tensorflow/issues/.*\?from=project-issue)"
text = "https://gitee.com/src-openeuler/tensorflow/issues"
if __name__ == '__main__':
    print(get_all_pattern_strings_from_a_url(text, FORMAT_ISSUE))
