class TodoItem:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.done = False

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("İş eklendi.")

    def mark_done(self, index):
        if 0 <= index < len(self.items):
            self.items[index].done = True
            print("İş tamamlandı.")
        else:
            print("Geçersiz indeks.")

    def display_items(self):
        print("\nYapılacaklar Listesi:")
        for i, item in enumerate(self.items):
            status = "✔" if item.done else " "
            print(f"{i}. [{status}] {item.title} - Öncelik: {item.priority}")
            print(f"   Açıklama: {item.description}")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. İş Ekle")
        print("2. İş Tamamla")
        print("3. Listeyi Göster")
        print("4. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            title = input("İş Başlığı: ")
            description = input("Açıklama: ")
            priority = input("Öncelik (yüksek/orta/düşük): ").lower()
            todo_item = TodoItem(title, description, priority)
            todo_list.add_item(todo_item)
        elif choice == "2":
            index = int(input("Tamamlanan işin indeksini girin: "))
            todo_list.mark_done(index)
        elif choice == "3":
            todo_list.display_items()
        elif choice == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek.")

if __name__ == "__main__":
    main()
