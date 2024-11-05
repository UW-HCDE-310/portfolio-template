words = ["apple", "banana", "avocado", "cherry", "apricot", "qwtp"]

for word in words:
    if word[0] is "a":
        print(word[0])
        continue
    elif word[0] is "b":
        print(word[0])
    if word == "apple":
        break

