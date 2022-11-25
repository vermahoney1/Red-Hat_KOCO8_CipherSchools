def main_code():

    logo='''
    +-+-+-+-+-+-+-+  +-+-+-+-+-+-+-+-+-+
    |A|C|R|O|N|Y|M|  |G|E|N|E|R|A|T|O|R|
    +-+-+-+-+-+-+-+  +-+-+-+-+-+-+-+-+-+
    '''
    print(logo)

    input_list = []

    def choice():
        choice1 = input("Do you want to enter more ? (Yes or No) ")
        if choice1.lower() == "yes" :
            return True
        elif choice1.lower() == "no" :
            return False
        else:
            print("Please enter a valid choice.")
            choice2 = choice()
            return choice2

    # Taking user input 

    def user():
        user_choice = True
        while user_choice:
            user_input = input("Enter a string: ")
            input_list.append(user_input)
            user_choice = choice()

    def acronym_generator():

        # Initializing an empty string to append the acronym
        a = ""
        
        user_string = ""
        
        # for loop to append acronym      
        for word in input_list:
            if word.lower() == "of":
                user_string = user_string + word
                pass
            else:
                a = a + word[0].upper()
                user_string = user_string + " " + word

        print(f'Acronym of{user_string} is {a}.')   

    user()

    acronym_generator()

main_code()    