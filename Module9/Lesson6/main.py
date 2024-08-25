def all_variants(text):
    l = len(text)
    for i in range(1, l + 1):
        for j in range(l - i + 1):
            yield text[j:j + i]

a = all_variants("abc")
for i in a:
    print(i)
