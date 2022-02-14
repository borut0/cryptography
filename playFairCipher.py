import string as stg
import numpy as np

class Cryptography:
    result = []
    def __init__(this,txt,key):
        this.txt = txt
        this.key = key

class playFairCipher(Cryptography):
    nkey = []
    matx = []
    def separateTxt(this):
        this.txt = list(this.txt)
        for i in range(0,len(this.txt)-1,2):
            if this.txt[i] == this.txt[i+1]:
                this.txt.insert(i+1,"x")
            else:
                pass
        if(len(this.txt)%2!=0):
            this.txt.extend("x")
        return this.txt

    def disKey(this):
        for i in this.key:
            if i in this.nkey:
                continue
            else:
                this.nkey.append(i)
        return this.nkey        

    def matrix(this):
        lsKey = this.disKey()
        this.matx.extend(lsKey)
        for i in stg.ascii_lowercase:
            if i in this.matx:
                continue
            elif i == "i":
                this.matx.append("ij")
            elif i == "j":
                continue
            else:
                this.matx.append(i)
        letter = np.array(this.matx)  
        matrix = letter.reshape(5,5)  
        print("Key matirx is : ")
        print(matrix)
        return matrix

    def whatisIndex(this,index):
        if index == 4:
            return 0
        else:
            return index+1    

    def newKey(this):
        text = this.separateTxt()
        matrx = this.matrix()
        for x in range(0,len(text),2):
            i = text[x]
            j = text[x+1]
            if i == "i" or i == "j":
                i = "ij"
            if j == "i" or j == "j":
                j = "ij"   
            i1,j1 = np.where(matrx == i)
            i2,j2 = np.where(matrx == j)
            if i1 == i2:
                this.result.append(matrx[i1,this.whatisIndex(j1)])
                this.result.append(matrx[i1,this.whatisIndex(j2)])
                
            elif j1 == j2:
                this.result.append(matrx[this.whatisIndex(i1),j1])
                this.result.append(matrx[this.whatisIndex(i2),j1])

            else:
                this.result.append(matrx[i1,j2])
                this.result.append(matrx[i2,j1])     
        return this.result


if __name__ == "__main__":
    txt = input("Enter plain text: ")
    key = input("Enter key: ")
    encryption = playFairCipher(txt,key).newKey()
    print("Encrypted text : ")
    for i in encryption:
        print(i,end=" ")