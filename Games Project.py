class Games:
    def __init__(self):
        print("Welcome to the Games project.\nTo start Even-Odd game enter 1, and to start average game enter 2.\nYou may enter 'X' any time to exit this game")
        self.Choose()

####################### Start Choose Method #######################
    def Choose(self):
        choice = input('Enter the game number: ')
        # Handle the closing with 'X' condition
        if choice == 'X':
            print('Closing the game')
            pass
        # Start Even_Odd Method
        elif choice == '1':
            self.Even_Odd()
        # Start Average Method
        elif choice == '2':
            self.Average()
        # Handle the invalid input
        else:
            print('You may only enter 1 Or 2\n')
            self.Choose()
####################### End Choose Method #######################

####################### Start Even_Odd Method #######################
    def Even_Odd(self):
        print("Welcome to the Even-Odd game")

        # An infinite loop until user enter 'X'
        while True:

            inp = input('Please enter a number: ')
            # Handle the closing with 'X' condition
            if inp == 'X':
                print('Closing the game')
                break
            
            # Validate the input
            try:
                num = int(inp)
            except ValueError:
                print('Please enter a valid NUMBER')
            # Print the result
            else:
                if num%2 == 0:
                    print('Even Number')
                else:
                    print('Odd Number')
####################### End Even_Odd Method #######################

####################### Start Average Method #######################
    def Average(self):
        print('This is a program to give as many numbers as you like and get their average\n')

        while True:

            NumSum = 0
            count = input('How many numbers you want to enter: ')
            # Handle the closing with 'X' condition
            if count == 'X':
                print('Closing the game')
                break
            
            # Validate the input
            try:
                count = int(count)
            except ValueError:
                print('Please enter a valid NUMBER')
            # Loop the count to create the desired inputs
            else:
                for n in range(1, count+1):
                    num = float(input('Enter the {} number: '.format(n)))
                    NumSum += num
                # Calculate the result
                result = NumSum/count
                # Print the result
                print('The average is: ', result)
####################### End Average Method #######################

G = Games()
