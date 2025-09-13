def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        print(i, end="")
        if i in ".?:":
            print("\n")

