# This is the main program
import lottery_program
import lottery_db


if __name__ == "__main__":
    print("\t","| Play            ----->  'p' |")
    print("\t","| History         ----->  'h' |")
    print("\t","| Seek by name    ----->  'n' |")
    print("\t","| Lottery history ----->  'l' |")
    user_choice = input("Enter the choice :").lower()
    if user_choice == "play".lower():
        print("you are now playing the game!!")
        lottery_program.userDetails()
        lottery_program.userNumber()
        lottery_program.lotteryNumber()
        lottery_program.finalResult()
        lottery_program.matchesCheck()


    if user_choice == "h".lower():
        print("This is the history.")
        lottery_program.gameHistory()

    if user_choice == "n".lower():
        lottery_db.userCheck()

    if user_choice == "l".lower():
        lottery_db.html_view()


