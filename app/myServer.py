## This is a dummy web server - just for netomedia Home Assessment
# http://hostname  should return hellow world
# http://hostname/intense should do CPU load

import flask
import time
from math import sqrt
from sys import argv


## web application initializatgion ....
app = flask.Flask(__name__)


def isPrime(num):
    # check if num is prime number (the bad way to do it) just to make cpu load
    num = abs(num)
    if num < 3:
        return num > 1
    stop = int(sqrt(num))
    for x in range(2,stop):
        if num % x == 0:
            return False
    return True

def useCPU(timeDuration):
    start = time.time()
    #pList=[]
    for x in range(11,9999999999999999999):
        s=time.time()
        tmp=isPrime(x)
        #if tmp:
        #    pList.append(x)
        e=time.time() - s
        if e > 0.2:
            print("Test of %d took %5fSec" % (x,e))
        if time.time() - start > timeDuration:
            print("Test duration end: %5fSec" % (time.time() - start))
            print( 'x is' , x)
            return None
@app.route('/')
def helloWorld():
    return flask.Response('Hello World')

@app.route('/intense')
def intense():
    useCPU(60)
    return flask.Response("Finished CPU load")

if __name__ == '__main__':
    print("Start Test ....", time.ctime())
    port = argv[1] if len(argv) > 1 else 80
    app.run(host='0.0.0.0',port=port)
    exit()
    tmp = useCPU(55)
    print("found %d prime numbers" % len(tmp))
    if len(tmp) > 150:
        print(" show only the last numbers ...")
        st = len(tmp) - 150
    else:
        st = 0

    while st < len(tmp):
         print(', '.join( [ str(i) for i in tmp[st:st + 10] ]  ))
         st += 10

