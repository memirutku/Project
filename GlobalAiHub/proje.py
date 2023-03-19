#İclal Kurt
#Mustafa Emir Utku


#Main

# txt de okuma
PizzaTxt = open('pizza.txt','r')
SauceTxt = open('sauce.txt','r')


#Pizza için txt de ki dosyayı dictionary çevirme
satirlarPizza = PizzaTxt.readlines()
pizzaDict = []
for i in satirlarPizza:
    pizzaDict.append(i.split(":"))
pizzaDict=dict(pizzaDict)



#Sos için txt de ki dosyayı dictionary çevirme
satirlarSos = SauceTxt.readlines()
SauceDict = []
for i in satirlarSos:
    SauceDict.append(i.split(":"))
SauceDict=dict(SauceDict)


#txt kapama işlemi
PizzaTxt.close()
SauceTxt.close()

# txt de okuma ve kullanıcıdan veri alma işlemi
PizzaTxt = open('pizza.txt','r')
SauceTxt = open('sauce.txt','r')

[print(line) for line in PizzaTxt.readlines()]
ChosenPizza=input("Lütfen Bir Pizza Tabanı Seçiniz:")

[print(line) for line in SauceTxt.readlines()]
ChosenSauce=input("Pizzanız için sos seçiniz:")

#txt kapama işlemi
PizzaTxt.close()
SauceTxt.close()


#pizza için dictionary ile kullanıcını değerini eşitleyip yazdırıyor
for x in pizzaDict:
   if ChosenPizza==x:
    print("Seçilen pizza:\n"+pizzaDict[x])

#sos için dictionary ile kullanıcını değerini eşitleyip yazdırıyor
for y in SauceDict:
   if ChosenSauce==y:
    print("Seçilen sos:\n"+SauceDict[y])


#pizza için super class
class Pizza():
    def __init__(self, descriptionPizza, costPizza):
        self.descriptionPizza = descriptionPizza
        self.costPizza = costPizza

    def get_description(self):
        return self.descriptionPizza

    def get_cost(self):
        return self.costPizza

