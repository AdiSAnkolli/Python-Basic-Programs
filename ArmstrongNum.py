for i in range(1001):
    num=i
    result=0
    n=len(str(i))
#As numerical variables do not contain length property, they need to be converted to string
    while(i!=0):
        digit=i%10
        result=result+digit**nee
        i=i//10
# // stands for division truncate, which returns integer part of the quotient after division, that is the number before decimal point
        if num==result:
            print(num)