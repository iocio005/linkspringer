import requests
import time
import lxml.html
from urlparse import urljoin
from pyPdf import PdfFileWriter, PdfFileReader
import os
import resource

class Download_Book():

	def concatenate_pdf(self,book_title):
		fileList = os.listdir(os.getcwd())
		num_chapters=0
		for i in range(1,40):
			if not fileList.__contains__(book_title+str(i)+".pdf"):
				num_chapters= i-1
				print "numero capitulos"+str(num_chapters)
				break

		print"Uniendo pdfs..."
		output = PdfFileWriter()
		for i in range (1,num_chapters):
			f=open(book_title+str(i)+".pdf", "rb")
			num_pages=PdfFileReader(f).getNumPages()
			if num_pages==0:
				pdfOne = PdfFileReader(f).getPage(0)
				output.addPage(pdfOne)

			else:
				for a in range (0,num_pages):
					pdfOne = PdfFileReader(f).getPage(a)
					output.addPage(pdfOne)

		print file
		outputStream = file(r""+book_title+".pdf", "wb")
		output.write(outputStream)
		outputStream.close()

		print"Union finalizada"
		for i in range(1,num_chapters+1):
			print "borrando... capitulo: "+str(i)
			os.remove(book_title+str(i)+".pdf")

	def download(self,link):
		parent_url='http://link.springer.com'
		source = requests.get(link).content
		html = lxml.html.fromstring(source)
		book_title= html.cssselect('h1#title')[0].text_content() 
		chapter=01
		for i in html.cssselect('li.toc-item'):
			url=urljoin(parent_url,i.cssselect('div.actions')[0].cssselect('span.action')[0].cssselect('a')[0].get('href'))
			pdf=requests.get(url).content
			f = open(book_title+str(chapter)+'.pdf', 'wb+')
			f.write(pdf)
			chapter+=1
			print url
		Download_Book().concatenate_pdf(book_title)


print '''
************************************
*                                   *
* Books Downloader link springer 	*
*                                   *
*************************************
'''

"""

"""
#resource.setrlimit(resource.RLIMIT_NOFILE, (500,-1))

def Tres():
	Download_Book().download('http://link.springer.com/book/10.1007/978-3-642-22288-7')

 
def Uno():
    url = raw_input('Book URL: ')
    Download_Book().download(url)
 
def Dos():
	local_url = raw_input('URLs file path: ')
	urlfile = open('local_url', 'r')
	for line in urlfile.readlines():
		urlfile = line
		Download_Book().download(line)
		print "esperando 10 segundos para el siguiente libro..."
		time.sleep(10)
	
 


Switch = { 1 : Uno, 2 : Dos, 3 : Tres,}
print "Selecciona modo de actuacion"
print "1 - Descarga un libro"
print "2 - Descarga desde un fichero de urls"
print "3 - Modo pruebas"

num = raw_input("Introduce un numero \n")

Switch[int(num)]()