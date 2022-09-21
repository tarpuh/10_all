def checkpassword(username, password, ok, failed):
    glas, kol_vo_glas = list('eyuioa'), 0
    chisla, kol_vo_chisla = list('0123456789'), 0
    for i in list(password):
        if i in chisla:
            kol_vo_chisla += 1
        if i in glas:
            kol_vo_glas += 1
    if kol_vo_glas >= 3 and kol_vo_chisla >= 1 and len(password) - kol_vo_glas - kol_vo_chisla >= 2:
        return ok(password)
    return failed(password)


print(checkpassword('alex', 'aaabb111', ok=lambda x: x + ' - good password', failed=lambda x: x + ' - bad password'))
