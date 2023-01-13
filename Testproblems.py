# 3.Problem

def sumOfTwonum():
    g=list(map(int,input("enter the values:").split()))
    g.sort()
    c=g[-1]*g[-2]
    print(c)
sumOfTwonum()

# 4.Problem

def lengthOflist():
    data=list(map(int,input("enter the values:").split()))
    c=len(data)
    n=0
    while c>1:
        c//=2
        n+=1
        print(n)
lengthOflist()


# 5.Problem

def acendingOrder():
    g=list(map(int,input("enter the values:").split()))
    g.sort()
    print(g)
acendingOrder()


# 2.Problem


def minCost(word,N):
    mxfreq=0
    fre=[0]*26
    for i in range(len(word)):
        fre[ord(word[i])-ord('B')]=fre[ord(word[i])-ord('B')]+1
        mxfreq=max(mxfreq,fre[ord(word[i])-ord('B')])
    return N-mxfreq+1
str="BBBX"
N=len(str)
print(minCost(str,N-1))


# 1 Problem

def palindrome(num):
    n=num
    rev=0
    while(num>0):
        k=num % 10
        rev=(rev*10)+k
        num=num//10
    if (n==rev):
        return True
    else:
        return False
num=1000
num=num-1
while(True):
    if (palindrome(num)):
        break
        num=num+1
print("biggest palindrome number below:")
print(num)
