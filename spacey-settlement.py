# This is a simple text adventure of the Settlements created by SpaceY game using python
# author: Aryaman Chandra
# date: 26-11-2020

# importing modules like system and time to output a typing text effect
import sys
from time import sleep
import webbrowser

# using pycolors
class bcolors:
    OKBLUE = "\033[94m"
    WARNING = "\033[93m"


# username
name = input(bcolors.OKBLUE + "What should I call you, sir? ")

# introduction
introduction = (
    bcolors.OKBLUE
    + "Welcome "
    + name
    + ", you are at SpaceY Settlement. SpaceY is a big organisation led by Aryaman and Ashvin. It was a big success and thus led to this settlement. \n "
)

# the typing out effect
for char in introduction:
    sleep(0.05)
    sys.stdout.write(char)
    # makes the text come out one by one and not together
    sys.stdout.flush()

# places using tuples
residential = (
    "Residential Area",
    bcolors.OKBLUE + "Pranam " + name + ", you are currently in the Residential Area.",
)
agriculture = (
    "Agriculture Area",
    bcolors.OKBLUE
    + "Namaste "
    + name
    + ", you are currently in the agriculture area where aeroponics takes place. Be careful there is a lot of carbon dioxide and other gases out here.",
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


# where all can the user go from the current location using a dictionary and tuple
transitions = {
    massd: (agriculture, residential, industrial, atlas, balderol),
    agriculture: (massd, residential),
    residential: (massd, agriculture),
    industrial: (massd, atlas),
    atlas: (massd, atlas),
    balderol: (massd,),
}

location = massd

# starting the game using while loop
while True:
    # current location text
    for char in location[1]:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n You can go to these places through SpaceY Mass Driver")

    # providing the location that the user can go to
    # enumerate assigns an index to each item
    for (i, t) in enumerate(transitions[location]):
        print(i + 1, t[0])

    # selecting the location
    choice = int(input("Where do you wanna go? "))

    # assigning new location
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
        print(bcolors.OKBLUE + "Thank you for playing the SpaceY Settlement!")

        # showing the trailer
        video = input("Do you wanna watch the trailer of our Settlement[yes/no]? ")
        if video == "yes":
            url = "http://aryaman.cc/spacey"
            chrome_path = (
                "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            )
            webbrowser.get(chrome_path).open(url)
        else:
            "Hope you come again!"
        break

