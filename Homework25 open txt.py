from pprint import pprint

text_file = 'texttexttext.txt'
file = open(text_file, mode='rb')
file_content = file.read()
file.close()
pprint(file_content.decode('utf-8'))