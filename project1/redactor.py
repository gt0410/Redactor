#
#
#
import sys
import glob
import main
import numpy


a_list = []
a_list = sys.argv
input_path = []
output_path = ''
concept = ''
flags = []
stats_list = []
n = 'names'
gen = 'genders'
dt = 'dates'
add = 'addresses'
ph = 'phones'
print(len(a_list))
del a_list[0]

# For loop to save all the list of possible actions to be done
for i in range(len(a_list)):
#    print(a_list[i])
    if a_list[i] == '--input':
        input_path.append(a_list[i+1])
    
    elif a_list[i] == '--output':
        output_path = a_list[i+1]
    
    elif a_list[i] == '--concept':
        concept = a_list[i+1]
    
    elif a_list[i] == '--stats':
        stats_list.append(a_list[i+1])

    elif a_list[i].startswith('--'):
        flags.append(a_list[i][2:])

for paths in input_path:
    files = glob.glob(paths)
    
    for f in files:
        my_file = open(f, encoding = "ISO-8859-1")
        data = my_file.read()
        print(f)
        if n in flags:
            data, names_list = main.names(data)
        if gen in flags:
            data, genders_list = main.genders(data)
        if dt in flags:
            data,dates = main.dates(data)
        if add in flags:
            data, address_list = main.addresses(data)
        if ph in flags:
            data, phones_list = main.phones(data)
        
        data, concept_list, concept_count = main.concept(data, concept)
        status = main.stats(names_list, dates,address_list, phones_list, genders_list, concept_list, concept_count, stats_list, f)

        #print(status)
        f_name = output_path + f
        f_name = f_name.replace('.txt', '.redacted')
        with open(f_name, 'w', encoding = "utf-8")as file:
            file.write(data)
            file.close()

#print(flags)


        