#pizza için subclasslar açıklamaları ve fiyatları
class Klasik(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza, İtalyan mutfağından köken alan, genellikle yuvarlak bir hamur tabanının üzerine domates sosu ve peynir ile çeşitli malzemelerin eklenerek hazırlanan bir yemektir. ", 10.99)

class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza, İtalyan mutfağına ait klasik bir pizzadır ve adını İtalya Kraliçesi Margherita'dan almıştır. Pizza, ince hamur tabanının üzerine domates sosu, rendelenmiş mozzarella peyniri ve taze fesleğen yapraklarından oluşur.", 12.99)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizzası, Türk mutfağına ait bir yemektir ve 'Pide' olarak da adlandırılır. İnce hamur tabanının üzerine domates sosu, kıyma, soğan, domates, biber, maydanoz ve baharatlar gibi malzemeler eklenerek hazırlanır.", 14.99)

class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza, İtalyan mutfağına ait bir pizzadır ve 'Pizza Margherita' olarak da bilinir. Pizza, ince hamur tabanının üzerine domates sosu ve mozzarella peyniri ile hazırlanır.", 16.99)



#Sos için super class
class Decorator():
    def __init__(self, descriptionSos, costSos):
        self.descriptionSos = descriptionSos
        self.costSos = costSos

    def get_description(self):
        return self.descriptionSos

    def get_cost(self):
        return self.costSos

#sos için subclasslar açıklamalar ve fiyatları
class Zeytin(Decorator):
    def __init__(self):
        super().__init__("Zeytin, pizza yapımında sıkça kullanılan bir malzemedir. Zeytinler, lezzetleri ve farklı renkleri ile pizza hamurunun sosu ve diğer malzemeleriyle harmanlandığında, mükemmel bir lezzet oluştururlar. Zeytinler, zeytinyağı, sağlıklı yağlar ve lif açısından zengin olup, sağlıklı bir seçenek sunarlar. Siyah veya yeşil renkleriyle ve küçük boyutlarıyla pizza tasarımlarında kullanılmak üzere çeşitli şekillerde kesilebilirler. Zeytinli pizza, müşterilerinize sağlıklı ve lezzetli bir seçenek sunmanızı sağlar ve menünüzde yer alması gereken popüler bir seçenektir.", 10.99)

class Mantarlar(Decorator):
    def __init__(self):
        super().__init__("Mantar, pizza'nın popüler bir malzemesidir. Doğal olarak lif, protein ve vitamin açısından zengin, düşük kalorili ve lezzetli bir seçenektir. Mantarlar, pizza hamurunun sosu ve diğer malzemeleriyle harmanlanarak mükemmel bir lezzet oluşturur ve müşterilere çeşitli seçenekler sunar.", 12.99)

class KeciPeyniri(Decorator):
    def __init__(self):
        super().__init__("Keçi peyniri, keçi sütünden yapılan bir peynirdir. Genellikle beyaz renklidir ve yoğun bir lezzete sahiptir. Daha az sert ve daha kremamsı bir dokusu vardır ve diğer peynirlere göre daha az yağlı ve daha düşük kalorilidir.", 14.99)

class Et(Decorator):
    def __init__(self):
        super().__init__("Et, sağlıklı protein ve diğer besinler açısından zengin olup, müşterilere doyurucu bir pizza deneyimi sunarlar.", 16.99)

class Sogan(Decorator):
    def __init__(self):
        super().__init__("Soğan, pizza yapımında yaygın olarak kullanılan bir sebzelerdir. Soğanın keskin tadı ve aroma profili, pizzalara benzersiz bir tat ve lezzet katar.", 16.99)

class Misir(Decorator):
    def __init__(self):
        super().__init__("Mısır, tatlı ve lezzetli bir sebzelerdir ve pizza hamuru, sosu ve diğer malzemeleriyle mükemmel bir şekilde uyum sağlar.", 16.99)



#toplama işlemi fonksiyon
#dicten veriyi alıp onu classlar ile eşleyip fiyatı çekiyor
def ToplamaIslemi():

#pizza eşitleme
 classPizza=pizzaDict[(ChosenPizza)]
 if str(classPizza[-1:])=="\n":
   classPizza=str(classPizza[1:-1])
   convPizza=f"{classPizza}().get_cost()"

 else:
  classPizza=str(classPizza)
  convPizza=f"{classPizza}().get_cost()"


#sos eşitleme
 classSos=SauceDict[(ChosenSauce)]
 if str(classSos[-1:])=="\n":
  classSos=str(classSos[1:-1])
  convSos=f"{classSos}().get_cost()"   #zeytin().get_cost()
  classSos=str(classSos)
  convSos=f"{classSos}().get_cost()"

#stringi eval() ile koda çevirme
 pizzaFiyat=eval(convPizza)
 sosFiyat=eval(convSos)
 ToplamFiyat=sosFiyat+pizzaFiyat
 return ToplamFiyat


#açıklama fonksiyonu
def Acıklama():

#pizza eşitleme
 classPizza=pizzaDict[(ChosenPizza)]
 if str(classPizza[-1:])=="\n":
  classPizza=str(classPizza[1:-1])
  converPizza=f"{classPizza}().get_description()"
 else:
  classPizza=str(classPizza)
  converPizza=f"{classPizza}().get_description()"

#sos eşitleme
 classSos=SauceDict[(ChosenSauce)]
 if str(classSos[-1:])=="\n":
  classSos=str(classSos[1:-1])
  converSos=f"{classSos}().get_description()"
 else:
  classSos=str(classSos)
  converSos=f"{classSos}().get_description()"

#stringi ecal() ile koda çevirme
 sosAcıklama=eval(converSos)
 pizzaAcıklama=eval(converPizza)
 ToplamAcıklama=f"Seçilen sosun Açıklaması:{sosAcıklama}\nSeçilen Pizzanın Açıklaması:{pizzaAcıklama}"
 return ToplamAcıklama



#Acıklama print işlemi
ToplamAcıklama=Acıklama()
print(f"{ToplamAcıklama}\n")

#toplama işlemi print etmek
ToplamFiyat=ToplamaIslemi()
print(f"Toplam fiyatınız: {ToplamFiyat}\n")



#Kullanıcıdan alınan özel veriler burada
Name=input("Adınızı ve Soyadınızı giriniz:")
IdentityNo=input("Tc kimlik numaranızı giriniz:")
CardNo=input("Kredi kartı numaranızı giriniz:")
CardPass=input("Kredi kartı şifrenizi giriniz:")

#importlar
import csv
import datetime

#zaman
time = datetime.datetime.now()
# csv dosyasının açılımı
file = open('bilgiler.csv', 'a')
# yazdırmak için
writer = csv.writer(file)
# içindekileri detaylandırma Ad-Soyad, Kimlik numarası, Kart Numarası, Kart Şifresi, Zaman, Toplam Fiyat
data = [Name, IdentityNo, CardNo, CardPass, time,ToplamFiyat]
writer.writerow(data)
# csv nin kapanması
file.close()
