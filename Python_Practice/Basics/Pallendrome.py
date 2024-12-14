## pallendrome 

number = int(input("Enter the value: "))
actual_number = number
reverse_number = 0


while  number !=0:
      remainder = number%10
      number= number//10
      reverse_number = (reverse_number * 10) + remainder
       
if actual_number == reverse_number:
      print("pallendrome")
else:
      print("not a pallendrome")