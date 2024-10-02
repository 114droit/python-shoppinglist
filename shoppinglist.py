# Definieren der Variable shoppinglist
shoppinglist = []

# Funktion zum Hinzufügen eines Artikels
item = input("Welcher Artikel soll der Einkaufsliste hinzugefügt werden?")
def add_item():
    if not item:
        print("Das kann nicht hinzugefügt werden")
    else:
        shoppinglist.append(item)
        print(item, "wurde der Einkaufsliste hinzugefügt")
add_item()

# Funktion zum Anzeigen der Einkaufsliste
def show_shoppinglist():
    if shoppinglist:
        print("Deine Einkaufsliste:")
        for item in shoppinglist:
            print(item)
    else:
        print("Deine Einkaufsliste ist leer")
show_shoppinglist()