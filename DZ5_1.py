txt = input("Enter text: ")
print(f"Text is: {txt}")
find_txt = "абв"
list1 = [ i for i in txt.split() if find_txt not in i]
print(f'Final text: {" ".join(list1)}')