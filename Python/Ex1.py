# Write a program in Python which:
# - accepts as an input json file,
# - parses the the file, calculates and prints:
#     - operation, which is taking the longest when summed from all entries,
#     - list of softwares from the one taking the longest, to the one running the shortest.
        
# What kind of error handling would you implement? What should be done about invalid entries?
import json


def read_json(path):
    if not path.endswith('.json'):
        raise ValueError('Invalid file type')
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def preprocess_file(data):
    operations = []

    for entry in data:
        try:
            operation = entry['operation']
            software = entry['software']
            time = entry['length']

            if type(operation) is not str or type(software) is not str or type(time) is not int:
                raise TypeError
            
            if time < 0:
                raise ValueError

            operations.append((operation, software, time))
            
        except TypeError:
            print(f'Invalid entry: {entry}')
            continue

        except ValueError:
            print(f'Incorrect time: {entry}')
            continue

        except KeyError:
            print(f'Invalid entry: {entry}')
            continue

    return operations

if __name__ == '__main__':
    data = read_json('p_ex_1_runtime_parsing.json')
    clean_data = preprocess_file(data)

    operations = {}
    for operation, software, time in clean_data:
        if operation not in operations:
            operations[operation] = [(software, time)]
        else:
            operations[operation].append((software, time))

    for operation, software_times in operations.items():
        operations[operation] = sorted(software_times, key=lambda x: x[1], reverse=True)

    longest_operation = max(operations, key=lambda x: sum([y[1] for y in operations[x]]))
    print(f'\nLongest operation: {longest_operation}')
    print(f'Time: {sum([y[1] for y in operations[longest_operation]])}')

    software_times = {}
    for operation, software_time in operations.items():
        for software, time in software_time:
            if software not in software_times:
                software_times[software] = time
            else:
                software_times[software] += time

    print('\nSoftware times:')
    for software, time in sorted(software_times.items(), key=lambda x: x[1], reverse=True):
        print(f'{software}: {time}')


    
