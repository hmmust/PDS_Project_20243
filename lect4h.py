ids = [202201,202202,202203,202204]
names = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
students = list(zip(ids,names))
"""last_name = lambda n:n.split(" ")[-1]"""
students= sorted(students,key=lambda s:s[1])
print(students)