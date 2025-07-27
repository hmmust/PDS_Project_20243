generate_email=lambda name,domain:"{}@{}".format(
        name.lower().replace(" ","."),domain
    )
ge=generate_email
print(generate_email("Aya Taweel","gmail.com"))
print(ge("Aya Taweel","outlook.com"))

