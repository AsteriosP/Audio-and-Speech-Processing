import sys
import os
from PyQt4 import QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Features import *
from Recordings import *


qtCreatorFile = "FeatureExtractor.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.path = os.getcwd()
        self.features = Features()
        self.recs = Recordings()
        self.initFeatureSelectionTab()
        self.initRecordingsTab()
        self.setupGlobalConnections()

    def initFeatureSelectionTab(self):
        chkBoxLayout = QVBoxLayout()
        self.featureBoxes = {}
        # mEvent = QMouseEvent(QEvent.MouseButtonDblClick, )
        for fname in self.features.names:
            cbox = QCheckBox(fname)
            cbox.setChecked(self.features.getBoolValue(fname))
            # cbox.stateChanged.connect(lambda:self.handleCheckBox(cbox))
            self.featureBoxes[fname]=cbox
            chkBoxLayout.addWidget(cbox)
        chkBoxLayout.addStretch(1)
        chkBoxLayout.setMargin(0)
        chkBoxLayout.setContentsMargins(0, 0, 0, 0)
        chkBoxLayout.setSpacing(0)
        widget = QWidget()
        widget.setLayout(chkBoxLayout)

        scrollArea = QScrollArea()
        scrollArea.setMinimumWidth(1021)
        scrollArea.setMinimumHeight(600) 
        scrollArea.setWidgetResizable(True)
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setWidget(widget)
        lay = QVBoxLayout(self.featureTab)
        lay.addWidget(scrollArea)

    def initRecordingsTab(self):
        self.selectFolder.clicked.connect(self.setTrackTable)
        self.folderPath.returnPressed.connect(self.setTrackTable)
        self.btnTest.clicked.connect(self.getWindowingParameters)
        self.overlapPercentage.valueChanged.connect(self.updatePercentageLabel)
        # self.btnTest.clicked.connect(self.recs.rertieveTracks)
        # print("test")

    def setupGlobalConnections(self):
        self.btnExit.clicked.connect(self.exit)
        self.btnTestGlobal.clicked.connect(self.printFeatures)

    def setTrackTable(self):
        self.recs.loadRecordings("/home/steve/Music/")
        self.trackTableWidget.setColumnCount(3)
        self.trackTableWidget.setRowCount(80)
        self.recs.constractTrackTable(self.trackTableWidget)

    def getWindowingParameters(self):
        self.windowSize = self.winSize.value()
        self.windowOverlap = self.overlapPercentage.value()
        print("window Size:", self.windowSize)
        print("window Overlap:", self.windowOverlap)

    def updatePercentageLabel(self):
        self.lblOverlap.setText("Overlaping ("+ str(self.overlapPercentage.value()) +" %)")

    def printFeatures(self):
        print("=============================")
        for fname in self.features.names:
            if self.featureBoxes[fname].isChecked():
                print(fname)
        
    
    def exit(self):
        print("terminating...")
        sys.exit()

    def handleCheckBox(self, box:QCheckBox):
        print("handle:", box.text())
        self.features.changeState(box.text())

        # modifiers = QtGui.QApplication.keyboardModifiers()
        # print(box)
        # if modifiers == Qt.ControlModifier:
        #     box.setChecked(True)
        #     self.changeParameters = 10 #### TODO: Call A Function to edit parameters of the features
            

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_()) 
