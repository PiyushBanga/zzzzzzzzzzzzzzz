import csv

# function to create login csv file
def create_login_csv():
    with open('login.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Username', 'Password'])
        num_users = int(input("How many users do you want to create? "))
        for i in range(num_users):
            username = input(f"Enter username for user {i+1}: ")
            password = input(f"Enter password for user {i+1}: ")
            writer.writerow([username, password])

def create_questions_csv():
    with open('questions.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Question', 'Difficulty Level'])
        for i in range(1, 4):
            question = input(f"Enter Question {i}: ")
            difficulty = input(f"Enter Difficulty Level for Question {i} (1 - Easy, 2 - Medium, 3 - Hard): ")
            writer.writerow([question, difficulty])

# function to validate user login credentials
def validate_login(username, password):
    with open('login.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Username'] == username and row['Password'] == password:
                return True
        return False

# function to create options csv file
def create_options_csv():
    with open('options.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Question', 'Option A', 'Option B', 'Option C', 'Option D'])
        for i in range(1, 4):
            question = f"Question {i}"
            option_a = input(f"Enter Option A for Question {i}: ")
            option_b = input(f"Enter Option B for Question {i}: ")
            option_c = input(f"Enter Option C for Question {i}: ")
            option_d = input(f"Enter Option D for Question {i}: ")
            correct_option = input(f"Enter the correct option for Question {i} (A, B, C, D): ")
            if correct_option == 'A':
                option_a = f"[{option_a}]"
            elif correct_option == 'B':
                option_b = f"[{option_b}]"
            elif correct_option == 'C':
                option_c = f"[{option_c}]"
            elif correct_option == 'D':
                option_d = f"[{option_d}]"
            writer.writerow([question, option_a, option_b, option_c, option_d])

def read_csv_file(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data


# function to take the exam
# take the exam
def take_exam():
    # read the questions and options csv files
    questions = read_csv_file("questions.csv")
    options = read_csv_file("options.csv")

    # initialize variables to keep track of the score and total questions
    score = 0
    total_questions = len(questions)

    # loop through the questions and ask the user for their answer
    for i in range(total_questions):
        # display the question and options to the user
        print(f"Question {i+1}: {questions[i]}")
        print(f"Options: {options[i]}")
        # prompt the user for their answer
        answer = input("Enter your answer (A/B/C/D): ")
        # check if the answer is correct and increment the score if it is
        if answer.upper() == options[i]['Correct Answer']:
            score += 1

    # calculate the percentage score
    percentage_score = (score / total_questions) * 100
    print(f"Your result: {percentage_score}%")

    # update the result in the credentials file
    with open('credentials.csv', 'r') as file:
        lines = file.readlines()
    with open('credentials.csv', 'w') as file:
        for line in lines:
            # split the line by comma and get the username
            username = line.split(',')[0]
            # check if the username matches the current user
            if username == current_user:
                # update the line with the new percentage score
                line = line.rstrip() + f",{percentage_score}%\n"
            file.write(line)


# main function
def main():
    # create the login csv file
    create_login_csv()
    # prompt the user to enter their login credentials
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        # validate the login credentials
        if validate_login(username, password):
            print("Login successful!")
            # create the options csv file
            create_options_csv()
            # take the exam
            take_exam()
            break
        else:
            # show error message for invalid username or password
            print("Invalid username or password. Please try again.")

    # update the result in the credentials file
    with open('credentials.csv', 'r') as file:
        lines = file.readlines()
    with open('credentials.csv', 'w') as file:
        for line in lines:
            # split the line by comma and get the username
            username_in_file = line.split(',')[0]
            # check if the username matches the current user
            if username_in_file == username:
                # get the student's percentage score
                percentage_score = get_percentage_score()
                # update the line with the new percentage score
                line = line.rstrip() + f",{percentage_score}%\n"
            file.write(line)
