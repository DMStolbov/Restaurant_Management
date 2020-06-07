with open("comments.txt", 'a', encoding="utf-8") as f:
    print("Please, write a comment:")
    text = input()
    f.write(f'\n{text}')
