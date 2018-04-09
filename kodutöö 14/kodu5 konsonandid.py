vokaalid=("a", "e", "i", "o", "u", "õ", "ä", "ö", "ü")
def konsonandid(sõne):
    if len(sõne)==0: return ""
    else:
        täht=sõne[0]
        ülejäänud=sõne[1:]
    järgmine=konsonandid(ülejäänud)
    if täht not in vokaalid: return järgmine+täht
    else: return järgmine


print((konsonandid("vanapagana tagavara rahapada"))[::-1])