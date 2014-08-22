#coding: utf-8
state = "out"
kapi = "kapali"

while state != "close":
    expectation = raw_input("\nNe yapmak istiyorsunuz?(in, out, ac , kapat):")
    if expectation == "in" or expectation == "out":
        if kapi == "kapali":
            print "Once kapiyi acmalisiniz(ac)"
        else:
            if expectation == "in":
                if state == "out":
                    state = "in"
                    print "Now you are inside."
                else:
                    print "You are already inside."
            elif expectation == "out":
                if state == "in":
                    state = "out"
                    print "You are outside"
                else:
                    print "You are already outside."
            else:
                state = "close"
    elif expectation == "ac":
        kapi = "acik"
        print "kapi simdi acik. \nkapiyi kapatmak icin kapat yaziniz"
    elif expectation == "kapat":
        kapi = "kapali"
        print "kapi simdi kapali. \nacmak icin ac yaziniz"
    else:
        state = "close"
