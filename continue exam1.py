#programing for separating values using continue statement.
s="PYTHON PROGRAMING LANGUAGE"
print("GIVEN LINE line:",s)
i=0
while(i<len(s)):
    if(s[i] not in['A''E''I''O''U'])or(s[i]==""):
        i=i+1
        continue
    print(s[i])

