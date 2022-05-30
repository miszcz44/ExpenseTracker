import json

def Show_expenses():
    Categories_sorted = sorted(Categories[0].items(), key=lambda x: x[1], reverse=True)
    for key, value in Categories_sorted:
        print(key + ": " + str(value))

def Add_expense(user_choice2):
    print("Wydatek:")
    expense = float(input())
    category = "fdas"
    print(user_choice2)
    if(int(user_choice2) == 1): category = "jedzenie"
    elif(int(user_choice2) == 2): category = "transport"
    elif(int(user_choice2) == 3): category = "alkohol"
    elif(int(user_choice2) == 4): category = "rozrywka"
    elif(int(user_choice2) == 5): category = "edukacja"
    elif(int(user_choice2) == 6): category = "inne"
    Categories[0][category] += expense
    with open("Categories.json", "w") as json_file:
        json.dump(Categories, json_file)

second_menu_possibilities = [1, 2, 3, 4, 5, 6]

with open("Categories.json", "r") as json_file:
    Categories = json.load(json_file)






while True:
    print("1.Dodaj wydatek\n2.Wyświetl wydatki według kategorii\n3.Wyjdź")
    user_choice = input()
    if(int(user_choice) == 3):
        break
    elif(int(user_choice) == 1):
        while(True):
            print("1.Jedzenie\n2.Transport\n3.Alkohol\n4.Rozrywka\n5.Edukacja\n6.Inne\n7.Wróć")
            user_choice2 = input()
            if(int(user_choice2) == 7):
                break
            elif(int(user_choice2) in second_menu_possibilities):
                Add_expense(user_choice2)
            else:
                print("Błąd")
                continue
    elif(int(user_choice) == 2):
        Show_expenses()
    else:
        print("Błąd")
        continue

