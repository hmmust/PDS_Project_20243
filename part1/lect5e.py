names = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
scores = [(15,18),(20,17),(14,19),(19,21)]
students = list(zip(names,scores))
check_scores = lambda s: (s[1][0]+s[1][1])>35

students_filtered = list(filter(check_scores,students))
students_filtered2 = [ s for s in students 
                     if (s[1][0]+s[1][1])>35 ]
students_filtered3 = [ s for s in students 
                     if s[0][0] in "AN" ]
print(students_filtered3)
