# -*- coding: utf-8 -*-
# @Author: Jon Bos
# @Date:   2020-05-26
# @Last Modified by:   jonbos
# @Last Modified time: 2020-05-26
# 

import re

with open("../README.md") as fin:
    content = fin.readlines()

content.sort(key = lambda line : re.findall('\[(.*?)\]', line))

with open("README.md", "w") as fout:
	for line in content:
		fout.write(line)
