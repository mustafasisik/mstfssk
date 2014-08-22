#coding: utf-8
kapi = "kapali"
states = {"girside": "cik", "cikside": "gir"}
current_state = "cikside"
expected_string = states[current_state]

komut = " "
while True:
    komut = raw_input("Ne yapmak istersiniz\n")
    if komut == "exit":
        break
    elif komut == expected_string:
        if kapi == "kapali":
            print "%sside gitmek icin kapiyi acin" % expected_string
        else:
            current_state = "%sside" % komut
            print "Geldiginiz yer " + current_state
            expected_string = states[current_state]
    elif komut == "ac":
        kapi = "acik"
        print "kapi acildi"
    elif komut == "kapat":
        kapi = "kapali"
        print "Kapi kapatildi"
    else:
        print "Zaten oldugunuz yer " + current_state
