name = input("enter your name: ")
game_answere = input("hi "+ name +",welcome to adventure game would u like to play: ")

if game_answere == "yes":
    print("ok then lets start!! ")

    direction_answere = input("Its a dirty road u have come to an end you should have to go Left or Right which way will u go? ")

    if direction_answere == "left":
        swim_or_walk = input("You have come across a river,Would u rather swim across the river or walk around the river ")

        if swim_or_walk == "swim":
            print("oops,u were eaten by a alligator")

        elif swim_or_walk == "walk":
            print("you have walked for a long time, u ran out of water and food and died")

        else:
            print("not a valid option")


    elif direction_answere == "right":
        forward_or_back = input("vow there is bridge infornt of u, it looks vobly,Do u want to move forward or return back ")

        if forward_or_back == "back":
            print("while ur going back on a bridge u fell down and died")

        elif forward_or_back == "forward":
            help_or_not = input("you have seen a old man struggling to cross a road, he asked u for help, DO u want to help him or not ")

            if help_or_not =="help":
                print("the old man appericiated your work and rewarded a daimond")

            elif help_or_not == "no" or "not":
                print("he cursed u to be dead and ur dead")

            else:
                print("not a valid option")

        else:
            print("not a valid option")

    else:
        print("not a valid option")

else:
    print("bye,hope u will play with us next time")
