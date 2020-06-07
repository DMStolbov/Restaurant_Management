with open("comments.txt", 'a', encoding="utf-8") as f:
    print("Please, write a comment:\n")
    text = input()
    f.write(text)
