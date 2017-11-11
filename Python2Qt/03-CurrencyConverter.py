import sys
import urllib

from PySide.QtGui import QLabel, QComboBox, QDoubleSpinBox, QApplication, QGridLayout, QDialog


class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)

        date = self.get_data()
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)

        self.fromComboBox = QComboBox()
        self.toComboBox = QComboBox()

        self.fromComboBox.addItems(rates)
        self.toComboBox.addItems(rates)

        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01,1000)
        self.fromSpinBox.setValue(1.00)

        self.toLabel = QLabel("1.00")

        layout = QGridLayout();
        layout.addWidget(dateLabel,5,0)
        layout.addWidget(self.fromComboBox, 1,0)
        layout.addWidget(self.toComboBox,2,0)
        layout.addWidget(self.fromSpinBox,1,1)
        layout.addWidget(self.toLabel,2,1)

        self.setLayout(layout)

        #Connect Signal
        self.fromComboBox.currentIndexChanged.connect(self.update_ui)
        self.toComboBox.currentIndexChanged.connect(self.update_ui)
        self.fromSpinBox.valueChanged.connect(self.update_ui)

    def get_data(self):
        self.rates = {}

        try:
            date = "Unknown"
            # Thanks Mr Mark Summerfield
            fh = urllib.urlopen("http://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/csv?start_date=2017-01-03")

            for line in fh:
                line = line.rstrip()
                if not line or line.startswith(("#", "Closing")):
                    continue

                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]

                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass

            return "Exchange rates date: " + date
        except Exception, e:
            return "Failued to download:\n%s" % e


    def update_ui(self):
        from_ = self.fromComboBox.currentText()
        to = self.toComboBox.currentText()

        results = (self.rates[from_] / self.rates[to])*(self.fromSpinBox.value())

        self.toLabel.setText("%0.2f"%(results))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
