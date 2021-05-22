import csv, datetime

TOTAL = 59

def main():
    dict = csv_to_dict("Attendence.csv")
    absentee_list = check_absentees(dict)
    correct_absentee_list(absentee_list)
    absentee_count = len(absentee_list)
    presentee_count = TOTAL - absentee_count
    print_absentee_message(presentee_count, absentee_count)
    


def csv_to_dict(attendance_file):
    d = dict()
    with open(attendance_file, "r") as f:
        csvread = csv.reader(f)
        for row in csvread:
            if row[0] != 'Student Roll':
                key = row[0]
                val = row[1]
                d[key] = val
    return d


def check_absentees(dict):
    list = []
    for key in dict:
        if dict[key] == '':
            list.append(key)
    return list

    
def get_date():
    today = datetime.date.today()
    today = today.strftime("%d-%m-%Y")
    return today

def print_absentee_message(presentee_count, absentee_count):
    print('This is the message you may copy and paste to Whatsapp Attendance Collection Group.')
    print('-----------------------------------------------------------------------------------')
    print('@ANK Sir') 
    print('Daily Attendance:')
    print('Date: ' + get_date())
    print('Form & Section : ')
    print('X Sci-A (BMMS)')
    print('Total Student : ' + str(TOTAL))
    print('Present       : ' + str(presentee_count))
    print('Absent        : ' + str(absentee_count))
    print('Name of FM.   : ANK')
    print('\n\n')

def correct_absentee_list(list):
    print('This is the absent list that was found in the .csv file.')
    print_list(list)
    print()
    user_choice = input('Is this correct?(y/n)  ')
    if user_choice == 'n':
        user_opt = input('Type a and enter to add absentees, and type r and enter to remove absentees: ')
        while user_opt != 'f':
            if user_opt == 'a':
                user_mod_roll = input('Type in a roll and press enter to add absentee: ')
                if user_mod_roll in list:
                    print(user_mod_roll + ' is already in the list.')
                else:
                    list.append(user_mod_roll)
                    print(user_mod_roll + ' was added to the absentee list.')
                    list.sort()
                    print('Now the new absentee list stands the following:')
                    print_list(list)
            elif user_opt == 'r':
                user_mod_roll = input('Type in a roll and press enter to remove absentee: ')
                if user_mod_roll not in list:
                    print(user_mod_roll + ' is already not in the list.')
                else:
                    list.remove(user_mod_roll)
                    print(user_mod_roll + ' was removed from absentee list.')
                    print('Now the new absentee list stands the following:')
                    print_list(list)
            user_opt = input('Type a and enter to add more absentees, type r and enter to remove more absentees, and type f to finalize absentee list: ')

            
        

def print_list(list):
    if len(list) == 0:
        print('There are no absentees today.')
    else:
        for roll in list:
            print(roll)

if __name__=='__main__':
    main()