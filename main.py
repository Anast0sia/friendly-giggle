def count_letter(words, letter):
    count = 0
    for i in range(len(words)):
        word = words[i]
        if letter in word:
            count += 1
    return count

print(count_letter(['python', 'c++', 'c', 'scala', 'java'], 'c'))