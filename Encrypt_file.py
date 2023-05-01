'''try:
    path = input(r'Enter the path of the file: ')
    key = int(input("ENter the key to encrypt: "))
    print("The path of the file: ",path)
    print("The key for encryption: ",key)
    f = open(path,rb)
    image = f.read()
    f.close()
    print("Yes")
    image = bytearray(image)
    for index,values in enumerate(image):
        image[index] = values**k
    f = open(path,'wb')
    f.write(image)
    f.close()
    print("Encryption done......")
except Exception:
    print("Exception came up....",Exception.__name__)


#r = open("d:\\CS Project\ACM CLUB\photo.jpeg",'r')
'''
path = input(r'Enter the path of the file: ')
key = int(input("ENter the key to encrypt: "))
print("The path of the file: ",path)
print("The key for encryption: ",key)
f = open(path,'rb')
image = f.read()
f.close()
print("Yes")
image = bytearray(image)
for index,values in enumerate(image):
    image[index] = values^key
f = open(path,'wb')
f.write(image)
f.close()
print("Encryption done......")
