import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters  
    if use_digits:
        characters += string.digits  
    if use_special_chars:
        characters += string.punctuation  

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Basit Şifre Oluşturucuya Hoşgeldiniz!")

    while True:
        length = int(input("Şifre uzunluğunu girin: "))
        use_digits = input("Rakamları içerecek misiniz? (1: Evet, 2: Hayır): ") == '1'
        use_special_chars = input("Özel karakterleri içerecek misiniz? (1: Evet, 2: Hayır): ") == '1'

        password = generate_password(length, use_digits, use_special_chars)
        print("Oluşturulan Şifre:", password)

        again = input("Başka bir şifre oluşturmak istiyor musunuz? (1: Evet, 2: Hayır): ")
        if again != '1':
            print("Şifre oluşturucu kapatılıyor.")
            break

if __name__ == "__main__":
    main()