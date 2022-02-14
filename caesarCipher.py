class Cryptography:
    result = ''
    def __init__(this,txt,key):
        this.txt = txt
        this.key = key

class caesarCipher(Cryptography):
    def encryption(this):
        for i in range(len(this.txt)):
            if this.txt[i].isupper():
                this.result += chr(((ord(txt[i])-65)+(key%26))+65)
            else:
                this.result += chr(((ord(txt[i])-97)+(key%26))+97)
        return this.result

    def decryption(this):
        for i in range(len(this.txt)):
            if this.txt[i].isupper():
                this.result += chr(((ord(txt[i])-65)-(key%26))+65)
            else:
                this.result += chr(((ord(txt[i])-97)-(key%26))+97)
        return this.result


if __name__ == "__main__":
    try:
        print("1. Encryption")
        print("2. Decryption")
        while True:
            x = int(input("Enter Your choise (if you wanna quit then enter -1): "))
            if x==1:
                txt = str(input("Enter Plain Text: "))
                key = int(input("Enter Key: "))
                result = caesarCipher(txt,key).encryption()
                print(result)
            elif x==2:
                txt = str(input("Enter Plain Text: "))
                key = int(input("Enter Key: "))
                result = caesarCipher(txt,key).decryption()
                print(result)
            elif x==-1:
                print("Program Terminated :)")
                exit()
            else:
                print("Please chose 1 or 2")
    except:
        pass