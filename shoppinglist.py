# Definieren der Variable shoppinglist
shoppinglist = ["Apfel","Banane","Kirsche"]

# Funktion add-item

item = input("Welcher Artikel soll der Einkaufsliste hinzugefügt werden?")
def add_item():
    shoppinglist.append(item)
    print(item, "wurde der Einkaufsliste hinzugefügt")
add_item()