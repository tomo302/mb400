def keyword():
    gojyuon = []
    boon = ['a', 'i', 'u', 'e', 'o']
    sion = ['k', 's', 't', 'n', 'h', 'm', 'y', 'r', 'w']
    for bo in boon:
        gojyuon.append(bo)
    for row in sion:
        for _ in boon:
            if not (row+_)== "wi" and not (row+_)=="wu" and not (row+_)=="we" and not (row+_)=="wo":
                #print("あたりです")
                gojyuon.append(row + _)
    return gojyuon
