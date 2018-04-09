lennud = { 
    "Pariis" : {"London", "Berliin", "Nice", "New York", "Stockholm", "Rooma", "Washington"},
    "New York" : {"London", "Berliin", "Pariis", "Hong Kong", "Peking", "Moskva", "Washington"},
    "London" : {"Berliin", "Pariis", "New York", "Kaplinn", "Stockholm", "Moskva", "Peking", "Washington", "Rooma", "Mogadishu", "York"},
    "Berliin": {"London", "Pariis", "Tallinn", "New York", "Moskva", "Washington", "Rooma"},
    "Tallinn": {"Berliin", "Helsinki", "Tartu"},
    "Kaplinn" : {"New York"},
    "Hong Kong" : {"New York", "Peking"},
    "Helsinki" : {"Tallinn", "London", "Stockholm", "Moskva"},
    "Nice" : {"Pariis"},
    "Stockholm" : {"Pariis", "London", "Helsinki", "Moskva"},
    "Peking" : {"Hong Kong", "New York", "Washington"},
    "Rooma" : {"Pariis", "Berliin", "London"},
    "Moskva" : {"London", "New York", "Berliin", "Washington", "Helsinki", "Stockholm", "Kiiev"},
    "Washington" : {"New York", "London", "Pariis", "Peking", "Moskva", "Berliin", "Ottawa", "Wellington"},
    "Tartu" : {"Tallinn"},
    "Kiiev" : {"Moskva"},
    "Ottawa" : {"Washington"},
    "Mogadishu" : {"London"},
    "Wellington" : {"Washington"},
    "York" : {"London"}
}

def saab_lennata(lähtelinn, sihtlinn, andmebaas):
    võimalikud_lennud=andmebaas[lähtelinn]
    for i in võimalikud_lennud:
        if i==sihtlinn:
            print("Otselend võimalik")
            return
    for i in võimalikud_lennud:
        for j in andmebaas[i]:
                if j==sihtlinn:
                    print("Ühe ümberistumisega lend võimalik")
                    return
    for i in võimalikud_lennud:
        for j in andmebaas[i]:
            for k in andmebaas[j]:
                if k==sihtlinn:
                    print("Kahe ümberistumisega lend võimalik")
                    return
    print("Kahe või vähema ümberistumiseta pole lend võimalik")
                    

saab_lennata("London", "Tartu", lennud)