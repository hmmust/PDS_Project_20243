students = [25,20,18]
names= ["Aya","Rana","Nadeen"]
for i in range(1,10):
    print(i)
for s in enumerate(students):
    print(s)
for n,a in zip(names,students): #(a,b) = (1,3)
    print(a,n)
#students = [*zip(names,students)]
#students = list(zip(names,students))
students = dict(zip(names,students))
print(students)