from codes import *


# region snippet
word_freq_dict = {
    'you': 0.098,
    "the": 0.020,
    'friend': 0.059
}
print(word_freq_dict)
print(word_freq_dict['you'])
word_freq_dict['you'] = 0.088
print(word_freq_dict)
word_freq_dict['her'] = 0.0392
print(word_freq_dict)
print('you' in word_freq_dict)
print('he' in word_freq_dict)
for key, value in word_freq_dict.items():
    print(key + ':' + str(value))

def word_freq(words):
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    for word, freq in freq_dict.items():
        freq_dict[word] = freq / len(words)
        return freq_dict

text = readtext("nlp/data/textbooks/grade0/text0.txt")
words = splitwords(text)
freq_dict = word_freq(words)
print(freq_dict)
# endregion snippet
