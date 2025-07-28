import random
pass_char = ['$','_','@','.','%']
students = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
emails= [f"{s.lower().replace(" ",".")}@uop.edu.jo" 
            for s in students]
passwords= [f"{s[0].upper()}{random.choice(pass_char)}{random.randint(100,999)}" 
            for s in students]
print(emails)
print(passwords)


