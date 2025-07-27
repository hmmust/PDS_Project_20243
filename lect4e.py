generate_email=lambda name:"{}@uop.edu.jo".format(
        name.lower().replace(" ",".")
    )
ge=generate_email
print(generate_email("Aya Taweel"))
print(ge("Aya Taweel"))

