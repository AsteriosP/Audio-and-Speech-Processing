import xml.etree.ElementTree as ET


class XmlHandler():
    def __init__(self):
        self.tree = ET.parse('test2_batchfile.xml')
        self.root = self.tree.getroot()
        self.batch = self.root.find("batch")
        self.fileSet = self.batch.find("fileSet")
        self.features = self.batch.find("settings").findall("feature")


        # append an element to fileSet
        elem = ET.Element("fileSet",{})
        elem.text = "test/path"
        self.fileSet.append(elem)
        # print(len(self.features))
        for feature in self.features:
            print(feature.find("name").text)

        # print(self.batch.getchildren())
        # for ch in self.fileSet.getchildren():
        #     print(ch.text)
    
    


if __name__ == "__main__":
    t = XmlHandler()
    
    # for child in t.root:
    #     print(child.tag, child.attrib)

