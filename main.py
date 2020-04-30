#!/usr/bin/env python

import re

NOUN = [
    "SSL",
    "TLS",
    "CRL",
    "CA"
]

def read_config_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf8') as f:
        return f.readlines()

def parse_line(s: str) -> str:
    for i in range(len(s)-1)[::-1]:
        if s[i].isupper() and s[i+1].islower():
            s = s[:i]+' '+s[i:]
        if s[i].isupper() and s[i-1].islower():
            s = s[:i]+' '+s[i:]
    return '_'.join(s.split())

if __name__ == '__main__':
    for content in read_config_file('zabbix_proxy.conf'):
        x = (''.join(re.findall(r'#\s\w+=', content)))
        matched = re.match(r'#\s(\w+)', x)
        if matched is not None:
            p = parse_line(matched.group(1))
            print(p.lower())
