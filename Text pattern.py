def text_search(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):

        j = 0

        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            return i

    return -1


text = "sadbutsad"
pattern = "sad"

result = text_search(text, pattern)

print("Pattern found at index:", result)