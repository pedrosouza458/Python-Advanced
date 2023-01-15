import re


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching from patter {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")


test_phrase = 'This is a string with numbers 1234 and a symbol #hashtag'

test_patterns = [r'\d+']

multi_re_find(test_patterns, test_phrase)
