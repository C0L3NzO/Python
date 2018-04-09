def hulkade_otsekorrutis(A, B):
    kõik_paarid=set()
    for i in A:
        A_osa=i
        for j in B:
            B_osa=j
            osad=A_osa+B_osa
            kõik_paarid.add(osad)
    print(len(kõik_paarid))
    return(kõik_paarid)
print(hulkade_otsekorrutis({'♥','♦','♠','♣'}, {'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'}))