ids = [202201,202202,202203,202204]
names = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
scores = [(15,18),(20,17),(14,19),(19,21)]
students = list(zip(ids,names,scores))
print(students)
students_scores = [ s[0]+s[1] for s in scores]
students_scores = list(map(lambda m:m[0]+m[1] ,scores))
print(students_scores)