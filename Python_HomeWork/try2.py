sales_person_1 = "Mike"
sold_out_1 = 650

sales_person_2 = "Tom"
sold_out_2 = 840

sales_person_3 = "Jennie"
sold_out_3 = 1500

salary = 200

sum_of_salary_1 = 0
sum_of_salary_2 = 0
sum_of_salary_3 = 0

if sold_out_1 or sold_out_2 or sold_out_3 <=500:
    count_1 = sold_out_1 or sold_out_2 or sold_out_3
    if count_1 <=500:
        sum_1 = (3/100)*(count_1)
        print("small")
        sum_of_salary_1 += sum_1 + salary
        print("Salary is:",sum_of_salary_1) 
if sold_out_1 or sold_out_2 or sales_person_3 >500: 
    if sold_out_1 or sold_out_2 or sold_out_3 <1000:
        count_2 = sold_out_1 or sold_out_2 or sold_out_3
        if count_2 >500 and count_2 <1000:   
            sum_2 = (5/100)*(count_2)
            print("medium")
            sum_of_salary_2 += sum_2 + salary
            print("Salary is:",sum_of_salary_2)
if sold_out_1 or sold_out_2 or sold_out_3 >1000 :
    count_3 = sold_out_1 or sold_out_2 or sold_out_3 
    if count_3 >1000:
        sum_3 = (8/100)*(count_3)
        print("Big")
        sum_of_salary_3 += sum_3 + salary + 200
        print("Salary is:",sum_of_salary_3) 

print("Small:",sum_of_salary_1)
print("Medium:",sum_of_salary_2)
print("Big:",sum_of_salary_3)



