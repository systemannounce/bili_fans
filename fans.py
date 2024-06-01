import time
import requests
import json
import csv
import datetime
import re
import os


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
        pass

    def get_fans(self):
        try:
            self.sess.get(self.init_url, headers=self.headers)
            self.sess.cookies.set('SESSDATA', self.sessdata)
            time.sleep(1)
            json_list = self.sess.get(self.fans_url, headers=self.headers, params=self.parameter)
            self.json = json.loads(json_list.text)
            if self.json['code'] != 0:
                raise Exception(self.json['message'])
            self.total_fans = self.json['data']['total']
            self.out_fans()
            self.pages = int(self.total_fans / 50)
            if self.total_fans % 50 != 0:
                self.pages += 1
            for self.page in range(2, self.pages + 1):
                self.parameter = {
                    'vmid': self.uid,
                    'pn': self.page
                }
                json_list = self.sess.get(self.fans_url, headers=self.headers, params=self.parameter)
                if self.json['code'] != 0:
                    raise Exception(self.json['message'])
                self.json = json.loads(json_list.text)
                self.out_fans()
                time.sleep(1)
            self.re_sort()
        except Exception as e:
            print(e)
            print('程序中止，请检查问题。')

    def out_fans(self):
        users = self.json['data']['list']
        if self.page == 1:
            os.remove('./fans.csv')
        with open('./fans.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            for user in users:
                uid = user['mid']
                username = re.sub(r'[,"\n]', ' ', user['uname'])
                m_time = datetime.datetime.fromtimestamp(user['mtime'])
                user_sign = re.sub(r'[,"\n]', ' ', user['sign'])

                writer.writerow([uid, username, m_time, user_sign])

    def re_sort(self):
        with open('./fans.csv', 'r', encoding='utf-8') as file1:
            csv_reader = csv.reader(file1)
            data1 = [[int(x) if i == 0 else x for i, x in enumerate(row)] for row in csv_reader]
        sorted_data1 = sorted(data1, key=lambda x: x[0])
        header1 = ['UID', '用户名（共有{}位）'.format(self.total_fans), '关注日期', '签名']
        # 打开新的 CSV 文件进行写入
        with open('./fans.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # 写入标题行(可选)
            if header1:
                csv_writer.writerow(header1)

            # 写入排序后的数据
            csv_writer.writerows(sorted_data1)


if __name__ == '__main__':
    app = Fans()
    app.get_fans()
