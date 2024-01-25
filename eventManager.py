#### IMPORTS ####

import event_manager as EM

#### PART 1 ####
# Filters a file of students' subscription to specific event:
#   orig_file_path: The path to the unfiltered subscription file
#   filtered_file_path: The path to the new filtered file
def fileCorrect(orig_file_path: str, filtered_file_path: str):
    students = fileFilterer(orig_file_path)
    new_str = ", "
    d = open(filtered_file_path, 'w')
    for i,e in enumerate(students[0]):
        d.write(str(students[0][i]) + new_str + students[1][i] + new_str + str(students[2][i]) + new_str + str(students[3][i]) + new_str + str(students[4][i]))
        d.write("\n")
    d.close()



def fileFilterer(orig_file_path: str):
    s = open(orig_file_path, 'r')
    id = []
    name = []
    age = []
    year_of_birth = []
    semester = []
    students = [id, name, age, year_of_birth, semester]
    for line in s:
        new_list = line.split(',')       
        id_filtered = checkId(new_list[0])
        if id_filtered == 0 :
            continue
        name_filtered = checkName(new_list[1])
        if name_filtered == 'invalid_name':
            continue
        new_age = int(new_list[2])
        if(new_age > 120 or new_age < 16 ):
            continue
        new_year_of_birth = int(new_list[3])
        if not(new_year_of_birth == 2020 - new_age):
            continue
        new_semester = int(new_list[4])
        if new_semester < 1 :
            continue
        if(len(id) == 0 or id_filtered <= id[0]):
            if not(len(id) == 0) and id_filtered == id[0]:
                name[0] = name_filtered
                age[0] = new_age
                year_of_birth[0] = new_year_of_birth
                semester[0] = new_semester
            else:
                id.insert(0, id_filtered)
                name.insert(0, name_filtered)
                age.insert(0, new_age)
                year_of_birth.insert(0, new_year_of_birth)
                semester.insert(0, new_semester)
        else:
            for i,e in enumerate(id):
                if id_filtered >= e :
                    if not(i == len(id)-1):
                        if id_filtered >= id[i+1] :
                            continue
                    if id_filtered == id[i]:
                        name[i] = name_filtered
                        age[i] = new_age
                        year_of_birth[i] = new_year_of_birth
                        semester[i] = new_semester
                    else:
                        id.insert(i+1, id_filtered)
                        name.insert(i+1, name_filtered)
                        age.insert(i+1, new_age)
                        year_of_birth.insert(i+1, new_year_of_birth)
                        semester.insert(i+1, new_semester)
                    break
    return students




def  checkId(id : str):
    valid_numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',' ')
    str = ""
    new_list = []
    for e in id:              
        if not(e in valid_numbers):
            return 0 
        new_list.append(e)
    while (new_list[0] == ' ' or new_list[-1] == ' '):
        if(new_list[0] == ' '):
            del new_list[0]
        if(new_list[-1] == ' '):
            del new_list[-1]
    if (new_list[0] == '0' or not(len(new_list) == 8)):
        return 0
    return int(str.join(new_list))


def checkName(name : str):
    Alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ')
    str = ""
    new_list = []
    for i,e in enumerate(name):
        if not(e in Alphabet):
            return 'invalid_name'
        if (i == len(name)-1):
            new_list.append(e)
        elif(not(e == ' ') or (e == ' ' and not(name[i] == name[i+1]))):     
            new_list.append(e)
    if(new_list[0] == ' '):
        del new_list[0]
    if(new_list[len(new_list)-1] == ' '):
        del new_list[len(new_list)-1]
    return str.join(new_list)


# Writes the names of the K youngest students which subscribed 
# to the event correctly.
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: file path of the output file
def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    if(k <= 0):
        return -1 
    fileCorrect(in_file_path, out_file_path)
    s = open(out_file_path,'r')
    id = []
    age = []
    name = []
    new_age = []
    new_name = []
    new_id = []
    for line in s:
        new_list = line.split(', ')
        id.append(int(new_list[0]))
        name.append(new_list[1])
        age.append(int(new_list[2]))
    while(k > 0 and len(age) > 0):
        min_age = min(age)
        min_age_index = age.index(min_age)
        if not(min_age in new_age):
            new_age.append(min_age)
            new_name.append(name[min_age_index])
            new_id.append(id[min_age_index])
        else:
            for i,e in enumerate(new_age):
                if (e == min_age and (id[min_age_index] < new_id[i])):
                    new_age.insert(i,min_age)
                    new_name.insert(i,name[min_age_index])
                    new_id.insert(i,id[min_age_index])
                elif (e == min_age and (id[min_age_index] > new_id[i])):
                    if not(i == len(new_age)-1):
                        if new_age[i+1] == e :
                            continue
                    new_age.insert(i+1,min_age)
                    new_name.insert(i+1,name[min_age_index]) 
                    new_id.insert(i+1,id[min_age_index])
        del age[min_age_index]
        del name[min_age_index]
        del id[min_age_index]
        k -= 1
    s.close()
    d = open(out_file_path,'w')
    for e in new_name:
        d.write(e)
        d.write("\n")
    d.close()    
    return len(new_age)


# Calculates the avg age for a given semester
#   in_file_path: The path to the unfiltered subscription file
#   retuns the avg, else error codes defined.
def correctAgeAvg(in_file_path: str, semester: int) -> float:
    if not(type(semester) == int) or semester < 1:
        return -1
    students = fileFilterer(in_file_path)
    ages = students[2]
    all_semesters = students[4]
    sum = 0
    num_of_students = 0
    for i,e in enumerate(all_semesters):
        if e == semester:
            sum += ages[i]
            num_of_students += 1
    if num_of_students == 0:
        return 0
    return sum/num_of_students


#### PART 2 ####
# Use SWIG :)
# print the events in the list "events" using the functions from hw1
#   events: list of dictionaries
#   file_path: file path of the output file
def printEventsList(events :list,file_path :str): #em, event_names: list, event_id_list: list, day: int, month: int, year: int):
    most_recent_event = events[0]["date"]
    for e in events:
        if EM.dateCompare(most_recent_event, e["date"]) > 0 :
            most_recent_event = e["date"]
    em = EM.createEventManager(most_recent_event)
    for e in events:
        EM.emAddEventByDate(em, e["name"], e["date"], e["id"])
    EM.emPrintAllEvents(em, file_path)
    return em

    

    
    
def testPrintEventsList(file_path :str):
    events_lists=[{"name":"New Year's Eve","id":1,"date": EM.dateCreate(30, 12, 2020)},\
                    {"name" : "annual Rock & Metal party","id":2,"date":  EM.dateCreate(21, 4, 2021)}, \
                                 {"name" : "Improv","id":3,"date": EM.dateCreate(13, 3, 2021)}, \
                                     {"name" : "Student Festival","id":4,"date": EM.dateCreate(13, 5, 2021)},    ]
    em = printEventsList(events_lists,file_path)
    for event in events_lists:
        EM.dateDestroy(event["date"])
    EM.destroyEventManager(em)

#### Main #### 
# feel free to add more tests and change that section. 
# sys.argv - list of the arguments passed to the python script
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        testPrintEventsList(sys.argv[1])

