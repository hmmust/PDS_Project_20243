names = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
generate_email = lambda n: f"{n.lower().replace(" ",".")}@uop.edu.jo"
emails = list(map(generate_email,names))
emails = list(map(lambda n: f"{n.lower().replace(" ",".")}@uop.edu.jo",
                  names))
print(emails)
