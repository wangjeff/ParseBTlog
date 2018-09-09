# homework.py
# -*- coding: utf-8 -*-
import re

logfile  = "0908dupT1_2.log"
logfile2 = "0908notdupT2_3.log"
MACfile  = "MAC.txt"
parsefile1 = "Parse1.log"
parsefile2 = "Parse2.log"
split_data1 = '41ff'
split_data2 = '53741414'

## read file data into string
def file_read(carray , fname):
        with open(fname) as f:   
                for line in f:
                        carray.append(line)
                return carray

## add the newline in the string by using regulation expression
def data_withline(substring,inputstring):
    strinfo = re.compile(substring)
    linedata = strinfo.sub(substring+'\n',inputstring)
    return linedata

def parse_logfile(logfile,str1):
    f_log = open(logfile, "w")
    done_string1 = data_withline(split_data1,str1)
    done_string1 = data_withline(split_data2,str1)
    f_log.write(done_string1)
    file.close(f_log)

def parseHex(hexlogfile):
    f_hexlog  = open(hexlogfile, "rb")
    re_str = (f_hexlog.read()).encode("hex")
    file.close(f_hexlog)
    return re_str


def main():

    content_array = []
    total  = 0
    total2 = 0
    i = 0

    ## Read the Hex file and store into string format
    string1 = parseHex(logfile)
    string2 = parseHex(logfile2)

    ## parse the log file for analysis and generate new log file
    parse_logfile(parsefile1,string1)
    parse_logfile(parsefile2,string2)


    file_read(content_array,MACfile)
    package1 = string1.count("53741414")
    package2 = string2.count("53741414")
    print '=============Result============================='
    for macdata in content_array:
    	i = i + 1
    	macdata = macdata.lower().replace(' ', '').strip('\n')
    	count_string  = string1.count(macdata)
    	count_string2 = string2.count(macdata)
    	total  = total  + count_string
    	total2 = total2 + count_string2
        
        #print the result of count
        print ("%s.%s: %s    %s" % (i,macdata,count_string,count_string2))
        
    
    print "total is:%s    %s " % (total,total2)
    print "package/min:%s    %s " % (package1,package2)
    print '==============End============================'

if __name__=='__main__':
    main()    