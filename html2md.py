#!/usr/bin/python
# -*- coding: utf-8 -*-
import io
import os
import sys

import html2text

reload(sys)
sys.setdefaultencoding('utf8')


def convert(file_path):
    with io.open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    html_output = ""
    for line in lines:
        html_output += line

    # print(html_output)

    h = html2text.HTML2Text()
    md_output = h.handle(html_output)
    # print(md_output)

    file_name = os.path.splitext(os.path.basename(file_path))[0]
    file_dir = os.path.dirname(file_path)

    # remove prefix before '-' in file name
    if "-" in file_name:
        file_name = file_name.replace(file_name[0:file_name.index("-") + 1], "")

    # need to url encode file name
    with io.open(file_dir + os.sep + file_name + ".md", 'w', encoding='utf-8') as f:
        f.write(md_output)


def convert_all_files(root_dir):
    _files = []
    _list = os.listdir(root_dir)
    for i in range(0, len(_list)):
        path = os.path.join(root_dir, _list[i])
        if os.path.isdir(path):
            _files.extend(convert_all_files(path))
        if os.path.isfile(path) and os.path.splitext(path)[1] == '.html':
            print(path)
            convert(path)
            _files.append(path)
    return _files


convert_all_files(sys.argv[1])
