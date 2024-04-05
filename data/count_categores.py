counter = 0
bad_lines = 0
all_counter = 0
sum = 0
s = []

with open('TenderHack_msk.csv') as file:
    for line in file:
        t = line.split(';')
        try:
            s += [int(t[3])]
            sum += len(t[1])
            counter += 1
        except ValueError:
            # print('! Exception ValueError -', counter, line)
            bad_lines += 1
        except IndexError:
            # print('! Exception IndexError -', counter, line)
            bad_lines += 1
        all_counter += 1

res = len(set(s))

print('Average length of main string:', sum / counter)
print('Number of categories:', res)
print('Bad lines:', bad_lines)
print('Number of all lines:', all_counter)
print('% of good lines: ' + str((all_counter - bad_lines) / all_counter * 100) + ' %')
