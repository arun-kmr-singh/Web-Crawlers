import time
import requests

from bs4 import BeautifulSoup

filea = open("logfile.txt","a+")
filea.write("Log File \n \n \n")


def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
	t_end = time.time() + 60 * 2
	while time.time() < t_end:
		for link in s.findAll('a', {'class':'s-access-detail-page'}):
        		tet = link.get('title')
        		print(tet)
			filea.write(tet + "\n")
        		tet_2 = link.get('href')
        		print(tet_2)
			filea.write(tet_2 + "\n")


			
web(1,'https://www.amazon.in/mobile-phones/b?ie=UTF8&node=1389401031&ref_=sd_allcat_sbc_mobcomp_all_mobiles')

filea.close()
