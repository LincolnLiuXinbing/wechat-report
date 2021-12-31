import pymysql
import re
import datetime

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='wechat_report',
    charset='utf8mb4',
    port=3306)

cur = conn.cursor()

with open(r"/Users/liuxinbing/Downloads/🎮刘斩仙🗯/abby.txt", encoding='utf-8') as f:
    lines = f.readlines()
    filter_lines = []
    reg = "^.+\s\(.+\):"

    for line in lines:
        # 去除转发的聊天记录 简单过滤
        if (line.startswith('🎮刘斩仙🗯') or line.startswith('abby')) and re.match(reg, line):
            filter_lines.append(line.strip())

for line in filter_lines:
    s1 = line.find(" ")
    s2 = line.find("):")
    name = line[:s1]
    time = line[s1 + 2:s2]
    print(time)
    time = datetime.datetime.strptime(time, "%Y-%m-%d %I:%M:%S %p").strftime("%Y-%m-%d %H:%M:%S")
    print(time)
    content = line[s2 + 2:]
    print(line)
    insert_sql = f"insert into log(user,datetime,content) values ('{name}','{time}' ,'{pymysql.converters.escape_string(content)}')"
    cur.execute(insert_sql)
conn.commit()
