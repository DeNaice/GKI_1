import xml.etree.ElementTree as ET

tree = ET.parse('Bundespräsidenten.xml')
root = tree.getroot()

for text in root.findall('collection'):
    data = text.find('rohtext').text
    print(data)





print("Funktioniert nicht")

