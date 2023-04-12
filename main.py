import random

secret_number = random.randint(1, 100)

guess = int(input("Tahmin ettiğiniz sayı nedir? "))

while guess != secret_number:
    if guess < secret_number:
        print("Daha yüksek bir sayı den
              


'''

Aşamalar:
Rastgele bir sayı seçin ve kullanıcının tahmin etmesini isteyin.
Kullanıcının tahminini alın ve tahmin doğru olana kadar aşağıdaki adımları tekrarlayın:
Tahmin edilen sayıyı, seçilen sayıdan büyük veya küçük olduğunu söylemek için kontrol edin.
Kullanıcıya yeni bir tahmin yapması için ipucu verin.
Kullanıcının doğru tahmin ettiğini belirtin ve oyunu bitirin.

'''