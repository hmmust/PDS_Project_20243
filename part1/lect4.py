students = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
students_emails = [ s  for s in students]
students_emails = {  s:s  for s in students}
students_emails = {  s.split(' ')[0].lower():
    #s.lower().replace(" ",".")+"@uop.edu.jo"
    f"{s.lower().replace(" ",".")}@uop.edu.jo"
    #"{}@uop.edu.jo".format(s.lower().replace(" ","."))
    for s in students}

print(students_emails)
