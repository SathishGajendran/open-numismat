from PyQt4 import QtGui
from PyQt4.QtCore import Qt

class FormItem(object):
    def __init__(self, field, title, parent=None):
        self._field = field
        self._title = title
        self._widget = None
        self._label = QtGui.QLabel(title, parent)
        self._label.setAlignment(Qt.AlignRight)
    
    def field(self):
        return self._field

    def title(self):
        return self._title

    def label(self):
        return self._label

    def widget(self):
        return self._widget
    
    def setWidget(self, widget):
        self._widget = widget
        
    def value(self):
        return self._widget.text()

    def setValue(self, value):
        return self._widget.setText(value)

class BaseFormLayout(QtGui.QGridLayout):
    def __init__(self, record, parent=None):
        super(BaseFormLayout, self).__init__(parent)
        self.row = 0

    def addRow(self, item1, item2=None):
        if not item2:
            self.addWidget(item1.label(), self.row, 0)
            self.addWidget(item1.widget(), self.row, 1, 1, 3)
        else:
            self.addWidget(item1.label(), self.row, 0)
            self.addWidget(item1.widget(), self.row, 1)
    
            self.addWidget(item2.label(), self.row, 2)
            self.addWidget(item2.widget(), self.row, 3)

        self.row = self.row + 1

if __name__ == '__main__':
    from main import run
    run()