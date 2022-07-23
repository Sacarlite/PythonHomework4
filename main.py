'''
#1
-
'''
'''
#2
def listOfDiv(num):
    divisors=[]
    step=2
    while(step<=num):
        if(num%step==0):
            divisors.append(step)
        step=step+1
    return divisors
num=int(input())
divisors=listOfDiv(num)
print(divisors)
'''
'''
#3
def listInput():
    input_list=[]
    input_string=" "
    while True:
        input_string=input()
        if input_string =="":
            break
        input_list.append(float(input_string))
    return input_list
def listRepNums(input_list):
    end_list=[]
    for i in input_list:
        num = 0
        for j in input_list:
            if(i==j):
                num=num+1
        if(num==1):
            end_list.append(i)
    return end_list
input_list=listInput()
end_list=listRepNums(input_list)
print(end_list)
'''
'''
#4
-
'''