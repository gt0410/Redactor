#
#
#
import sys
import glob
a_list = []
a_list = sys.argv
input_path = []
output_path = ''
concept = ''
flags = []
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
        stats = a_list[i+1]

    elif a_list[i].startswith('--'):
        flags.append(a_list[i][2:])


for paths in input_path:
    files = glob.glob(paths)
    
    for f in files:
        my_file = open(f, encoding = "ISO-8859-1")
        data = my_file.read()

        print(data[:25])


print(flags)


        
