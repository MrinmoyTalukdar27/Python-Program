num=[2,23 ,24 ,51 ,46 ,67]
even_numbers =[]
odd_numbers =[]

for number in num:
   if number % 2 == 0:
    even_numbers.append(number)
   else:
     odd_numbers.append(number)

print("Even numbers:",even_numbers)
print("odd numbers:",odd_numbers)

'''num = [2, 23, 24, 51, 46, 67]
even_numbers = []
odd_numbers = []

for number in num:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
'''