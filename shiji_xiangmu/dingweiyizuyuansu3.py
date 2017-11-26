#coding=utf-8
#!/user/bin/python

from selenium import webdriver
import os,time

dr5 = webdriver.Firefox()
file_path ='file:///' +  os.path.abspath('ckeckbox.html')
dr5.get(file_path)

#print(time)