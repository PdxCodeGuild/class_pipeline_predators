import string
code_list = [ ]
master_list = list(string.ascii_lowercase)
entry_list = list(input('\nEnter your word or phrase to be encrypted: '))

for char in (entry_list):
    #print(char) 
    if char in master_list:   
        index = master_list.index(char)    
        if index <= 12:
            code_list.append(master_list[index + 13])
        elif index >= 13:
            code_list.append(master_list[index - 13])
    else:
        code_list.append(char)
        
encryption = ''.join(code_list)
print(f'\nHere is your encryption: {encryption}')
print()