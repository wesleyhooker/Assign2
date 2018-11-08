#!/usr/bin/env python3
"""
Finds the top 25 error messages in a log file and prints
them to the screen
"""
from __future__ import print_function
from urllib.request import urlopen
import sys
import re
import collections


def doc_help():
    """
    The help Function
    Args:None
    Returns: Prints error message
    """
    print("Usage is: ", sys.argv[0], "<file Input>")
    exit(1)



def open_file(web_file):
    """
    Opens a file from the web
    ARGS: the file from the web you wish to open
    RETURNS: a list variable containing the file from the web
    """
    log_file = []
    with urlopen(web_file) as the_file:
        for line in the_file:
            log_file.append(line.decode('utf-8'))
    final_file = [line.split() for line in log_file]
    return final_file


def create_error_list(log_file):
    """
    Finds error messages and saves each error message to a list
    ARGS: log_file, the file from which to find the errors
    RETURNS: a list containing all the errors
    """
    error_log = []
    for line in log_file: #log file is a list of lists
        for word in line: #line is a list
            match1 = re.match(r"^/.*", word) #starts with /and anything after
            match2 = re.match(r"^'/.*", word) #starts with '/ and anything after
            if match1:
                error_log.append(word)
            if match2:
                error_log.append(word[1:-1]) #cuts off extra ' marks
    return error_log #returns list with all errors


def count_errors(error_list):
    """
    Prints the top 25 errors
    ARGS: a list containing the errors
    RETURNS: Nothing
    """
    print(r"*** Top 25 page errors ***")
    num_errors_dict = collections.Counter(error_list)
    for error, number in num_errors_dict.most_common(25):
        print("Count: {0:<10}   Page: {1}".format(number, error))


def main():
    """
    Takes in an argument containing the server log with errors and prints
    the top 25 errors and their Path locations
    ARGS: the internet log file
    RETURNS: Nothing
    """
    if len(sys.argv) == 1 or sys.argv[1] == "-help":
        doc_help()
    #open webfile  and save to log_file variable
    log = open_file(sys.argv[1])
    #retrieve the individual errors and save to a variable list
    #[date] [error] [client] errorMessage
    error_list = create_error_list(log)
    #Display the top 25 errors
    count_errors(error_list)


if __name__ == "__main__":
    main()
    exit(0)
