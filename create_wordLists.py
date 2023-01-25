
with open('word_list.txt', 'r') as f1, open('anagrams_wordList.txt', 'w') as f2:
    for line in f1:
        if len(line) > 3 and len(line) < 8: f2.write(line)

file = open('word_list.txt')


