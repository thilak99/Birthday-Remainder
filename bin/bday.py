import sys,os
import splunk.Intersplunk
def matching():
    f = open("C:\\Users\\ibnus\\Documents\\bday\\birthday.txt","r")
    a=f.readlines()
    f.close()
    return a

a = matching()
splunk.Intersplunk.outputResults([{"result":a}])     
