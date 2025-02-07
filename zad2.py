print("Witaj w programie do tworzenia Listy Zakupów Weekendowych!")
produkty = []
ilosc = []
zakupy = {}

# Funkcja do sortowania
def sort(element):
    produkt, ilosc = element
    return -ilosc, produkt  

while True:
    item = input("Podaj produkt lub wpisz 'koniec', aby zakończyć dodawanie produktów: ")


    #print(produkty)
    if item == 'koniec':

        
        posortowane = sorted(zakupy.items(), key=sort)

        
        i = 1
        for produkt, ilosc in posortowane:
            print(str(i) + ". " + produkt + " - " + str(ilosc) + "szt.")
            i += 1
        break
    else:
        try:
            count = int(input("Podaj ilość: "))
            zakupy[item] = count
        except ValueError:
            print("Błąd")
        




