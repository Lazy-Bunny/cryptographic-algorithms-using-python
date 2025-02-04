def encryption(left, right, round_key):
    xor_container = []
    for bit, k in zip(round_key, right):
        xor_bit = int(bit) ^ int(k)
        xor_container.append(str(xor_bit))
    function_result = ''.join(xor_container)
    xor_container.clear()
    for l, r in zip(left, function_result):
        left_xor_bit = int(l) ^ int(r)
        xor_container.append(str(left_xor_bit))
    left_xor_result = ''.join(xor_container)
    return right + left_xor_result
def decryption(left, right, round_key):
    xor_container = []
    for bit, k in zip(round_key, right):
        xor_bit = int(bit) ^ int(k)
        xor_container.append(str(xor_bit))
    function_result = ''.join(xor_container)
    xor_container.clear()
    for l, r in zip(left, function_result):
        left_xor_bit = int(l) ^ int(r)
        xor_container.append(str(left_xor_bit))
    left_xor_result = ''.join(xor_container)
    return left_xor_result + left


input_string = "hello girl"
input_in_binary = '01101000011001010110110001101100011011110010000001100111011010010111001001101100'
left_plain = input_in_binary[:len(input_in_binary)//2]
right_plain = input_in_binary[len(input_in_binary)//2:]
key = '11010011001010011001010111010101110101010110101010111110101010110101010101010111'
cipher_text = encryption(left_plain, right_plain, key)
print(f"Cipher text: {cipher_text}\n")
left_cipher = cipher_text[:len(cipher_text)//2]
right_cipher = cipher_text[len(cipher_text)//2:]
decrypted_text = decryption(left_cipher, right_cipher, key)
plain = left_plain + right_plain  # Expected original plaintext
if decrypted_text == plain:
    print(f"Plain_text : {plain} : hello girl")
    print("Decryption Successful")
else:
    print("Decryption Failed")