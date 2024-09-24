# ======================================
# PROGRAM : Covid 19 Contact Tracing App
# ======================================

def isMet(name1, name2):
    for data in all_data:
        if name1 in data and name2 in data:
            return True
    return False

def getPartner(name, pair):
    for x in pair:
        if x!=name and x.isalpha():
            return x
    return False

def insertData(pat_name, cont_name, cont_time):
    global all_data
    if isMet(pat_name, cont_name):
        return False
    all_data += ((pat_name, cont_name, cont_time), )
    return True

def getConts(name):
    global cont_tup
    temp = tuple()
    for data in all_data:
        if name in data:
            contact = getPartner(name, data)

            if contact not in cont_tup:
                temp += (contact,)

    cont_tup += temp
    if len(temp)==0:
        return
    for x in temp:
        getConts(x)
        
all_data = tuple()

print("This is a contact tracing app.\nEnter requested information.\nEnd by giving your name as 'end'.")

while True:
    first_inp = input('\nYour name: ')

    if first_inp == 'end':
        break
    
    patient_name = first_inp.strip()
    contact_name = input("Contact's name: ").strip()
    contact_time = int(input('Time spent with contact: ').strip())
    
    print(f'{patient_name} has spent {contact_time} minutes in close proximity to {contact_name}.')
    insertData(patient_name, contact_name, contact_time)

to_trace_name = input('\nEnter name of person to trace: ').strip()
cont_tup = tuple()
getConts(to_trace_name)

print(f'\nFollowing persons who are in contact cluster of {to_trace_name} must self-isolate')

for name in cont_tup:
    print(name)