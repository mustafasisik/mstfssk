from time import (time,
                  sleep)



def timer(fn):
    def inner(*args, **kwargs):
        t = time()
        fn(*args, **kwargs)
        print "took {ahmet}".format(ahmet=time()-t)

    return inner

@timer
def speak(topic):
    sleep(2)
    print "My speach is " + topic

#speaker = timer(speak)
speaker("FP with Python")
