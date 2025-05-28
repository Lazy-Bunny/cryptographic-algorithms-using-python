def encrypte(plain_text):
    for i in range(len(plain_text)):
        if i%2 == 0:
            permutation_box[0].append(plain_text[i])
        else:
            permutation_box[1].append(plain_text[i])
    cipher_text = ''.join(permutation_box[0]+permutation_box[1])
    permutation_box[0].clear()
    permutation_box[1].clear()
    return cipher_text
        
def decrypte(cipher_text):
    plain_text_list = []
    if len(cipher_text)%2 == 0:
        permutation_box[0].append(cipher_text[0:(len(cipher_text)//2)])
        permutation_box[1].append(cipher_text[(len(cipher_text)//2):len(cipher_text)])
    else:
        permutation_box[0].append(cipher_text[0:(len(cipher_text)//2)+1])
        permutation_box[1].append(cipher_text[(len(cipher_text)//2)+1:len(cipher_text)])
    j = 0
    k = 0
    for i in range(len(cipher_text)):
        if i%2 == 0 and len(permutation_box[0][0])>j:
            plain_text_list.append(permutation_box[0][0][j])
            j += 1
        elif len(permutation_box[1][0])>k:
            plain_text_list.append(permutation_box[1][0][k])
            k +=1
    permutation_box[0].clear()
    permutation_box[1].clear()
    plain_text = ''.join(plain_text_list)
    return plain_text
permutation_box = [[],[]]
user_input_str = input("Enter the string : ")
choice = int(input("[1]. Encryption\n[2]. Decryption\nEnter a choice : "))
if (choice == 1):
    print(encrypte(user_input_str))
elif choice == 2:
    print(decrypte(user_input_str))
else:
    print("Enter correct choice next time")    