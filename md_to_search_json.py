#coding=utf-8

#Created by Alfred Jiang 20150514


import sys
import os
import json

iosnotebook_project_url = "https://github.com/viktyz/iosnotebook/blob/master/"

list = []

#获取脚本文件的当前路径
def current_file_dir():

     path = sys.path[0]

     if os.path.isdir(path):

         return path

     elif os.path.isfile(path):

         return os.path.dirname(path)

def parse_file(filepath, filename):

    url_string = iosnotebook_project_url

    if str(filename).startswith('Note_'):

        url_string = url_string + 'Notes/' + filename

    elif str(filename).startswith('JavaScript_'):

        url_string = url_string + 'JavaScript/' + filename

    elif str(filename).startswith('Python_'):

        url_string = url_string + 'Python/' + filename

    else:

        return


    file = open(filepath + '/' + filename, 'r')

    is_name_section = False
    is_tag_section = False
    is_session_section = False

    name_string = ''
    tag_string = ''
    session_string = ''

    for linenum, line in enumerate(file.readlines()):

        if len(str(line).strip('\n')) == 0:

            continue

        if '### 方案名称' in line:

            is_name_section = True
            is_tag_section = False
            is_session_section = False

            continue

        if '### 关键字' in line:

            is_name_section = False
            is_tag_section = True
            is_session_section = False

            continue

        if '### 需求场景' in line:

            is_name_section = False
            is_tag_section = False
            is_session_section = True

            continue

        if '### 参考链接' in line:

            is_name_section = False
            is_tag_section = False
            is_session_section = False

            break

        if is_name_section == True and len(str(line).strip('\n')) != 0 :

            name_string = name_string + str(line).strip('\n')

        if is_tag_section == True and len(str(line).strip('\n')) != 0:

            tag_string = tag_string + str(line).strip('\n')

        if is_session_section == True and len(str(line).strip('\n')) != 0:

            session_string = session_string + str(line).strip('\n')

    info = dict()

    info['title'] = name_string
    info['category'] = session_string
    info['tags'] = tag_string
    info['url'] = url_string
    info['date'] = ''

    list.append(info)

def get_file_from_dir(dir,callback):

    for root,dirs,files in os.walk(dir):

        for item in files:

            extension = os.path.splitext(item)[1][1:]

            callback(root, item)

# 主函数
def main():

    get_file_from_dir(current_file_dir(), parse_file)

    json.dump(list, open(r'Other/search.json', 'w'),ensure_ascii=False, indent=1)

if __name__ == '__main__':
  main()