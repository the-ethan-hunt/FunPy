#This is a code to find whether two given numbers are amicable or not
#Define amicable numbers
def amicable_numbers(x,y):
    sum_x=0
    sum_y=0
    for i in range(1,x):
        if x%i==0:
            sum_x+=i
    for j in range(1,y):
        if y%j==0:
            sum_y+=j
    return sum_x==y and sum_y==x
#Program body
n_1=int(input('Enter number 1 :'))
n_2=int(input('Enter number 2:'))
print
if amicable_numbers(n_1,n_2):
    print('The numbers are amicable :)')
else:
    print('The numbers are not amicable :(')