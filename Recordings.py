import os
from recordtype import recordtype
from PyQt4.QtGui import QTableWidgetItem, QTableWidget
from PyQt4.QtCore import *

Track = recordtype("Track", "name path genre")
class Recordings():
    def __init__(self):
        self.currPath = os.getcwd()
        # self.path = path
    
    def loadRecordings(self, path):
        os.chdir(path)
        print("Current folder:", os.getcwd())
        contents = os.listdir()
        self.tracks = []
        for content in contents:
            if os.path.isdir(content):
                os.chdir(os.path.join(path, content))
                print("path:", os.getcwd())
                songs = os.listdir()
                for s in songs:
                    self.tracks.append(Track(name=s, path=os.getcwd()+"/"+s, genre=content))
                os.chdir(path)
        os.chdir(self.currPath)

    def constractTrackTable(self, table:QTableWidget):
        self.horisontalHeaders = ["Name", "Path", "Genre"]
        self.table = table
        for n, track in enumerate(self.tracks):
            for m, header in enumerate(self.horisontalHeaders):
                if header == "Name":
                    newItem = QTableWidgetItem(track.name)
                elif header == "Path":
                    newItem = QTableWidgetItem(track.path)
                elif header == "Genre":
                    newItem = QTableWidgetItem(track.genre)
                
                newItem.setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled)
                # newItem.
                self.table.setItem(n, m, newItem)
        self.table.setHorizontalHeaderLabels(self.horisontalHeaders)
    
    def updateTrack(self, row, col, text):
        if col == 0:
            self.tracks[row].name = text
        elif col == 1:
            self.tracks[row].path = text
        elif col == 2:
            self.tracks[row].genre = text    
        # /home/steve/Music
    
    def rertieveTracks(self):
        model = self.table.model()
        data = []
        for row in range(model.rowCount()):
            if row < len(self.tracks):
                data.append([])
                for column in range(model.columnCount()):
                        index = model.index(row, column)
                        
                        self.updateTrack(row, column, str(model.data(index)))
            else:
                break
        [print(track) for track in self.tracks]


if __name__ == "__main__":
    recs = Recordings()
    recs.loadRecordings("/home/steve/Music/")
    print(recs.tracks)
