__author__ = "ChiangWei"
__date__ = "2022/6/1"

import subprocess

# ps = [
# 	subprocess.Popen(
# 		['python', 'one_process.py', filename],
# 		stdout=subprocess.PIPE
# 	) for filename in ["data1.txt", "data2.txt", "data3.txt"]
# ]

ps = [
	subprocess.Popen(['python', 'one_process.py'],stdout=subprocess.PIPE)
]

count = 0
for p in ps:
	count += int(p.stdout.read())

print(count)
