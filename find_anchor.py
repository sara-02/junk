# coding: utf-8
"""
manifest format:
[
    {
        ecosystem:<value>
        package_list: [
        [...]
        [...]
        [...]
        ]
    }
]
"""

from __future__ import division
import json
import operator


def find_highest(filename, threshold=None):
    if threshold is None:
        threshold = 20
    with open(filename, 'r') as f:
        data = json.load(f)

    p = data[0]['package_list']
    l1 = len(p)
    print l1
    d = {}
    for l in p:
        for e in l:
            if e in d:
                d[e] += 1
            else:
                d[e] = 1

    sorted_x = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    sorted_x[0]
    l2 = len(sorted_x)
    q = sorted_x[0][1]
    for i in range(l2):
        s = sorted_x[i]
        j = s[1] / l1 * 100
        j = round(j, 4)
        if j >= threshold:
            print s[0] + "        " + str(j) + "            "


def main():
    find_highest('manifest_vertx.json')
    find_highest('manifest_springboot.json')
    find_highest('manifest.json', 10)

if __name__ == '__main__':
    main()
