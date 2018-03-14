# WAP to count the occurrences of each word in the following sentence using dict()
"""
    the clown ran after the car and car ran into the tent
    and tent fell down on the clown and the car
"""

words = {}
para = "the clown ran after the car and car ran into the tent and tent fell down on the clown and the car".replace(" ", "")

for each_word in para:
    if each_word in words:
        words[each_word] += 1
    else:
        words[each_word] = 1

print(words)