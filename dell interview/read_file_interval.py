#!/usr/bin/env python

import getopt
import sys
import os
import time

"""
Write a script (java, python, bash, batch or any) to read number of files in a folder in a regular
interval (example: every ‘n’ seconds) and print the output to a comma separated file
○     Contents of Output file should have the timestamp and file count
○     Script should have an option to adjust the time interval
○     Script should have an option to give unique name to the output file
"""

#file path
MONITOR_DIR = "sample_dir"


def file_write_content(filename, content):
    file_fd = open(filename, encoding='UTF-8', mode='a+')
    file_fd.write(content)
    file_fd.close()


def print_help():
    """print help for the script
    """

    # process
    print("*******************************************")
    print("Usage: the script is used to count file number ")
    print("  -h :show help")
    print("  -i :time interval")
    print("  -o :set output file")
    print("*******************************************")


def parse_args():
    """parse the args
    """
    # set varaible
    short_option = "hi:o:"
    output_file = None
    interval = None

    # process
    try:
        options, _ = getopt.getopt(sys.argv[1:], short_option)
    except getopt.GetoptError as msg:
        print("ERROR:%s" % msg)
        print_help()
        sys.exit(1)

    # process the option
    if options:
        for opt, value in options:
            if opt in ["-h"]:
                print_help()
                sys.exit()
            if opt in ["-o"]:
                output_file = value
            if opt in ["-i"]:
                interval = int(value)
    if output_file and interval:
        return interval, output_file
    else:
        print_help()
        sys.exit(1)


def count_file_numbers(dirname):
    if not os.path.isdir(dirname):
        print("The directory [%s] does not exist!" % dirname)
        sys.exit(1)

    # process
    return len(os.listdir(dirname))


if __name__ == '__main__':
    # process
    check_interval, result_output_file = parse_args()

    while True:
        file_num = count_file_numbers(MONITOR_DIR)
        timestamp = time.strftime("%d %b %Y %H:%M:%S %Z", time.localtime())
        file_content = "%s,%s," % (timestamp, file_num)
        print("Now updating the file [%s]..."% result_output_file)
        file_write_content(result_output_file, file_content)

        # sleep
        print("Now sleeping [%s]..." % check_interval)
        time.sleep(check_interval)
