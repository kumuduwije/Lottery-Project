# Lottery program
# import packages
import random
import lottery_db
# Create variables

number_1 = 0
number_2 = 0
number_3 = 0
number_4 = 0
number_5 = 0

# lottery numbers

lottery_num_1 = 0
lottery_num_2 = 0
lottery_num_3 = 0
lottery_num_4 = 0
lottery_num_5 = 0
# Create a empty list to store user's numbers
user_num_list = []
# Create a empty list to store lottery numbers
lottery_num_list = []
# store user details
user = {}
# track the matches count
match_count = 0
user_id = 0
user_name = ""
def userDetails():
    global user, user_id, user_name
    import random
    while True:
        user_name = input("Enter your name :").capitalize()
        if user_name != "" or user_name != user_name.isdigit():
            print("Saved!!")
            user_id = random.randrange(101,599)
            user = {'username': user_name, 'userID': user_id}
            # detail = open("detail-list.txt","a")
            # detail.write(str(user))
            # detail.write(str("\n"))
            # detail.close()
            break
        else:
            print("Invalid response.")


def userNumber():
    '''This is for user inputs'''
    # Get the 1th input
    global number_1, number_2, number_3, number_4, number_5,user_num_list
    while True:

        number_1 = int(input("Insert number 1 :"))
        if 1 <= number_1 <= 50:
            if 1 <= number_1 <= 9:
                int(0) + number_1
            user_num_list.append(number_1)
            break

        else:
            print("Number is out of range, enter number between 1 to 50 ")
            continue
    # Get the 2th input
    while True:
        number_2 = int(input("Insert number 2 :"))
        if 1 <= number_2 <= 50:
            if 1 <= number_2 <= 9:
                int(0) + number_2
            user_num_list.append(number_2)
            break

        else:
            print("Number is out of range, enter number between 1 to 50 ")
            continue
    # Get the 3th input
    while True:
        number_3 = int(input("Insert number 3 :"))
        if 1 <= number_3 <= 50:
            if 1 <= number_3 <= 9:
                int(0) + number_3
            user_num_list.append(number_3)
            break

        else:
            print("Number is out of range, enter number between 1 to 50 ")
            continue

    # Get the 4th input
    while True:
        number_4 = int(input("Insert number 4 :"))
        if 1 <= number_4 <= 50:
            if 1 <= number_4 <= 9:
                int(0) + number_4
            user_num_list.append(number_4)
            break

        else:
            print("Number is out of range, enter number between 1 to 50 ")
            continue

    # Get the 5th input

    while True:
        number_5 = int(input("Insert number 5 :"))
        if 1 <= number_5 <= 50:
            if 1 <= number_5 <= 9:
                int(0) + number_5
            user_num_list.append(number_5)
            break

        else:
            print("Number is out of range, enter number between 1 to 50 ")
            continue

    return user_num_list

# random lottery number return


def lotteryNumber():
    global lottery_num_list,lottery_num_1,lottery_num_2,lottery_num_3,lottery_num_4,lottery_num_5
    lottery_num_1 = random.randrange(1,51)
    lottery_num_list.append(lottery_num_1)

    lottery_num_2 = random.randrange(1,51)
    lottery_num_list.append(lottery_num_2)

    lottery_num_3 = random.randrange(1,51)
    lottery_num_list.append(lottery_num_3)

    lottery_num_4 = random.randrange(1,51)
    lottery_num_list.append(lottery_num_4)

    lottery_num_5 = random.randrange(1,51)
    lottery_num_list.append(lottery_num_5)

    return lottery_num_list

# userNumber()
#  Lottery numbers
# lotteryNumber()



# Check the matches
def matchesCheck():
    """Check user's numbers and generated numbers."""
    match_count = 0
    if user_num_list[0] == lottery_num_list[0]:
        match_count  += 1
    elif user_num_list[1] == lottery_num_list[1]:
        match_count  += 1
    elif user_num_list[2] == lottery_num_list[2]:
        match_count  += 1
    elif user_num_list[3] == lottery_num_list[3]:
        match_count  += 1
    elif user_num_list[4] == lottery_num_list[4]:
        match_count  += 1

    print("You have", match_count , "matches.")
    return match_count

# Showing the user's numbers
def finalResult():
    """Write the detail.txt file to store user details"""
    global user, user_id,user_name, lottery_num_list,user_num_list,match_count
    # Update the 'user dictionary' dictionary
    user["Numbers"] = user_num_list
    user["Lottery-Numbers"] = lottery_num_list
    user["win-matches"] = {'rounds win': match_count}
    detail = open("detail-list.txt","a")
    detail.write(str(user))
    detail.write(str("\n"))
    detail.close()
    # Inserting data into table
    lottery_db.userTable(str(user_id),str(user_name),str(user_num_list),str(lottery_num_list),str(match_count))

    print("User Matches : ", number_1, number_2 , number_3 , number_4 , number_5)
    print("Lott Numbers : ", lottery_num_1 , lottery_num_2 , lottery_num_3, lottery_num_4, lottery_num_5)

# matchesCheck()

def gameHistory():
    history = open("detail-list.txt", "r")
    with history:
        for item in history:
            print(item)



