import math

class GeometricShape:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Geometrik Şekil: {self.name}")

class Circle(GeometricShape):
    def __init__(self, radius):
        super().__init__("Daire")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

class Rectangle(GeometricShape):
    def __init__(self, width, height):
        super().__init__("Dikdörtgen")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(GeometricShape):
    def __init__(self, base, height):
        super().__init__("Üçgen")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self, side1, side2):
        return self.base + side1 + side2

def main():
    print("Geometrik Şekil Hesaplayıcı")

    while True:
        print("\n1. Daire")
        print("2. Dikdörtgen")
        print("3. Üçgen")
        print("4. Çıkış")
        choice = input("Hesaplamak istediğiniz şekli seçin (1/2/3/4): ")

        if choice == "1":
            radius = float(input("Dairenin yarıçapını girin: "))
            circle = Circle(radius)
            circle.display_info()
            print(f"Alan: {circle.calculate_area()}")
            print(f"Çevre: {circle.calculate_circumference()}")
        elif choice == "2":
            width = float(input("Dikdörtgenin uzunluğunu girin: "))
            height = float(input("Dikdörtgenin yüksekliğini girin: "))
            rectangle = Rectangle(width, height)
            rectangle.display_info()
            print(f"Alan: {rectangle.calculate_area()}")
            print(f"Çevre: {rectangle.calculate_perimeter()}")
        elif choice == "3":
            base = float(input("Üçgenin taban uzunluğunu girin: "))
            height = float(input("Üçgenin yüksekliğini girin: "))
            side1 = float(input("Üçgenin birinci kenar uzunluğunu girin: "))
            side2 = float(input("Üçgenin ikinci kenar uzunluğunu girin: "))
            triangle = Triangle(base, height)
            triangle.display_info()
            print(f"Alan: {triangle.calculate_area()}")
            print(f"Çevre: {triangle.calculate_perimeter(side1, side2)}")
        elif choice == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek.")

if __name__ == "__main__":
    main()
