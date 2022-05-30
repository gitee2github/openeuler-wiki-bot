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
import argparse

from Helper.sig_helper import SigHelper
from report.excel import ReportHelper

sig_list = []


def init_parser():
    cmd_parser = argparse.ArgumentParser(description="The openEuler wiki robot.")

    cmd_parser.add_argument("-l", "--list", action="store_true", default=False, help="list all sig names")
    cmd_parser.add_argument("-r", "--report", action="store_true", default=False, help="generate information report")

    cmd_parser.add_argument("-s", "--sig", type=str, help="get a specific sig information")
    cmd_parser.add_argument("-a", "--all", action="store_true", default=False, help="get all sig information")
    return cmd_parser


def process_list():
    SigHelper.init_sig_info(sig_list)
    ReportHelper.print_sig_list(sig_list)


def process_report_specified_sig(command_args):
    SigHelper.init_sig_info(sig_list)
    for sig in sig_list:
        if sig.get_sig_name() == command_args.sig:
            tmp_sig_list = [sig]
            SigHelper.process_sig_pr(tmp_sig_list)
            SigHelper.process_sig_issue(tmp_sig_list)
            ReportHelper.generate_report(tmp_sig_list)
            return
    print("Unrecognized sig: ", command_args.sig, ", please check input.")


def process_report_all():
    SigHelper.init_sig_info(sig_list)
    SigHelper.process_sig_pr(sig_list)
    SigHelper.process_sig_issue(sig_list)
    ReportHelper.generate_report(sig_list)


def process_report(command_args):
    if command_args.sig:
        process_report_specified_sig(command_args)
    elif command_args.all:
        process_report_all()
    else:
        print("Unrecognized command option, please check input.")


if __name__ == '__main__':
    print("Welcome to use openEuler-wiki-bot.")
    parser = init_parser()
    args = parser.parse_args()
    if args.list:
        process_list()
    elif args.report:
        process_report(args)
    else:
        parser.print_help()
    print("See you next time.")
