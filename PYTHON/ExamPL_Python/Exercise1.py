income=float(input('Give your income: '))
age=int(input('Give your age: '))
if income and age <0:
    print('These values are wrong.')
else:
    if age<18:
        print('Since you are a minor, there are no taxes to pay.')
    else:
        if age<30:
            if income<12500:
                tax=income*0.02
                print('You have to pay %d $ because the percentage applied is 0.02' %tax)
            if income>= 12500 and income<25000:
                tax=income*0.04
                print('You have to pay %d $ because the percentage applied is 0.04' %tax)
            elif income>=25000:
                tax=income*0.07
                print('You have to pay %d $ because the percentage applied is 0.07' %tax)
        else:
            if income<12500:
                tax=income*0.05
                print('You have to pay %d $ because the percentage applied is 0.05' %tax)
            if income>= 12500 and income<25000:
                tax=income*0.09
                print('You have to pay %d $ because the percentage applied is 0.09' %tax)
            elif income>=25000:
                tax=income*0.15
                print('You have to pay %d $ because the percentage applied is 0.15' %tax)
