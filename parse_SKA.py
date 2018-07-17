####parse a downlaoded file
import os
from lxml import html
from lxml import etree
import xml.etree.ElementTree as ET
import re
from collections import OrderedDict


os.chdir('/Users/estebanlanter/Dropbox/Machine Learning/TextGenerator')

filedir = "/Users/estebanlanter/Dropbox/Machine Learning/TextGenerator/rawDat"
newFileDir = "/Users/estebanlanter/Dropbox/Machine Learning/TextGenerator/parseDat"
newFileDir2 = "/Users/estebanlanter/Dropbox/Machine Learning/TextGenerator/textDat"
for root, dirs, filenames in os.walk(filedir):
    print("try")
    for f in filenames:
        if f.endswith('.txt'):
            print("parsing "+str(f))
            path = os.path.join(root, f)
            text = open(path, 'r')
            message = text.read()
            text.close()
            htmlroot = html.fromstring(message)
            tree = htmlroot.getroottree()
            result = htmlroot.xpath('//*[@id="mainContent"]/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div')
            r = result[0]
            out_html = etree.tostring(r, pretty_print=True,encoding='unicode',doctype='<!DOCTYPE html>')
            out_onlytext = r.text_content() 
            
            try:    
                idx = out_html.index("Company description")+len("Company description")
                out_html = out_html[:idx] + '\n' + out_html[idx:]
            except ValueError:
                pass
            try:
                idx = out_html.index("Contact information")+len("Contact information")
                out_html = out_html[:idx] + '\n' + out_html[idx:]  
            except ValueError:
                pass
            try:    
                idx = out_onlytext.index("Company description")+len("Company description")
                out_onlytext = out_onlytext[:idx] + '\n' + out_onlytext[idx:]
            except ValueError:
                pass               
            try:
                idx = out_onlytext.index("Contact information")+len("Contact information")
                out_onlytext = out_onlytext[:idx] + '\n' + out_onlytext[idx:]  
            except ValueError:
                pass
            
            
            #remove top of page
            out_onlytext = re.sub('Top of page', '', out_onlytext, flags=re.M)
            #remove non ascii
            out_onlytext = ''.join([i if ord(i) < 128 else '' for i in out_onlytext])
            #remove tabs
            out_onlytext = re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', out_onlytext, flags=re.M)
            #remove multiple  \n
            out_onlytext = re.sub(r'\n\s*\n', '\n', out_onlytext)
            #remove \n at beginning
            out_onlytext = re.sub(r'^[\n]*', '', out_onlytext)
            #remove multiple spaces
            out_onlytext = re.sub(' +',' ',out_onlytext)
            #remove trailing and leading whitespaces
            out_onlytext = "\n".join([x.strip() for x in out_onlytext.split('\n')])        
            #remove duplicate lines
            out_onlytext = "\n".join(list(OrderedDict.fromkeys(out_onlytext.split("\n"))))
            
            out_html = re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', out_html, flags=re.M)
            out_html = re.sub(r'\n\s*\n', '\n\n', out_html)
            
            with open(os.path.join(newFileDir,"parsed"+f), "w") as cons_out:
                cons_out.write(out_html)     
                cons_out.close()
            with open(os.path.join(newFileDir2,"text"+f), "w") as cons_out:
                cons_out.write(out_onlytext)
                cons_out.close()    
                
                
                
#Company description
#Contact information
types = []
for root, dirs, filenames in os.walk(newFileDir2):
    for f in filenames:
        if f.endswith('.txt'):
            print("parsing "+str(f))
            path = os.path.join(root, f)
            text = open(path, 'r')
            message = text.read()
            text.close()
            cat = message.split('\n')[0]  
            types.append(cat)
from collections import Counter
Counter(types)
