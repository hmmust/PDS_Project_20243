names = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
scores = [(15,18),(20,17),(14,19),(19,21)]
students = list(zip(names,scores))
def check_scores(s):
    return (s[1][0]+s[1][1])>35

students_filtered = list(filter(check_scores,students))
print(students_filtered)
