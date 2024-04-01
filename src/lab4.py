import re

file = open('src/input2.txt', 'r', encoding='utf-8')
stopwords = file.read().split()
string = '''Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!'''


def censor_text(string, stopwords):
    for stopword in stopwords:
        string = re.sub(stopword, lambda x: '*' * len(x.group()), string, flags=re.IGNORECASE)
    return string


res = censor_text(string, stopwords)
print(res)

file.close()