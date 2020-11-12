# Author: Joshua Varela

# Constant:
PLANET_NUMBERS = 4



# Array containing the planets information
def infoPlanet(planetRef):
    # declare array
    prefix = ["Planet Name: ", "Average distance from the sun: ","Mass: ", "Surface temperature: "]
    planetNames = ["Mercury", "Venus", "Earth", "Mars"]
    avgDistFromSun = ["57.9 million kilometers", "108.2 million kilometers", "149.6 million kilometers", "227.9 million kilometers"]
    planetMass = ["3.31 × 10^23kg", "4.87 × 10^24kg", "5.967 × 10^24kg", "0.6424 × 10^24kg"]
    surfacetemp= ["–173 to 430 degrees Celsius", "472 degrees Celsius", "–50 to 50 degrees Celsius", "–140 to 20 degrees Celsius"]
    
    # Display the specificed planet

    refNum = planetRef - 1
    i = 0
    for i in range(4):
        if i == 0:
            print(prefix[i], planetNames[refNum])
        if i == 1:
            print(prefix[i], avgDistFromSun[refNum])
        if i == 2:
            print(prefix[i], planetMass[refNum])
        if i == 3:
            print(prefix[i], surfacetemp[refNum])
# End infoPlanet


# Greet the user

def greeting():
    print("Welcome to \"Facts about the Solar System\"!")
    print("Which Planets would you like to learn about?")
# end Greeting

# Main Menu
def mainMenu():
    inputNum = 0

    # While loop
    while inputNum != 5:
        print("Please make a selection \n")
        inputNum = input("1. Mercury \n 2. Venus \n 3. Earth \n 4. Mars \n 5. Exit the Program \n")
        
        selectNum = int(inputNum)

        if selectNum >= 6:
            print("That is not a valid option!")
        elif selectNum !=5:
            infoPlanet(selectNum)
        else:
            break;

# end Main Menu


# main()
def main():
    greeting()
    mainMenu()
# end main()


# begin program
main()


# end of the file