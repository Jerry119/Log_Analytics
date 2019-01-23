import os
import datetime
import numpy as np
import matplotlib.pyplot as plt


os.system('adb shell date "+%D.%T" > log.txt')
f = open('log.txt', 'r')
time = f.read().split('\n')[0].split('.')
f.close()

date = time[0].split('/')
t = time[1].split(':')

required_time = str(datetime.datetime(int(date[2])+2000, int(date[0]), int(date[1]), int(t[0]), int(t[1]), int(t[2]), 000)-datetime.timedelta(minutes=30)) + ".000"

os.system("adb logcat -t '" + required_time[5:] + "' > log.txt")

f = open('log.txt', 'r')
lines = f.read().split('\n')
error_cnt = 0
warning_cnt = 0
info_cnt = 0
debug_cnt = 0
fatal_error_cnt = 0
verbose_cnt = 0
r_cnt = 0

for line in lines:
    if " W " in line:
        warning_cnt += 1
    elif " D " in line:
        debug_cnt += 1
    elif " I " in line:
        info_cnt += 1
    elif " E " in line:
        error_cnt += 1
    elif " F " in line:
        fatal_error_cnt += 1
    elif " V " in line:
        verbose_cnt += 1
    else:
        r_cnt += 1

objects = ('warning', 'debug_msg', 'info_msg', 'error', 'fatal_err', 'verbose_msg')
y_pos = np.arange(len(objects))
performance = [warning_cnt, debug_cnt, info_cnt, error_cnt, fatal_error_cnt, verbose_cnt]

plt.bar(y_pos, performance, align="center", alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('frequency')

plt.title('Logcat Analytics')
plt.savefig('log_analytics.jpg')
plt.show()


