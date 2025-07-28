students = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
#students.sort()
last_name = lambda n:n.split(" ")[-1]
#print(last_name("Aya Taweel"))
#students= sorted(students,key=last_name)
students= sorted(students,key=lambda s:s[-1])
print(students)