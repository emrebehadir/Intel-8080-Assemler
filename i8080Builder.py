#!/usr/bin/python3

# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import sys,os



sensiWebPagePath = "file:///usr/local/bin/i8080AssemblerSensi/8080Assembler.html"
fileName = sys.argv[1]
filepath = os.getcwd()+'/'+fileName
fileDir = os.getcwd()

try:
	os.remove(fileName.split(".")[0]+".com")
except:
	pass


with open(filepath, 'r') as content_file:
    content = content_file.read()


fo= webdriver.FirefoxOptions()
fo.headless = True

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir",fileDir)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")

print("\x1b[1;37;46m{}\x1b[0m" .format("Build start ...           "))

browser = webdriver.Firefox(fp,options=fo)

browser.get(sensiWebPagePath)
time.sleep(0.5)
print("\x1b[1;37;44m{}\x1b[0m" .format("Inserting data ...        "))
browser.find_element_by_xpath('//*[@id="source"]').clear()
browser.find_element_by_xpath('//*[@id="source"]').send_keys(content)
time.sleep(0.5)

tags = browser.find_elements_by_tag_name('pre')
print("\x1b[1;37;45m{}\x1b[0m" .format("Error Check Start ...     "))
errorFlag = True
for i in tags:
	if (i.get_attribute("class")=="errorline"):
		print ("\x1b[1;37;41m"+"Line "+ str( int(i.get_attribute("id")[1:]) +1 ) + " : "+"\x1b[0m" + "\x1b[1;30;47m"+ i.text +"\x1b[0m" )
		errorFlag=False

if(errorFlag):
	print("\x1b[1;37;42m{}\x1b[0m" .format("There is no error.        "))
	print("\x1b[1;37;42m{}\x1b[0m" .format("Error check is completed. "))
else:
	print("\x1b[1;37;41m{}\x1b[0m" .format("Error detected !!         "))

time.sleep(0.2)
browser.find_element_by_xpath('//*[@id="baton"]').click()
#time.sleep(2)
browser.quit()
print("\x1b[1;37;46m{}\x1b[0m" .format("Build ended ...           "))


