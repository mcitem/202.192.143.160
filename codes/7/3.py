from codes import *

# region snippet
textbooks_data = load_textbooks_data()
print(len(textbooks_data))
print(textbooks_data[0:4])

def get_diff_level(path_grade):
    diff_level = {}
    for path, grade in path_grade:
        text = readtext(path)
        words = splitwords(text)
        grade = int(grade)
        for word in words:
            if word in diff_level and diff_level[word] <= grade:
                continue
            else:
                diff_level[word] = grade
    return diff_level

diff_level = get_diff_level(textbooks_data)
print(diff_level)
save_private(diff_level, "./data/tmp/diff_level")
diff_level = load_private('./data/tmp/diff_level')
print(diff_level)
text = readtext("nlp/data/reading/train/text0.txt")
print(text)
words = splitwords(text)
print(len(words))
grade_freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
li = [0] * 3
l2 = ['a'] * 5
print(li)
print(l2)
grade_freq = [0] * 12
for word in words:
    if word in diff_level:
        grade = diff_level[word]
        grade_freq[grade] += 1
    else:
        continue
print(grade_freq)
num = sum(grade_freq)
print(num)
for i in range(12):
    grade_freq[i] /= num
print(grade_freq)

def extract_features(path, diff_level):
    text = readtext(path)
    words = splitwords(text)
    grade_freq = [0] * 12
    for word in words:
        if word in diff_level:
            grade = diff_level[word]
            grade_freq[grade] += 1
        else:
            continue
    num = sum(grade_freq)
    for i in range(12):
        grade_freq[i] /= num
    return grade_freq

grade_freq = extract_features("nlp/data/reading/train/text1.txt", diff_level)
print(grade_freq)
# endregion snippet
