import csv, datetime

TOTAL = 59

def main():
    dict = csv_to_dict("Attendence.csv")
    absentee_list = check_absentees(dict)
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
    print('@ANK Sir') 
    print('Daily Attendance:')
    print('Date: ' + get_date())
    print('Form & Section : ')
    print('X Sci-A (BMMS)')
    print('Total Student : ' + str(TOTAL))
    print('Present       : ' + str(presentee_count))
    print('Absent        : ' + str(absentee_count))
    print('Name of FM. D  : ANK')


if __name__=='__main__':
    main()