

import numpy as np
number = np.random.randint(1, 101) # загадываем число
print (number)
count = 0
while True:
    count +=1
    predict_number = int(input("Input the number"))
    if predict_number > number:
        print('Input number is more')
    elif predict_number < number:
        print ('Input number is less')
    else:
        print (f"Your number {predict_number} is correct. Number of attempts = {count}")
        break
    

