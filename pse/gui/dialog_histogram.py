""" Bibliotecas externas. """
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QRadioButton)
from PyQt5.QtCore import (Qt)

class DialogHistogram(QDialog):
    def __init__(self, parent = None):
        super(DialogHistogram, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.initUI()


    def initUI(self):        
        layout = QHBoxLayout()

        self.b1 = QRadioButton('RGB')
        self.b1.setChecked(True)
        self.b1.toggled.connect(lambda:self.btnState(self.b1))
        layout.addWidget(self.b1) 

        self.b2 = QRadioButton('RED')
        self.b2.toggled.connect(lambda:self.btnState(self.b2))
        layout.addWidget(self.b2)

        self.b3 = QRadioButton('GREEN')
        self.b3.toggled.connect(lambda:self.btnState(self.b3))
        layout.addWidget(self.b3) 

        self.b4 = QRadioButton('BLUE')
        self.b4.toggled.connect(lambda:self.btnState(self.b4))
        layout.addWidget(self.b4)       

        self.setLayout(layout)
        self.setWindowTitle('Histograms')


    def btnState(self, b):
        if b.text() == 'RBG':
            if b.isChecked() == True:
                print(b.text() + ' is selected')
            else:
                print(b.text() + ' is deselected')

        if b.text() == 'RED':
            if b.isChecked() == True:
                print(b.text() + ' is selected')
            else:
                print(b.text() + ' is deselected')

        if b.text() == 'GREEN':
            if b.isChecked() == True:
                print(b.text() + ' is selected')
            else:
                print(b.text() + ' is deselected')

        if b.text() == 'BLUE':
            if b.isChecked() == True:
                print(b.text() + ' is selected')
            else:
                print(b.text() + ' is deselected')


    @staticmethod
    def getResults(parent = None):
        """ Método estático que cria o dialog e retorna true com sua finalização """
        dialog = DialogHistogram(parent)
        result = dialog.exec_()
        return True