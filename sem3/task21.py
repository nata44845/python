# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


dict_1= [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}] 

set_1=set()

for mini_dict in dict_1:
    set_1 = set_1.union(set(mini_dict.values()))

print(set_1)