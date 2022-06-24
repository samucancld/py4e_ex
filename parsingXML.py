import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <sexo amount="poco">M</sexo>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
print('Sexo:',tree.find('sexo').text,'\nCantidad:',tree.find('sexo').get('amount'))