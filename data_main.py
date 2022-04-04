import csv

def write_row(login, name, description, need_num):
    try:
        f = open('data.csv')  
    except IOError as e:
        print('NET')
        with open("data.csv", "w") as f:
            writer = csv.writer(f, delimiter=';', lineterminator='\r')
            writer.writerow(("id","CreatorLogin","Name","Discription","NeedNum","CurrentNum"))
            writer.writerow([1, login, name, description, need_num, 1])
    else:
        with open("data.csv", "a") as f:
            writer = csv.writer(f, delimiter=';', lineterminator='\r')
            writer.writerow([2, login, name, description, need_num, 1])