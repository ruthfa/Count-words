with open("text.txt") as my_file:
    data = my_file.read()
    text = data.split(" ")

print(text)