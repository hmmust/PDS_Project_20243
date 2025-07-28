students = ['Aya','Nadeen','Rana','Leen']
students2= (s.lower() for s in students)
print(*students2)

#traditional method
students2 =[]
for s in students:
    s= s.lower()
    students2.append(s)
print(students2)

emails= {s:f"{s.lower().replace(" ",".")}@uop.edu.jo" 
            for s in students}
print(emails)