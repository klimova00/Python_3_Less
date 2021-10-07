def int_func(word):
    lattin_char = "abcdefghijklmnopqrstuvwxyz"
    return word.title() if not set(word).difference(lattin_char) else \
        print("Error word")


words = input("Input your str only with small latin letters : ").split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')
