Names=["Maria","Hala","Ghady","Ehsan","Joe","Zoe"]
letter= input("Please enter a letter:")
dict1={
    "Maria",
    "Hala",
    "Ghady",
    "Ehsan",
    "Joe",
    "Zoe"
}
for dict1 in Names:
    if letter in dict1:
        print(dict1)