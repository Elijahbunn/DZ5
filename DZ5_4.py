with open('Text1.txt', 'r') as txt_file: text1 = list(txt_file.read())
print(text1)

text2 = []
count = 1

def CreatText2(text1, text2, count):
    for i in range(int(len(text1))):
        if i<int(len(text1))-1 and text1[i] == text1[i+1]:
            count += 1
        elif i == int(len(text1)) and text1[i] == text1[i-1]:
            count += 1
            text2.append(f"{str(count)}{text1[i]}")
        elif i == int(len(text1)) and text1[i] != text1[i-1]:
            text2.append(f"{str(count)}{text1[i-1]}")
            text2.append(f"1{text1[i]}")
        else:
            text2.append(f"{str(count)}{text1[i]}")
            count = 1
    print(text2)

CreatText2(text1, text2, count)
with open('Text2.txt', 'a') as data:
    for i in range(len(text2)):
        data.write(text2[i])
    data.write("\n")