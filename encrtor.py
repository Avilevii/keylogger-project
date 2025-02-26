def xor_cipher(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) ^ key)
    return encrypted_text

user_input = input("הקלד את הטקסט להצפנה: ")
key = int(input("הזן את מפתח ה-XOR (key): "))

encrypted_output = xor_cipher(user_input, key)
print("הטקסט המוצפן: ", encrypted_output)

decrypted_output = xor_cipher(encrypted_output, key)
print("הטקסט המפוענח: ", decrypted_output)