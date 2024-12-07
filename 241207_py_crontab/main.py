from crontab import CronTab

# 创建 cron 访问
cron = CronTab(user='root')

# 增加新作业
job = cron.new(command='echo hello_world')

# 每一分钟执行一次
job.minute.every(1)

# 写入作业
cron.write()
