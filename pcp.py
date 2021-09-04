import re
import pyperclip
import json
from difflib import get_close_matches 
  

global output
output = ''

with open('dat/pcp.txt', 'r') as file:
    data = file.read()


def clearoutput():  
    global output
    output = ''


def copy_output(this_list, separator=""):
    global output
    for i in this_list:
        output += i + separator
    pyperclip.copy(output)
    clearoutput()


def match_partial(text, *match_items):
    for item in match_items:
        if item in text:
            return True
    return False


def filter_out_partial_match(this_list, match_item):
    clean_list = []
    for i in this_list:
        if (match_partial(i, match_item)):
            continue
        else:
            clean_list.append(i)
    return clean_list


lines = data.splitlines()
lines = filter_out_partial_match(lines, "Closest Location ")


lines2 = []
for i in range(0, len(lines)):
    if (match_partial(lines[i], "(PCP)", "Floor", "Apartment", "Suite", "HT-",
                      "HT4", "Room 307", "Room 1C3", "Room 018", "Room A1-19")):
        lines2[len(lines2)-1] += " " + lines[i]
        continue
    lines2.append(lines[i])

search_string = "View Details"
secondary_search = " of 703"
doctor_info = []
current_string = ""
for i in lines2:
    if secondary_search in i:
        continue
    if search_string not in i:
        current_string = current_string + i + "\n"
    else:
        doctor_info.append(current_string)
        current_string = ""
        continue

for i in range(0, len(doctor_info)):
    doctor_info[i] = doctor_info[i].replace('? ', '')
    # print(doctor_info[i])

copy_output(lines2, "\n")

separator = ' '



class Doctor:
    def __init__(self, name, credentials, practice, address, phone_num):
        self.name = name
        self.credentials = credentials
        self.practice = practice
        self.address = address
        self.phone_num = phone_num

    def to_dict(self):
        return {"name": self.name, "credentials": self.credentials,
                "practice": self.practice, "address": self.address,
                "phone_num": self.phone_num}


doctor_list = []
doctor_lines = doctor_info[0].splitlines()
doctors = []


def doctor_string_to_lines(doctor):
    return doctor.splitlines()


def doctor_lines_to_dict(doctor_lines):
    name = doctor_lines.pop(0)
    credentials = doctor_lines.pop(0)
    phone_num = doctor_lines.pop(-1)
    address = (doctor_lines.pop(-2) + separator + doctor_lines.pop(-1))
    practice = separator.join(doctor_lines)
    doctor_dict = {'name': name, 'credentials': credentials,
                   'phone_num': phone_num, 'address': address,
                   'practice': practice}
    return doctor_dict


def dict_to_Doctor_obj(doctor_dict):
    return Doctor(doctor_dict.get('name'), doctor_dict.get('credentials'),
                  doctor_dict.get('practice'), doctor_dict.get('address'),
                  doctor_dict.get('phone_num'))


def export_json_list(list):
    jsonStr = json.dumps()

doctor_dict_list = []

for doctor in doctor_info:
    doctor_lines = doctor_string_to_lines(doctor)
    doctor_dict = doctor_lines_to_dict(doctor_lines)
    doctor_dict_list.append(doctor_dict) 
    doctors.append(dict_to_Doctor_obj(doctor_dict))

copy_output(doctor_info)

results = [obj.to_dict() for obj in doctors]
jsdata = json.dumps({"doctors": results}, indent=2)
outfile = open('dat\\doctors.json', 'w')
outfile.write(jsdata)
outfile.close()

practices = []


for this_doctor in doctors:
    practices.append(this_doctor.practice)


def remove_list_duplicates(this_list):
    this_list = set(this_list)
    this_list = list(this_list)
    return this_list

def closeMatches (word, this_list):
    return get_close_matches(word, this_list)

def remove_near_duplicates(this_list):
    for i in this_list:
        closeMatches(i, this_list, )
    word = 'appel'
    patterns = ['ape', 'apple', 'peach', 'puppy'] 
    closeMatches(patterns, word) 


# get_close_matches(word, patterns)

practices = remove_list_duplicates(practices)
practices.sort()

for i in practices:
    output += i + "\n"
    print(i)

# pyperclip.copy(output)
'''
jsonStr = json.dumps(doctor1.__dict__)
    print(jsonStr)
'''





'''
TODO:
* First line is always Doctor Name
* Second line is always doctor creds
* Last line is always Phone number
* -2 and -3 are always address
* rest is variable in length but after popping everything out you can just
.join the whole thing with a ' ' separator.
'''
