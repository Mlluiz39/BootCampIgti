# trabalahando com arquivos xml

from xml.dom import minidom

nome_do_arquivo_xml = 'arquivo_xml.xml'
documento_xml = minidom.parse(nome_do_arquivo_xml)

documento_xml

# nos presentes no documento
nos = documento_xml.documentElement
print(nos.tagName)

# extraindo elementos de um arquivo xml
# cada elemento em um arwuivo xml tem um nome
lista_de_compras = documento_xml.getElementsByTagName('item')
type(lista_de_compras)

lista_de_compras[0]

# acessando os atributos de um arquivo
for item in lista_de_compras:
    print(item.attributes['name'].value)

# Acessando os elementos de um arquivo
for item in lista_de_compras:
    print(item.firstChild.data)
