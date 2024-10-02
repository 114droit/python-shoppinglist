# Definieren der Variable shoppinglist
shoppinglist = []

# Funktion zum Hinzufügen eines Artikels
def add_item():
    item = input("Welcher Artikel soll der Einkaufsliste hinzugefügt werden?")
    if not item:
        print("Das kann nicht hinzugefügt werden")
    else:
        shoppinglist.append(item)
        print(item, "wurde der Einkaufsliste hinzugefügt")

# Funktion zum Anzeigen der Einkaufsliste
def show_shoppinglist():
    if shoppinglist:
        print("Deine Einkaufsliste:")
        for item in shoppinglist:
            print(item)
    else:
        print("Deine Einkaufsliste ist leer")

# Main Funktion
while True:
    print("\n")
    print("-----Einkaufsliste-----")
    print("1. Artikel zur Einkaufsliste hinzufügen")
    print("2. Einkaufsliste anzeigen")
    print("3. Programm beenden")
    choice = int(input("Was möchtest du tun?(1/2/3)"))
    if choice == 1:
        add_item()
    elif choice == 2:
        show_shoppinglist()
    elif choice == 3:
        print("Programm wird beendet! Auf Wiedersehen")
        break
    