#! usr/bin/python
import re


file=open('SearchResults (1).csv', 'r')
books_url = file.read()
file.close()

regex = re.compile("http:\/\/[A-Za-z\.]*\/[A-Za-z]*\/[0-9\.]*\/[0-9\-]*")

lista = regex.findall(books_url)

string = ''
num_libros = 0

for item in lista:
	string = string + item+('\n')
	num_libros = num_libros + 1

print num_libros

file=open('urls.txt', 'w')
file.write(string)
file.close()
