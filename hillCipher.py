import numpy as np

class Cryptography:
    result = []
    def __init__(this,txt,key):
        this.txt = txt
        this.key = key

class hillCipher(Cryptography):
    def encryption(this,dim):          
        ans = np.zeros((dim),dtype="int32")
        temp1 = [6,20,9]

        for i in range(dim):
            for j in range(dim):
                this.key[i][j] = this.key[i][j] * temp1[j]

        for i in range(dim):
            for j in range(dim):
                ans[i] += this.key[i][j]
                ans[i] %= 26
                ans[i] += 65

        print(chr(ans[0]),chr(ans[1]),chr(ans[2]))

if __name__ == "__main__":
    print("1. Encryption")
    print("2. Decryption") 
    ch = int(input("Enter your choice: "))    
    if ch == 1:
        txt = input("Enter plain text: ")
        dim = int(input("Enter dimenstion: "))
        key = np.zeros((dim,dim),dtype="int32")
        print("Enter key values:-")
        for i in range(dim):
            for j in range(dim):
                key[i][j] = input("[{}][{}] : ".format(i,j))
        # if len(txt)%dim != 0:
        #     txt += "x"    
        print(hillCipher(txt,key).encryption(dim))
        
    elif ch == 2:
        txt = input("Enter cipher text: ")
        dim = int(input("Enter dimention: "))
    else:
        exit("please enter 1 or 2")