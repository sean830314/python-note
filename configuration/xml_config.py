import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


def conver_dic_to_xml(tag, d):
    elem = ET.Element(tag)
    for key, val in d.items():
        child = ET.Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


def read_xml(file):
    with open(file) as f:
        content = f.read()
    return content


if __name__ == "__main__":
    content = read_xml(os.path.dirname(__file__) + "/config/config.xml")
    cfg = BeautifulSoup(content)
    print(cfg.mysql.host.contents[0])
    print(cfg.mysql.user.contents[0])
    print(cfg.mysql.passwd.contents[0])
    print(cfg.mysql.db.contents[0])
    print(cfg.other.food['value'])
    data_list = []
    for tag in cfg.other.type.stripped_strings:
        data_list.append(tag)
    print(data_list)
    dic = {'food': ['Sweet', 'Spicym', 'Sour']}
    element = conver_dic_to_xml('other', dic)
    mydata = ET.tostring(element)
    print(mydata)
    myfile = open(os.path.dirname(__file__) + "/config/write.xml", "wb")
    myfile.write(mydata)
