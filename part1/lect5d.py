names = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
first_letter = lambda n: n[0].lower() in 'an'
a_n_names = list(filter(first_letter,names))
print(a_n_names)
