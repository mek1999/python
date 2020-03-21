def decimalToBinary(n):  
    return bin(n).replace("0b", "")  
n=int(input())
if __name__ == '__main__':  
    print(decimalToBinary(n))  
    
