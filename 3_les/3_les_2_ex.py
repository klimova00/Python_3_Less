def print_person_information(name, surname, year, city, email, number_phone):
    return f"Name - {name}, surname - {surname}, year - {year}, city - {city}, " \
           f"email - {email}, number_phone - {number_phone}."


print(print_person_information(name=input("Enter name: "), surname=input("Enter surname: "),
                         year=input("Enter your year of birth: "),
                         city=input("Enter your city: "),
                         email=input("Enter email: "),
                         number_phone=input("Enter your phone number: ")))
