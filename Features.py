import os
os.environ["CLASSPATH"] = "./jAudio/jAudio.jar"
from jnius import autoclass


class Features():
    
    def __init__(self):
        os.chdir("./jAudio")
        DataModel = autoclass("jAudioFeatureExtractor.DataModel")
        print(os.getcwd())
        self.model = DataModel("/home/steve/Desktop/ErgasiaSP/jAudio/features.xml", None)
        self.setNames()
        self.enabled = self.model.defaults
        self.primary = self.model.is_primary

    def printPrimaryFeatures(self):
        for fname in self.names:
            if self.primary[self.names.index(fname)]:
                print(fname)

    def setNames(self):
        self.names = []
        for m in self.model.featureDefinitions:
            self.names.append(m.name)
        
    def changeState(self, name):
        self.enabled[self.names.index(name)] = not self.enabled[self.names.index(name)]
    
    def getBoolValue(self, name):
        return self.enabled[self.names.index(name)]
