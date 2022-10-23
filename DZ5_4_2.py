with open('Text3.txt', 'r') as txt_file: text2 = list(txt_file.read())
print(text2)

text3 = []

def CreatText3(text1, text2):
    i = 0
    while i < int(len(text1)):
        text2.append(int(text1[i])*text1[i+1])
        i += 2
    print(text2)

CreatText3(text2, text3)
with open('Text4.txt', 'a') as data:
    for i in range(len(text3)):
        data.write(text3[i])
    data.write("\n")