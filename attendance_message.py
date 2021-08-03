#!/usr/bin/env python
import csv
import datetime
import webbrowser
from time import sleep

TOTAL = 59
ATTENDANCE_CSV = "Attendance.csv"
DEFAULT_SUBMITTER = 'Auhon+5717'

def main():
    dict = csv_to_dict(ATTENDANCE_CSV)
    absentee_list = check_absentees(dict)
    correct_absentee_list(absentee_list)
    absentee_count = len(absentee_list)
    presentee_count = TOTAL - absentee_count
    print_absentee_message(presentee_count, absentee_count, absentee_list)
    print('Here is the absentee list again, so that you may send the contact list to the Attendance Collection Group.')
    print_list(absentee_list)
    input("When you're done submitting the contacts, just hit enter.")
    create_url(absentee_list, absentee_count, presentee_count)
    exit()


def csv_to_dict(attendance_file):
    d = dict()
    with open(attendance_file, "r") as f:
        csvread = csv.reader(f)
        next(csvread)
        for row in csvread:
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


def get_date_weekday():
    today = datetime.date.today()
    today = today.strftime("%d-%m-%Y+%A")
    return today


def print_absentee_message(presentee_count, absentee_count, absentee_list):
    absentee_count = absentee_add_zero(absentee_count)
    print('This is the message you may copy and paste to Whatsapp Attendance Collection Group.')
    print('-----------------------------------------------------------------------------------')
    print()
    print('@ANK Sir')
    print('Daily Attendance:')
    print('Date: ' + get_date())
    print('Form & Section : X Sci-A (BMMS)')
    print('Total Student  : ' + str(TOTAL))
    print('Present        : ' + str(presentee_count))
    print('Absent         : ' + str(absentee_count) + ' (' + ', '.join(absentee_list) + ')')
    print('Name of FM.    : ANK')
    print('\n')
    input("When you're done submitting the contacts, just hit enter.")
    print()


def correct_absentee_list(list):
    print('This is the absent list that was found in the .csv file.')
    print_list(list)
    print()
    user_choice = input('Is this correct?(y/n)  ')
    if user_choice == 'n':
        user_opt = input(
            'Type a and enter to add absentees, and type r and enter to remove absentees: ')
        while user_opt != 'f':
            if user_opt == 'a':
                user_mod_roll = input(
                    'Type in a roll and press enter to add absentee: ')
                if user_mod_roll in list:
                    print(user_mod_roll + ' is already in the list.')
                else:
                    list.append(user_mod_roll)
                    print(user_mod_roll + ' was added to the absentee list.')
                    list.sort()
                    print('Now the new absentee list stands the following:')
                    print_list(list)
            elif user_opt == 'r':
                user_mod_roll = input(
                    'Type in a roll and press enter to remove absentee: ')
                if user_mod_roll not in list:
                    print(user_mod_roll + ' is already not in the list.')
                else:
                    list.remove(user_mod_roll)
                    print(user_mod_roll + ' was removed from absentee list.')
                    print('Now the new absentee list stands the following:')
                    print_list(list)
            user_opt = input(
                'Type a and enter to add more absentees, type r and enter to remove more absentees, and type f to finalize absentee list: ')
    print('\n')


def print_list(list):
    if len(list) == 0:
        print('There are no absentees today.')
    else:
        for roll in list:
            print(roll)


def create_url(absentee_list, absentee_count, presentee_count):
    absentee_count = absentee_add_zero(absentee_count)
    with open('url_format.txt', 'r') as txt:
        url_src = txt.read().splitlines()
        student_list = csv_to_dict('student_list.csv')
        with open('url.txt', mode='a', newline='') as url_file:
            url_file.write(url_src[0])
            submitter = input(
                'Write your nickname and roll (like this: Auhon+5717 with no spaces, if kept blank, the default is ' +DEFAULT_SUBMITTER+ '): ')
            if submitter == '':
                submitter = DEFAULT_SUBMITTER
            url_file.write('&' + url_src[1] + '=' + submitter)
            url_file.write('&' + url_src[2] + '=' + get_date_weekday())
            url_file.write('&' + url_src[3] + '=' + str(TOTAL))
            url_file.write('&' + url_src[4] + '=' + str(presentee_count))
            url_file.write('&' + url_src[5] + '=' + str(absentee_count))
            for roll in student_list:
                if roll in absentee_list:
                    url_file.write('&' + url_src[6] + '=' + student_list[roll])
            if absentee_count == 0:
                url_file.write('&' + url_src[6] + '=None')
            comment = input(
                'Enter Comment (Default is: Nothing unusual today.): ')
            if comment == '':
                comment = 'Nothing unusual today.'
            comment = comment.replace(' ', '+')
            url_file.write('&' + url_src[7] + '=' + comment)
    print('Now we will open your browser and show you the pre-filled Google forms. Just submit it.')
    sleep(1)
    open_url('url.txt')


def open_url(url_file):
    url_file = open(url_file, 'r+')
    url = url_file.read()
    webbrowser.open(url, new=2)
    url_file.truncate(0)
    url_file.close()

def absentee_add_zero(absentee_count):
    if absentee_count >= 0 and absentee_count < 10:
        absentee_count = '0' + str(absentee_count)
    return absentee_count

if __name__ == '__main__':
    main()
