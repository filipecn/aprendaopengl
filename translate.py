#!/usr/bin/bash

import urllib.request
from googletrans import Translator
from bs4 import BeautifulSoup
import argparse
import sys

parser = argparse.ArgumentParser(description='learnopengl.com translator')
parser.add_argument('link', help='link address of the page you want to translate')
parser.add_argument('output_file', help='translated output markdown file location')
parser.add_argument('--output_language', help='language to be translated to', default='pt')
parser.add_argument('--google_translate_link', help='link to google translate', default='translate.google.com.br')
parser.add_argument('--verbose', help='print translation progress', action="store_true")
args = parser.parse_args()

fp = urllib.request.urlopen(args.link)
mybytes = fp.read()
html = mybytes.decode("utf8")
fp.close()


soup = BeautifulSoup(html, 'lxml')

md_file = open(args.output_file, "w")

md_file.write('---\n')
md_file.write('title: \"Iluminação Básica\"\n')
md_file.write('date: 2020-10-29T15:28:58-03:00\n')
md_file.write('draft: false\n')
md_file.write('katex: true\n')
md_file.write('markup: "mmark"\n')
md_file.write('---\n\n')

md_file.write("[Post Original](" + args.link + ")\n\n")


def translateText(text):
    if args.verbose:
    	print("trying to translate:")
    	print(text)
    fail_count = 0 
    for i in range(10):
        translator = Translator(service_urls=[args.google_translate_link])
        try:
            output = translator.translate(text, src='en', dest=args.output_language)
            if args.verbose:
            	print("translated into:")
            	print(output.text)
            return output.text
        except Exception as e:
            fail_count += 1
    if args.verbose:
    	print("failed to translate after " + str(fail_count) + " attempts!")
    return text


content_div = soup.find('div', id='content')
total_elements = len(content_div.find_all())
element = 0
for p in content_div.find_all():
    if p.name == 'h1':
        md_file.write(f"# {p.text}\n\n")
    if p.name == 'h2':
        md_file.write(f"## {p.text}\n\n")
    if p.name == 'p':
        md_file.write(translateText(p.text) + '\n\n')
    if p.name == 'a':
        md_file.write('(' + p.get('href') + ')\n\n')
    if p.name == 'img':
        md_file.write('![altlogo](https://learnopengl.com' + p.get('src') + ')\n\n')
    if p.name == 'pre':
        md_file.write('```cpp\n')
        md_file.write(p.text + '\n')
        md_file.write('```\n\n')
    if p.name == 'li':
        md_file.write(translateText(p.text) + '\n\n')
    if p.name == 'note':
        md_file.write("{{% greenbox tip %}}\n")
        md_file.write(translateText(p.text) + '\n\n')
        md_file.write("{{% /greenbox %}}\n\n")
    if p.name == 'warning':
        md_file.write("{{% greenbox warning %}}\n")
        md_file.write(translateText(p.text) + '\n\n')
        md_file.write("{{% /greenbox %}}\n\n")
    element += 1
    if not args.verbose:
        sys.stdout.write("\rtranslating... %d%%" % ((element / total_elements) * 100.0))
        sys.stdout.flush()
if not args.verbose:
    print()
md_file.close()
