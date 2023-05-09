import re
s="192.168.225.255，156.234.156.215，1.2.3.4, 233.1.1.1"
print(re.findall(r'\d+.\d+.\d+.\d+',s))
#统计不同单词出现的次数
# word.txt
# cat word.txt | tr -s ' ' '\n' | sort | uniq -c 