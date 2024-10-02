# Definieren der Variable shoppinglist
shoppinglist = []

# Funktion zum Hinzufügen eines Artikels
item = input("Welcher Artikel soll der Einkaufsliste hinzugefügt werden?")
def add_item():
    shoppinglist.append(item)
    print(item, "wurde der Einkaufsliste hinzugefügt")
add_item()

# Funktion zum Anzeigen der Einkaufsliste
def show_shoppinglist():
    if not shoppinglist:
        print("Deine Einkaufsliste leer")
    else:
        print(f"Deine Einkaufsliste beinhaltet: {shoppinglist}!")
show_shoppinglist()