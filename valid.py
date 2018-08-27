hi=input("enter the data: ")
if hi.isalpha()==True: 
  if(hi=='a'or hi=='A' or hi=='e' or hi=='E' or hi=='i' or hi=='I' or hi=='o' or hi=='O' or hi=='u' or hi=='U'):
    print("vowel")
  else:
    print("consonant")
else:
  print("invalid input")
