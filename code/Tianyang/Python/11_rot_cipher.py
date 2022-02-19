a = input('Please enter a word need to be encrypted: ')
b = input('Please enter a word need to be decrypted: ')
def enc(phrase):
   ini = "abcdefghijklmnopqrstuvwxyz"
   output = ""
   for char in phrase:
       output += ini[(ini.find(char)+13)%26]
   return output

print(enc(a))

def dec(phrase):
    ini = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for char in phrase:
        output += ini[(ini.find(char)-13)%26]
    return output
print(dec(b))