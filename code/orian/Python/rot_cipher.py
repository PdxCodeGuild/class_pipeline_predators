import string
import codecs
import encodings
'''
rot_cipher={
    'a':"n",
    "b": "o", 
}

userinput = input(" Enter word to encode")
userinput="a"
word_en=userinput

for n in word_en:
    n = rot_cipher.keys()
    print(rot_cipher.values())
'''
lower=string.ascii_lowercase
print(lower)

table_1=str.maketrans("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z","n,o,p,q,r,s,t,u,v,w,x,y,z,a,b,c,d,e,f,g,h,i,j,k,l,m")
# table_2=bytes.maketrans("a,b,c,d,e,f,g,h,i,j,k","0,1,2,3,4,5,6,7,8,9,10")
a_input="Hello!"
a_list=list(a_input)
low_a=str.lower(a_input)
low_input=a_input 
print(low_input)
print(low_a)
code=low_input.translate(table_1)
print(code)
# code=low_input.translate(table_2)
print(a_list)

# a=value
# print(a) 

# a=ord("d")
# num=a-96
# print(num)