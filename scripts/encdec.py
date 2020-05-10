'''
Created on 26 апр. 2020 г.

@author: Unshiar
'''

import os
import sys
import codecs

#possible charsets list
charsetsList = ['ascii',
                'big5',
                'big5hkscs',
                'cp037',
                'cp273',
                'cp424',
                'cp437',
                'cp500',
                'cp720',
                'cp737',
                'cp775',
                'cp850',
                'cp852',
                'cp855',
                'cp856',
                'cp857',
                'cp858',
                'cp860',
                'cp861',
                'cp862',
                'cp863',
                'cp864',
                'cp865',
                'cp866',
                'cp869',
                'cp874',
                'cp875',
                'cp932',
                'cp949',
                'cp950',
                'cp1006',
                'cp1026',
                'cp1125',
                'cp1140',
                'cp1250',
                'cp1251',
                'cp1252',
                'cp1253',
                'cp1254',
                'cp1255',
                'cp1256',
                'cp1257',
                'cp1258',
                'euc_jp',
                'euc_jis_2004',
                'euc_jisx0213',
                'euc_kr',
                'gb2312',
                'gbk',
                'gb18030',
                'hz',
                'iso2022_jp',
                'iso2022_jp_1',
                'iso2022_jp_2',
                'iso2022_jp_2004',
                'iso2022_jp_3',
                'iso2022_jp_ext',
                'iso2022_kr',
                'latin_1',
                'iso8859_2',
                'iso8859_3',
                'iso8859_4',
                'iso8859_5',
                'iso8859_6',
                'iso8859_7',
                'iso8859_8',
                'iso8859_9',
                'iso8859_10',
                'iso8859_11',
                'iso8859_13',
                'iso8859_14',
                'iso8859_15',
                'iso8859_16',
                'johab',
                'koi8_r',
                'koi8_t',
                'koi8_u',
                'kz1048',
                'mac_cyrillic',
                'mac_greek',
                'mac_iceland',
                'mac_latin2',
                'mac_roman',
                'mac_turkish',
                'ptcp154',
                'shift_jis',
                'shift_jis_2004',
                'shift_jisx0213',
                'utf_32',
                'utf_32_be',
                'utf_32_le',
                'utf_16',
                'utf_16_be',
                'utf_16_le',
                'utf_7',
                'utf_8',
                'utf_8_sig']

# get only files from dir content list
def GetFilesOnly(dirItems):
    for dirItem in dirItems:
        if(not os.path.isfile(dirItem)):
            dirItems.remove(dirItem)
    return dirItems

def MsgHelp():
    print("Error - something wrong in parameters:")
    print("You need type: script.py sourceCharset targetCharset")
    print("For example: encdec.py cp1251 utf-8")
    print("This try convert all files from cp1251 to utf-8 codepage in current folder. Possible charsets list you find in this script.")


def MsgErrorSourceCharset():
    print("Error - SourceCharset name wrong:")
    print("You need type: script.py sourceCharset targetCharset")
    print("For example: encdec.py cp1251 utf-8")
    print("Possible charsets list you find in self script.")

def MsgErrorTargetCharset():
    print("Error - TargetCharset name wrong:")
    print("You need type: script.py sourceCharset targetCharset")
    print("For example: encdec.py cp1251 utf-8")
    print("Possible charsets list you find in self script.")    
     
#Programm
#incorrect parameters count
if len(sys.argv) != 3:
    MsgHelp()
    sys.exit(1)

sourceCharset = sys.argv[1]
targetCharset = sys.argv[2]
    
#incorrect sourceCharset
if sourceCharset not in charsetsList:
    MsgErrorSourceCharset()
    sys.exit(1)

#incorrect targetCharset
if targetCharset not in charsetsList:
    MsgErrorTargetCharset()
    sys.exit(1)

dirContent = os.listdir() #get current dir content (files and folders)
dirContent.remove(os.path.basename(__file__)) #remove self script-file from list

filesList = GetFilesOnly(list(dirContent))

for filename in filesList:
    fo = open(filename, 'rb', newline = None)
    byteContent = fo.read()    
    textContent = None
    
    #try decode bytes to string
    try:
        textContent = codecs.decode(byteContent, encoding = sourceCharset, errors = 'strict')
    except:
        print("Can't decode",filename,"with sourceCharset="+sourceCharset)
        continue  
    finally:
        fo.close()
        
    fw = open(filename, 'wb')
    fw.write(textContent.encode(encoding = targetCharset))
    fw.close()
