from codes import *


# region snippet
string = "hello world"
print(string)
print("1234")
text_1 = readtext("./nlp/data/textbooks/grade0/text0.txt")
print(text_1)
text = readtext("./nlp/data/textbooks/grade0/text0.txt")
words = splitwords(text)
li = [1, 3, 5, 7, 9, 11]
l2 = [1, 'a', ['3.14', '1.5'], 'bc']
print(li[2])
print(li[3])
li[1] = 20
print(li)
print(l2[1:3])
l2.append('a')
print(l2)
print(len(li))
print(len(l2))
for i in li:
    print(i)
# endregion snippet
