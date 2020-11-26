# This is a simple text adventure of the Settlements created by SpaceY game using python
# author: Aryaman Chandra
# date: 26-11-2020

# importing modules
import sys
from time import sleep


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"


# user's name
name = input(bcolors.OKBLUE + "What should I call you, sir? ")

# introduction
introduction = (
    bcolors.OKBLUE
    + "Welcome "
    + name
    + ", you are at SpaceY Settlement. SpaceY is a big organisation led by Aryaman and Ashvin. It was a big success and thus led to this settlement. \n "
)

for char in introduction:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()

# places
residential = (
    "Residential Area",
    bcolors.OKBLUE + "Pranam " + name + ", you are currently in the Residential Area.",
)
agriculture = (
    "Agriculture Area",
    bcolors.OKBLUE
    + "Namaste "
    + name
    + ", you are currently in the agriculture area where aeroponics takes place. Be careful there is a lot of carbon dioxide and gases out here.",
)
massd = (
    "Mass Driver",
    bcolors.OKBLUE
    + "Pranam "
    + name
    + ", you are currently at the mass driver location you can go to different regions of the moon from here. Be ready to travel at a speed of 2.4km/s",
)
industrial = (
    "Industrial Area",
    bcolors.OKBLUE
    + "Namaste "
    + name
    + ", you are currently in the industrial area. Here asteroid refining happens. The asteroids used here are captured by SpaceY Atlas",
)
atlas = (
    "SpaceY Atlas",
    bcolors.OKBLUE
    + "Namaste "
    + name
    + ", you are currently at Atlas. Atlas is the space settlement at Lagrangian point 4. It was the first space settlement that was created. It is an asteroid capturing settlement that helps us in providing resources. ",
)

balderol = (
    "SpaceY Balderol",
    bcolors.OKBLUE
    + "Pranam "
    + name
    + ", you are currently at Balderol. Balderol is a settlement in a rille section on the far side of the moon.",
)


# where all can the user go from the current location
transitions = {
    massd: (agriculture, residential, industrial, atlas, balderol),
    agriculture: (massd, residential),
    residential: (massd, agriculture),
    industrial: (massd, atlas),
    atlas: (massd, atlas),
    balderol: (massd,),
}

location = massd

while True:
    # current location
    for char in location[1]:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n You can go to these places through SpaceY Mass Driver")

    # providing the location
    for (i, t) in enumerate(transitions[location]):
        print(i + 1, t[0])

    # selecting the location
    choice = int(input("Where do you wanna go? "))
    location = transitions[location][choice - 1]
    for char in location[1]:
        sleep(0.075)
        sys.stdout.write(char)
        sys.stdout.flush()

    # whether to end the game or not
    conti = input("\n" + bcolors.WARNING + "Do you wanna continue [yes/no]? ")
    if conti == "yes":
        print("Great!!")
    else:
        print(
            bcolors.OKBLUE
            + "Thank you for playing the SpaceY Settlement! You can watch the trailer of our settlement on aryaman.cc/spacey"
        )
        break

