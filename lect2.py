students = [25,20,18]
s_sum = 0
for s in students:
    s_sum += s
output_string= "average={},sum={}"
print("average:", s_sum/len(students))  
print(f"average:{s_sum/len(students)}" )  
print(output_string.format(s_sum/len(students)
                           ,s_sum))  

