import os
string=" "
print("Enter words one by one(say 'exit' to end)\n")
while(string!="exit"):
    string = input(print("Enter word:"))
    os.system(f"say {string}")
