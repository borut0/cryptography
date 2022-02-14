class Cryptography:
    result = ''
    def __init__(this,txt,key):
        this.txt = txt
        this.key = key

class polyalphabeticCipher(Cryptography):
    def isequal(this):
        if len(this.txt) == len(this.key):
            return this.key 

    def encryption(this,key):
        for i in range(len(this.txt)):
            if this.txt[i].isupper():
                this.result += chr((((ord(this.txt[i])-65)+(ord(key[i])-65))%26)+65)
            else:
                this.result += chr((((ord(this.txt[i])-97)+(ord(key[i])-97))%26)+97)
        return this.result
    
    def withKey(this):
        if this.isequal():
            pass
        else:
            while True:
                this.key += this.key
                if len(this.key) >= len(this.txt):
                    this.key = this.key[0:len(this.txt)]
                    this.result = this.encryption(this.key)
                    return this.result

    def withoutKey(this):
        if this.isequal():
            pass
        else:
            this.key += this.txt
            if len(this.key) >= len(this.txt):
                this.key = this.key[0:len(this.txt)]
                this.result = this.encryption(this.key)
                return this.result
            

if __name__ == "__main__":
    txt = str(input("Enter plain text: "))
    key = str(input("Enter key: "))
    print("With key : "+polyalphabeticCipher(txt,key).withKey())
    print("without key : "+polyalphabeticCipher(txt,key).withoutKey())