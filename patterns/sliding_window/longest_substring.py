s = "abcabcedbb"


def find_langest_string(s):
    char_set = set()
    start = 0
    max_length = 0
    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_length = max(max_length, end - start + 1)

    return max_length


print(find_langest_string(s))
