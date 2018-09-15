# !/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import re

file_path = "../data/idiom.json"

# 查找包含某字词的全部成语
def findIdiomsByWord(in_word):
    with open( file_path, 'r' , encoding='utf-8' ) as f:
        file_dict = json.load(f)
        # 匹配汉语字符串。某些成语包含逗号！！！
        word_pattern = "([\u4e00-\u9fa5]*，?[\u4e00-\u9fa5]*"+in_word+"[\u4e00-\u9fa5]*，?[\u4e00-\u9fa5]*)"
        match_word_list = []
        for item in file_dict:
            if re.findall( word_pattern , item['word'] ):
                match_word_list.append(re.findall( word_pattern , item['word'] )[0])
        return match_word_list

idioms_result = findIdiomsByWord("万夫")
print(idioms_result)

