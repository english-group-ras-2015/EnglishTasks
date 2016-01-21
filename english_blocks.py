#!/usr/bin/python

__author__ = 'alexander'

import json
import codecs
from random import shuffle

if __name__ == '__main__':
    f = codecs.open("english_blocks.json", "r", "utf-8")
    dict_tmp = json.loads(f.read())
    f.close()
    results = list()
    for k, v in dict_tmp.iteritems():
        results.append((k, v))
    shuffle(results)
    f = codecs.open("output.txt", "w", "utf-8")
    for i in results:
        f.write(u"{0} : {1}\n".format(i[0], i[1]))
    f.close()
