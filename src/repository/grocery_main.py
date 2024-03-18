
import csv


# data = [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]
#def write_list_of_dicts_to_csv(filename, data):
    #with open(filename, 'w') as f:
       # writer = csv.DictWriter(f, fieldnames=data[0].keys())
        #writer.writeheader()
       # writer.writerows(data)


def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def main(filename):
    data = read_csv_to_dict(filename)
    for row in data:
        print(row)


def read_csv_to_dict(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def write_dicts_to_csv(file_path, data):
    if not data:
        return
    
    fieldnames = data[0].keys()
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def append_dict_to_csv(file_path, new_item):
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=new_item.keys())
        writer.writerow(new_item)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('sample_grocery.csv')
