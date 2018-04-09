def tagurpidi(sõne):
    if len(sõne)==0: return ""
    else:
        täht=sõne[0]
        ülejäänud=sõne[1:]
    järgmine=tagurpidi(ülejäänud) #rekursioon
    return järgmine+täht
print((tagurpidi("abc")))