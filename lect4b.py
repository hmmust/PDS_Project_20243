students = {202201:'Aya Taweel',202202:'Nadeen Qoqas',
            202203:'Rana Hindi',202204:'Leen Malkawi'}

students_emails={id:[name
                     ,f"{name.lower().replace(" ",".")}@uop.edu.jo"] 
                 for id,name in students.items()}
print(students_emails)
