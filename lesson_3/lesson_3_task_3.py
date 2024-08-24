from address import Address
from mailing import Mailing 

to_address = Address("12345", "Москва", "Крылова", "3", "55")

from_address = Address("23456", "Ростов-на-Дону", "Первомайская", "11", "65")

mailing = Mailing(to_address, from_address, 10000, "TRACK12345")

print(Mailing)