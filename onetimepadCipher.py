import random as rm

class Cryptography:
    result = ''
    def __init__(this,txt,key):
        this.txt = txt
        this.key = key

class onetimepadCipher(Cryptography):
        def getNum(this,num):
            txtnum = [] 
            for i in this.txt:
                txtnum.append(ord(i)-num)
            return txtnum

        def genRandNum(this):
            randnum = []
            for i in range(len(this.txt)):
                randnum.append(rm.randrange(0,27))
            return randnum

        def getSum(this,x):
            randnum = this.genRandNum()
            for i in range(len(x)):
                x[i] = x[i]+randnum[i]
                if x[i]>26:
                    x[i] -= 26
                else:
                    pass    
            return x    

        def encryption(this):  
            if this.txt.isupper():
                txtnum = this.getNum(65)
                sum = this.getSum(txtnum)
                this.result = []
                for i in sum:
                    this.result.append(chr(i+65))
                return this.result    
            else:
                txtnum = this.getNum(97)
                sum = this.getSum(txtnum)
                this.result = []
                for i in sum:
                    this.result.append(chr(i+97))
                return this.result 
                   
                
if __name__ == "__main__":
    txt = str(input("Enter plain text: "))
    key = ""
    print("Encrypted text: ")
    print(onetimepadCipher(txt,key).encryption())