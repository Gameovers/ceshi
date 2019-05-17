import re
from collections import Counter

# 读取文件中的文本
file = open('test.txt', 'r', encoding='utf-8').read()
# 通过正则匹配到所有的中文[\u4e00-\u9fa5]
test = re.compile(r'[\u4e00-\u9fa5]')
en = "".join(test.findall(file.lower()))
# 将过滤后的元素和次数转换为字典
b = Counter(en)
# 创建文本
data = open(r'a.txt', 'a', encoding='utf-8')
# 遍历字典并将其写到文本文件中
for k, v in b.items():
    data.write(str(k) + ':' + str(v) + '\n')

data.close()
