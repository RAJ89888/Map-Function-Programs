numbers=[1,2,3,4,5]
EvenNum=[]
OddNum=[]
for item in range(len(numbers)):
 if(numbers[item]%2==0):
     EvenNum.append(numbers[item])
 else:
     OddNum.append(numbers[item])
print("The original list is ",numbers)
print("After separating the list :")
print("Even Number list is : ",EvenNum)
print("Odd Number list is : ",OddNum)