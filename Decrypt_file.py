try:
    path = input(r'Enter the path of the file: ')
    key = int(input("ENter the key to encrypt: "))
    print("The path of the file: ",path)
    print("The key for decryption: ",key)
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
    print("Decryption done......")
except Exception:
    print("Exception came up....",Exception.__name__)
