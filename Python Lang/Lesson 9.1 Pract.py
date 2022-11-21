# Задача 1. Курьер

# Вам известен номер квартиры, этажность дома и количество квартир на этаже. Задача: написать функцию, которая по заданным
# параметрам напишет вам, в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.
import math


# практика
def dom(number_kvart, etagey, kvartir_etage):
    # округление в большую сторону ceil
    podezd = math.ceil(number_kvart / (kvartir_etage * etagey))
    etag = math.ceil((number_kvart - (podezd - 1) * kvartir_etage * etagey) / kvartir_etage)
    return podezd, etag


number_kvart = 208
etagey = 9
kvartir_etage = 6
podezd, etag = dom(number_kvart, etagey, kvartir_etage)

print("Для квартиры-", number_kvart, "Подьезд-", podezd, "Этаж-", etag)
