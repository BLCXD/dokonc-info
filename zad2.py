print("Witaj w programie do tworzenia Listy Zakupów Weekendowych!")
produkty = []
ilosc = []


while True:
    item = input("Podaj produkt lub wpisz 'koniec', aby zakończyć dodawanie produktów: ")

    #print(produkty)
    if item == 'koniec':
        '''
        print("twoja lista")
        for i in range(len(produkty)):

            print(f'{produkty[i]} - {ilosc[i]}szt.')
        break
        '''
        produkty_s = {}
        for i in range(len(produkty)):

            produkty_s[produkty[i]] = ilosc[i]
            x = dict(sorted((produkty_s.items())))



        print(produkty_s)
        print(x)
        break

    else:
        produkty.append(item)
        count = int(input("Podaj ilość: "))
        ilosc.append(count)



