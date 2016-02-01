#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'alexander'

import argparse
import json
import codecs
from random import shuffle

option_set = "on"
option_not_set = "off"


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description = "Coming soon")
    arg_parser.add_argument('--trans',
                            default = option_set,
                            help="Turn this option on if you don't want the Russian translations to show up.")
    arg_parser.add_argument('--count',
                            type = int,
                            default = 10,
                            help="Number of entries to print.")
    arg_parser.add_argument('--start',
                            default = 0,
                            type = int,
                            help="The first block to include.")
    arg_parser.add_argument('--end',
                            default = 0,
                            type = int,
                            help="The last block to include.")
    args = arg_parser.parse_args()

    f = codecs.open("english_blocks.json", "r", "utf-8")
    dict_tmp = json.loads(f.read())
    f.close()
    results = list()
    for k, v in dict_tmp.iteritems():
        if (int(k) >= args.start and int(k) <= args.end) or (int(k) >= args.start and args.end == 0):
            results.extend(v.items())
    shuffle(results)
    f = codecs.open("output.txt", "w", "utf-8")
    format_string = u"{0}"
    if args.trans and args.trans == option_set:
        format_string += u" : {1}"
    format_string += u"\n"
    length = args.count if args.count != 0 else len(results)
    for i in results[:length]:
        f.write(format_string.format(i[0], i[1]))
    f.close()
