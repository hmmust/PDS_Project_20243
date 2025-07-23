students = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
students2= (f"{s.lower().replace(" ",".")}@uop.edu.jo" 
            for s in students)
emails= [f"{s.lower().replace(" ",".")}@uop.edu.jo" 
            for s in students]
print(*students2)
print(emails)

