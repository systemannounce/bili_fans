import time
import requests
import json
import csv
import datetime
import re
import os
import sys
import count

# 这里调整是否忽略重名检查。1为开启重名检查，0为关闭重名检查。
# 今天遇到了b站服务器抽风了，获取了一堆两个三个同名粉丝，所以临时加了这个模块检查，强烈建议启用！！！！
check = 1



class Fans:
    def __init__(self):
        self.sessdata = os.environ.get('bili_sessdata')
        self.uid = os.environ.get('bili_uid')
        self.fans_url = 'https://api.bilibili.com/x/relation/followers'
        self.init_url = 'https://api.bilibili.com'

        self.page = 1
        self.pages = 1

        self.sess = requests.session()    # 构建一个session
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        }
        self.parameter = {
            'vmid': self.uid,
            'pn': 1
        }
        self.exception = 1

    def get_fans(self):
        try:
            self.sess.get(self.init_url, headers=self.headers)
            self.sess.cookies.set('SESSDATA', self.sessdata)
            time.sleep(1)
            json_list = self.sess.get(self.fans_url, headers=self.headers, params=self.parameter)
            print("current page: 1")
            self.json = json.loads(json_list.text)
            if self.json['code'] != 0:
                self.exception = self.json['code']
                raise Exception(self.json['message'])
            self.total_fans = self.json['data']['total']
            self.out_fans()
            self.pages = int(self.total_fans / 50)
            if self.total_fans % 50 != 0:
                self.pages += 1
            if self.pages > 20:    # 一千粉以后全是空白页，不浪费b站服务器资源了。
                self.pages = 20
            for self.page in range(2, self.pages + 1):
                self.parameter = {
                    'vmid': self.uid,
                    'pn': self.page
                }
                json_list = self.sess.get(self.fans_url, headers=self.headers, params=self.parameter)
                print("current page:", self.page)
                if self.json['code'] != 0:
                    self.exception = self.json['code']
                    raise Exception(self.json['message'])
                self.json = json.loads(json_list.text)
                self.out_fans()
                time.sleep(1)
            self.re_sort()
        except Exception as e:
            os.remove('./temp.txt')
            os.remove('./temp.csv')
            print(e)
            print('程序中止，请检查问题。')
            sys.exit(self.exception)

    def out_fans(self):
        users = self.json['data']['list']
        # 存入中间文件，以防出错然后文件错误修改覆盖。
        with open('./temp.csv', 'a', newline='') as f, open('./temp.txt', 'a', newline='', encoding='utf-8') as c:
            writer = csv.writer(f)
            for user in users:
                uid = user['mid']
                c.write(str(uid) + ',')    # 备份一份UID，下面统计列表内名单的唯一性
                username = re.sub(r'[,"\n]', ' ', user['uname'])
                m_time = datetime.datetime.fromtimestamp(user['mtime'])
                user_sign = re.sub(r'[,"\n]', ' ', user['sign'])

                writer.writerow([uid, username, m_time, user_sign])

    def re_sort(self):
        with open('./temp.csv', 'r', encoding='utf-8') as file1:
            if check:
                self.ex_check(file1)
            file1.seek(0)
            csv_reader = csv.reader(file1)
            # 遍历CSV文件中的每一行，将每一行的第一列转换为整数类型，同时保持其他列的原始数据类型，最终返回一个包含转换后数据的列表。
            data1 = [[int(x) if i == 0 else x for i, x in enumerate(row)] for row in csv_reader]
        sorted_data1 = sorted(data1, key=lambda x: x[0])        # 将按照第一列从小到大的顺序排序然后返回一个排序后的列表。
        header1 = ['UID', '用户名（共有{}位）'.format(self.total_fans), '关注日期', '签名']
        # 打开fans的 CSV 文件进行覆盖写入
        with open('./fans.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # 写入标题行(可选)
            if header1:
                csv_writer.writerow(header1)

            # 写入排序后的数据
            csv_writer.writerows(sorted_data1)
        os.remove('./temp.txt')
        os.remove('./temp.csv')

    def ex_check(self, fp):
        csv_reader = csv.reader(fp)
        print('b站显示共 {} 个粉丝'.format(self.total_fans))
        row_count = sum(1 for row in csv_reader)
        print('实际获取到 {} 位粉丝 '.format(row_count))
        ex_fans = count.count_names_infiles('./temp.txt')
        if ex_fans != row_count:
            self.exception = 666
            raise Exception("从b站服务器获取到多个同名粉丝，判定为无效获取。\n可能为b站服务器出错，请稍后重试或者提交issue。")



if __name__ == '__main__':
    app = Fans()
    app.get_fans()
