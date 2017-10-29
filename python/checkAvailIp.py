import subprocess as sp
import re
#s = "10.10.10." + str(i)
def checkAvailIp(prefix24,start,end):
  for i in range(start,end):
                    s = prefix24 + "." + str(i)
                    
                    #call(["ping", "-n" , "1", s])
                    try:
                        ss = sp.check_output(["ping", "-n" , "1", s], shell=True)#shell=True then the window should not be created
                        test_str = (ss).decode("utf-8")
                        p = re.compile(r'(host\sunreachable)', re.MULTILINE | re.IGNORECASE)
                        if(re.search(p, test_str) != None):
                            print(s)
                    except sp.CalledProcessError:
                        print("error while: " ,s)
                        pass
                    
      
if __name__=="__main__":
    checkAvailIp("10.10.10", 100, 110)
