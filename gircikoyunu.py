#coding: utf-8

state = "out"
kapi = "kapali"
while state != "close":
    expectation = raw_input("\nNe yapmak istiyorsunuz?(in yada out):")
    if expectation == "ac":
        if kapi == "acik":
            print "kapi zaten acik"
        else:
            kapi = "acik"
            print "kapi simdi acik"
    elif expectation == "kapat":
        if kapi == "kapali":
            print "kapi zaten kapali"
        else:
            kapi = "kapali"
            print "kapi simdi kapali"

    elif expectation == "in":
        if state == "out":
            if kapi == "acik":
                state = "in"
                print "Now you are inside."
            else:
                print "kapi kapali giremezsiniz"
        else:
            print "You are already inside."
    elif expectation == "out":
        if state == "in":
            if kapi == "acik":
                state = "out"
                print "You are outside"
            else:
                print "kapi kapali cikamazsınız"
        else:
            print "You are already outside."
    else:
        state = "close"

