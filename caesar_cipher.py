small_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
     'x','y','z',' ']
cipher_letter = ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',' ']
cipher_text = ''
plain_text = ''
input_string = input("Enter your string : ").lower()
choice = int(input("[1]. encrypt\n[2]. decrypt\nEnter your choice :"))
if choice == 1:
    for i in range(0,len(input_string)):
        # small_letter.index(input_string[i]
        cipher_text += cipher_letter[small_letter.index(input_string[i])]
    print(cipher_text)
elif choice == 2:
    for i in range(0,len(input_string)):
        plain_text += small_letter[cipher_letter.index(input_string[i])]
    print(plain_text)
else:
    print("Wrong choice try again")