num1 = input("enter a number: ")
num2 = input("enter a number: ")
add_zero = "0"

count_num1= 0
count_num2= 0
for letter_num1 in num1:
    count_num1 = count_num1 + 1

for letter_num2 in num2:
    count_num2 = count_num2 + 1

if count_num1>count_num2:
    count_diff = count_num1 - count_num2
    num2 = add_zero*count_diff + num2

else:
    count_diff = count_num2 - count_num1
    num1 = add_zero*count_diff + num1





count = 0
for letter in num1:
    count = count + 1

carry = 0
final_sum = " "
while count>0 :
    addition = int(num1[count -1]) + int(num2[count -1]) + carry
    carry = addition//10
    unit_place = addition%10

    if count != 1:
        final_sum =  str(unit_place) + str(final_sum)
        count = count - 1
    else:
        final_sum =   str(addition) + str(final_sum)
        count = count - 1

print(final_sum)













