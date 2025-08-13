##CREATING A MAIN MENU MESSAGE

menu_message = ""
"""get birthday"""
birthdate=input("enter birthdate in format:DD/MM/YYYY")

def age_in_2032(birthdate):
    birth_year= birthdate[6:10]
    birth_year=int(birth_year)
    print(birth_year)
    age_2032=2032-birth_year
    print(f"you will be {age_2032} years old in 2032")
def main_menu():
    birthdate=input("enter birthdate in format:DD/MM//YYYY")
    while True:
        print(menu_message)
        choice=input("choose option 1-4")
        if choice=="1":
            """convert age to months"""
        elif choice=="2":
            """age in 2032"""
        elif choice=="3":
            age_in_2032
        elif choice=="4":
            break
            """Exit"""
        else:
            """ERROR"""
    main_menu()

    