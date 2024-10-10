import sqlite3

# Verbindung zu sqlite-DB (Falls keine db vorhanden, wird diese erstellt)
conn = sqlite3.connect('shoppinglist.db')

# Erstellen eines cursor (Zeiger?) um sql-Befehl durchzuführen
cursor = conn.cursor()

# Erstellen von Tabellen in shoppinglist.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS groceries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    amount INTEGER NOT NULL,
    price FLOAT NOT NULL
    );
''')

# Funktion zum Hinzufügen eines Artikels (CREATE)
def add_item(name, amount, price):
    cursor.execute('''
    INSERT INTO groceries (name, amount, price) VALUES (?, ?, ?)
    ''', (name, amount, price))
    conn.commit()
    print(f"{name} wurde hinzugefügt.\n")

# Funktion zum Anzeigen der Einkaufsliste (READ)
def show_items():
    cursor.execute('SELECT id, name, amount, price FROM groceries')
    items = cursor.fetchall()
    if not items:
        print("\nDeine Einkaufsliste ist leer\n")
    else:
        for id, name, amount, price in items:
            print(f"Artikel: {name}, Menge: {amount}, Preis: {price}, id: {id}")

# Funktion zum aktualisieren der Artikel der Einkaufsliste (UPDATE)
def update_item(id, name, amount, price):
    cursor.execute('''
    UPDATE groceries SET name = ?, amount = ?, price = ?
    WHERE id = ?
    ''', (name, amount, price, id))
    conn.commit()
    print(f"Der Artikel mit der id {id} wurde aktualisiert.\n")

# Funktion zum löschen eines Atikels (DELETE)
def delete_item(id):
    cursor.execute('''
    DELETE FROM groceries WHERE id = ?
    ''', (id))
    conn.commit()
    print(f"Der Artikel mit der id {id} wurde gelöscht.\n")

# Main Funktion
def main():
    while True:
        print("\n-----Einkaufsliste-----\n")
        print("1. Artikel hinzufügen")
        print("2. Artikel bearbeiten")
        print("3. Artikel löschen")
        print("4. Einkaufsliste anzeigen")
        print("5. Programm beenden")
        choice = input("\nWas möchtest du tun?(1/2/3)\n")
        if choice == "1":
            name = input("Was möchtest du der Einkaufsliste hinzufügen?\n")
            amount = input("Wieviele?\n")
            price = input("(Ungefährer) Preis des einzelnen Artikels?\n")
            add_item(name, amount, price)
        elif choice == "2":
            id = input("Welchen Artikel (id, zu finden in der Einkaufsliste) möchtest du bearbeiten? \n")
            name = input("Aktualisierter Name des Artikels:\n")
            amount = input("Aktualisierte Menge:\n")
            price = input("Aktualisierter Preis:\n")
            update_item(id, name, amount, price)
        elif choice == "3":
            id = input("Welchen Artikel (id) möchtest du löschen?\n")
            delete_item(id)
        elif choice == "4":
            show_items()
        elif choice == "5":
            print("Programm wird beendet. Auf Wiedersehen")
            break
        else:
            print("Ungültige Auswahl. Bitte wähle 1,2,3,4 oder 5\n")

if __name__ == "__main__":
    main()