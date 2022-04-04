import csv

def pishem(login, name, description, needhum):
    try:
        f = open('input.csv')  
    except IOError as e:
        print('NET')
        with open("input.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(("id","CreatorLogin","Name","Discription","NeedHum","CurrentNum"))
            writer.writerow([1, login, name, description, needhum])
    else:
        with open("input.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow([2, login, name, description, needhum])
pishem("bapa", "pivo", "lubit pivo bara", 4)