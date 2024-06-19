alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#define a function that checks if input message contains alphabets onlys
def containsOnlyAlphabets(inputStr):
    for char in inputStr:
        if not char.isapha():
            return False
    return True

#input plainText containing only alphabets
while True:
    try:
        msg = input("Input message:")
        if containsOnlyAlphabets(msg):
            break
        else: 
            print("Input message doesnot contain aplhabets only !!.")
    except ValueError:
        print("Input is not an alphabetic.Try again !!")
        
#input a positive integer(between 1 to 26) as key(shift)
while True:
    try:
        key = int(input("Enter a number between 1 and 26: "))
        if 1 <=key <=26:
            break;
        else:
            print("Input is not between 1 and 26.Try again .!!")
    except ValueError:
        print("Input is not an integer.Try again.")
        
        
def caeserEncrpytion(text,shift):
    encryptedText = ''
    text =text.upper()
    n=len(text)
    
    for i in range(n):
        c= text[i]
        loc =alpha.find(c)
        newloc =(loc +shift)%26
        encryptedText += alpha[newloc]
    return encryptedText

def ceaserDecryption(encryptedText,shift):
    decryptedText = ''
    
    n =len(encryptedText)
    
    for i in range(n):
        c = encryptedText[i]
        loc =alpha.find(c)
        newloc = (loc - shift) % 26
        decryptedText += alpha[newloc]
    return decryptedText

cipherText = caeserEncrpytion(msg,key)
decryptedText = ceaserDecryption(cipherText,key)
print("Plaintext: ",msg)
print("Shift key: ", key)
print("Ciphertext: ",cipherText)
print("Decrypted text: ", decryptedText)