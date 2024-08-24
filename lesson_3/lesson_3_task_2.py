from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "Galaxy S24 Ultra", "+79001234555")
phone2 = Smartphone("Apple", "iPhone 15 Pro Max", "+79012345565")
phone3 = Smartphone("Xiaomi", "Readmi Note 10 Pro", "+79024567667")
phone4 = Smartphone("Google", "Pixel 9", "+79036787887")
phone5 = Smartphone("Huawei", "Pura 70 Ultra", "+79057899809")


catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} {phone.model} - {phone.phone_number}") 