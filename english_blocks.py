#!/usr/bin/python

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
                            default = "10",
                            help="Number of entries to print.")
    args = arg_parser.parse_args()

    f = codecs.open("english_blocks.json", "r", "utf-8")
    dict_tmp = json.loads(f.read())
    f.close()
    results = list()
    for k, v in dict_tmp.iteritems():
        results.append((k, v))
    shuffle(results)
    f = codecs.open("output.txt", "w", "utf-8")
    format_string = u"{0}"
    if args.trans and args.trans == option_set:
        format_string += u" : {1}"
    format_string += u"\n"
    for i in results[:int(args.count)]:
        f.write(format_string.format(i[0], i[1]))
    f.close()
