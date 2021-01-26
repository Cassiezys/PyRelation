import jieba
import jieba.posseg as pseg  # 词性标注
import json
from config import config

jieba.load_userdict(config['DICT_PATH']) #读取自定义词典
characterName = {}
names = {}
relationships = {}
count= {}

# 读取所有的人名
with open(config['NAME_PATH'], 'r', encoding='utf-8') as f:
    for line in f.readlines():
        localNames = line.split()
        for name in localNames[1:]:
            characterName[name] = localNames[0]

beautiful_format = json.dumps(characterName, indent=4, ensure_ascii=False)
print(beautiful_format)
exit()

with open(config['TXT_PATH'], 'r', encoding='utf-8') as f:
    for line in f.readlines():
        count += 1
        lineNames = []  # 本行所有人名
        wordsInfo = pseg.cut(line)
        for word,flag in wordsInfo:
            if flag == 'nr' and len(word) >=2 and (word in characterName):
                word = characterName[word]
