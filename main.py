def main():
    menu()


def menu():
    print("|-------------------------------|")
    print("|---WELCOME TO DANIEL's PIZZA---|")
    print("|----------bon appetit----------|")
    print("|-------------------------------|")

    choice = input("""          
                                A: New Customer Registration
                                B: Regular Customer Login
                                Q: Logout  
                                
                                Please select one of the above   """).upper()

    if choice == "A":
        register()
    elif choice == "B":
        login()
    elif choice == "Q":
        raise SystemExit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

main()
