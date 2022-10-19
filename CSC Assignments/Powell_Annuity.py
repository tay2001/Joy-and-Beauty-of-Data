##Future Value of an Annuity(PMT)
##Taylor Powell

##ask the questions
i = float(input("What is the annual interest rate?: "))
num = int(input("What are the number of payments per year?: "))
y = int(input("How many years?: "))
pmt = float(input("What is the periodic payment?: "))

##function for total amt of payments
def total_pay(num,y):
    t = num*y
    return t

def per_rate(i,num):
    r = (i/num)/100
    return r

def main(r,t,pmt):

    total_pay(num,y)
    per_rate(i,num)
    
    f = pmt((1+r)^t-1)/r
    return f

    print("Your future value is: ",f,".")



total_pay(num,y)
per_rate(i,num)
main(pmt,r,y,t,num)


##oh lawd heres an idiot
