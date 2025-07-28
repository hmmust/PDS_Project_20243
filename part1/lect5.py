ids = [202201,202202,202203,202204]
names = ['Aya Taweel','Nadeen Qoqas',
            'Rana Hindi','Leen Malkawi']
last_word = lambda n:n.split(" ")[-1]

#print(last_word("Welcome to Jordan"))
#last_names= [ last_word(s) for s in names ]
last_names= list(map(last_word,names))
print(last_names)
