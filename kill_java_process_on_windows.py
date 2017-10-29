import subprocess as sp
import re
import sys, getopt

def executeCommandAndGetOutput(commandArray):
    ss = sp.check_output(commandArray, shell=True)
    test_str = (ss).decode("utf-8")
    return test_str


def main(argv=["jboss7asdasd"]):
    if(len(argv)>0):
        arg=argv[0]
        
    # try tasklist for windows
    test_str = executeCommandAndGetOutput(["jps" , "-lv"])
    print("==========================================================")
    print(test_str)
    print("==========================================================")
    p = re.compile('^(\d+)(.*)('+arg+')', re.MULTILINE | re.IGNORECASE )
    #if( != None):
    #match = re.search(p, test_str)
    matchList = re.findall(p, test_str)

    #print(matchList)
    for match in matchList:
        processId = match[0]
        print(processId)
        # works on windows
        executeCommandAndGetOutput(["taskkill", "/f" , "/pid" , processId])
        #print(out)
    if (len(matchList) == 0):
        print("nothing found with this: " + arg)


if (__name__ == "__main__"):
    main(sys.argv[1:])