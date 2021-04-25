def choice_one():

        races_file = open("Races.txt", "r")
        num = 0
        results_list = []
        for line in races_file:
            num = num + 1
            line = line.strip() #to get rid of \n
            print("Please Choose " + str(num) + "." + " " + line)
            results_list.append(line)

        selection = int(input("Choice: "))
        lower_cased = results_list[selection - 1].lower()
        race_file = open(str(lower_cased + ".txt"), "r")
        time_list, code_list = [], []
        for line in race_file:
            line = line.strip()
            line = line.split(",")
            code = (line[0])
            seconds = int(line[1])

            minutes = seconds // 60
            minutes_seconds = seconds % 60
            print(line[0], str(minutes) + " Minutes " + str(minutes_seconds) + " Seconds")
            time_list.append(seconds)
            code_list.append(code)




        time_value = min(time_list)
        index = time_list.index(time_value)
        print(str(code_list[index]) + " Won the race ")

        races_file.close()
        race_file.close()

        # Q: is looping in this menu okay or do we not have a loop and just go to the main menu after first input
        # I put it this way, user will stay in sub menu untill they wan\t to quit



def choice_two():


    venue_name = input("Enter Venue to be created ")
    races_file = open("Races.txt", "a")
    new_line = "\n" + venue_name
    races_file.write(new_line)
    races_file.close()

    runner_list = open("Runners.txt", "r")
    race_list = open(venue_name + ".txt", "a")
    for item in runner_list:
        #To remove the \n
        item = item.strip()
        race_time = int(input(f"For {item}, " + "What time did this racer complete at(in seconds) "))
        if race_time == 0:
            print(item + " Did not run")
            continue
        item = item.split(",")
        record = (item[1] + "," + str(race_time) + "\n")
        race_list.write(record)
        print(record)
    race_list.close()
    runner_list.close()

def choice_three():
    print("You have selected to view all racers by County\n-----------")


    runners_list = open("Runners.txt", "r")
    listItems = runners_list.read().splitlines()
    cork_runners = []
    kerry_runners = []
    for line in listItems:
        cut = (line.split(",")[1])
        variable = (cut.split("-")[0])

        #for i in variable: # KY   ['C','K']
        if variable[0:] == "CK":
            cork_runners.append(line)
            print(cork_runners)
        if variable[0:] == "KY":
            kerry_runners.append(line)
            print(kerry_runners)
    print("Cork Runners\n--------")
    for i in cork_runners:
        x = i.split(",")
        print(x[0] + " " + x[1])
    print(" ")
    print("Kerry Runners\n--------")
    for i in kerry_runners:
        x = i.split(",")
        print(x[0] + " " + x[1])


def choice_four():

        venue = "Venue"
        winner = "Winner"
        separator = "=" * 20
        print(f"{venue:<15} {winner:>7} \n {separator}")
        x = open("races.txt", "r")
        venue_list = []
        for line in x:
            line = line.strip()  # to get rid of \n

            venue_list.append(line)
            # print(venue_list[-1])
            line.lower()
            y = open(line + ".txt", "r")
            time_list = []
            code_list = []
            for line in y:
                # print(line)
                split = line.split(",")[1]  # [code, 10]
                split = split.strip()  # to get rid of \n
                code = line.split(",")[0]
                code_list.append(code)

                # print(split)
                time_list.append(int(split))
            time_value = min(time_list)
            # print(time_value)
            index = time_list.index(time_value)
            print(f"{venue_list[-1]:<15}  {code_list[index]:>5}")
            y.close()

        x.close()

def choice_five():
    people = open("runners.txt", "r")
    # print(people)
    num = 0
    people_list = []
    for person_line in people:
        split = person_line.split(",")[0]
        num = num + 1
        print(str(num) + ": "+ split)
        person_line = person_line.strip()  # to get rid of \n
        people_list.append(person_line)
    # print(people_list)
    selection = int(input("Which Runner: "))
    list_select = people_list[selection - 1]
    print(list_select)
    print("---------------------------------------------------")
    code = list_select.split(",")[1]
    # print(code)



    races_file = open("Races.txt", "r")
    for venue_line in races_file:
        venue_line = venue_line.strip()  # to get rid of \n
        race_file = open(str(venue_line.lower() + ".txt"), "r")

        timelist = []

        runner_in_this_place = False
        for line in race_file:
            line = line.strip()

            player_time = line.split(",")[1]
            timelist.append(int(player_time))

            new_code = line.split(",")[0]




            if new_code == code:
                runner_in_this_place = True #person runs in this place

                time = line.split(",")[1]

                seconds = int(time)
                minutes = seconds // 60
                minutes_seconds = seconds % 60

        if runner_in_this_place:
            # to check out if this person is running here
            timelist.sort()
            # print(timelist)
            index1 = timelist.index(seconds)
            actual_position = index1 + 1
            print(f"{venue_line:<15}    {minutes:<2} Minutes {minutes_seconds:<2} Seconds ({actual_position} out of {len(timelist)})")


def choice_six():

    venue = "Venue"
    winner = "Winner"
    separator = "=" * 20
    print(f"{venue:<15} {winner:>7} \n {separator}")
    print("The following competitors have won atleast one race\n--------------------------")
    x = open("races.txt", "r")
    venue_list = []
    names = open("Runners.txt", "r")
    runner_name_list = []
    runner_code_list = []
    for i in names:
        # print(i)
        name = i.split(",")[0]

        code = i.split(",")[1]
        code = code.strip()
        # print(name)
        runner_name_list.append(name)
        runner_code_list.append(code)
    # print(runner_name_list)
    # print(runner_code_list)

    for line in x:
        line = line.strip()  # to get rid of \n

        venue_list.append(line)
        # print(venue_list[-1])
        line.lower()
        y = open(line + ".txt", "r")
        time_list = []
        winner_code_list = []
        for line in y:
            # print(line)
            split = line.split(",")[1]  # [code, 10] 10\n
            split = split.strip()  # to get rid of \n
            code = line.split(",")[0]
            winner_code_list.append(code)

            # print(split)
            time_list.append(int(split))
        # print(code_list)
        time_value = min(time_list)
        # print(time_value)
        winner_index = time_list.index(time_value)
        # print(f"{winner_code_list[winner_index]:>5}")
        code_of_winner = winner_code_list[winner_index]
        index3 = runner_code_list.index(code_of_winner)
        name_of_racer = (runner_name_list[index3])
        print(f"{name_of_racer} ({code_of_winner})")
        y.close()



def show_menu():
    while True:
        print("Menu for the races\n--------------")
        print("1. Show Results\n2. Add results\n3.Show competitors by county\n4.Show The winner of each race\n5.Show race times for one competitor\n6.Show all competitors who won a race\n7.Quit")
        #to get integer from user
        choice = int(input("Select your choice: "))
        if choice == 1:
            choice_one()
        elif choice == 2:
            choice_two()
        elif choice == 3:
            choice_three()
        elif choice == 4:
            choice_four()
        elif choice == 5:
            choice_five()
        elif choice == 6:
            choice_six()
        elif choice == 7:
            break

        #if number is 7 break
        #if 1, load data





def main():
    print("Hello")
    show_menu()

main()
