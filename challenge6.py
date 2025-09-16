text =input("enter your text : ")

i=0
result = ""
while(i<len(text)):
    result += text[len(text)-1-i]
    i+=1

print(f"the inverst is {result}")