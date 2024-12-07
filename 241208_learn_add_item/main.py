import os
import datetime
print(datetime.datetime.now().strftime('%y%m%d'))


# 获取当前目录
current_directory = os.getcwd()

# 获取当前目录下的所有项
entries = os.listdir(current_directory)


# 过滤出所有以数字开头的子目录，并排除前6个字符不是数字的目录
directories = [d for d in entries if os.path.isdir(os.path.join(current_directory, d)) and d[:6].isdigit()]

# 对目录列表进行排序
directories.sort()

# 打印排序后的目录列表
for directory in directories:
    print(directory)

today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow.strftime('%y%m%d'))

today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=61)
print(tomorrow.strftime('%y%m%d'))
