import sys
from PySide import QtCore, QtGui

class MainWindow(QtGui.QWidget):
    def __init__(self):
		QtGui.QWidget.__init__(self)

		layout = QtGui.QVBoxLayout()
		self.setLayout(layout)


######  Text Fields Created here  ########

		self.WeeklyRent = QtGui.QLineEdit("WeeklyRent")
		self.AgencyFee = QtGui.QLineEdit("AgencyFee")
		self.MonthlyMortgage = QtGui.QLineEdit("MonthlyMortgage")

		fields = (self.WeeklyRent,self.AgencyFee,self.MonthlyMortgage)

		for line in fields:
			line.setEnabled(True)
			line.setAlignment(QtCore.Qt.AlignRight)
			line.setFont(QtGui.QFont("Verdana",9))
			layout.addWidget(line)

######  Button Created here  ########
		self.bCalculate = QtGui.QPushButton('- Calculate -')
		self.bCalculate.setFont(QtGui.QFont("Verdana",10))
		layout.addWidget(self.bCalculate)

######  Labels Created here  ########
		self.labelPaid = QtGui.QLabel()
		layout.addWidget(self.labelPaid)

		self.labelAgency = QtGui.QLabel()
		layout.addWidget(self.labelAgency)

		self.labelProfit = QtGui.QLabel()
		layout.addWidget(self.labelProfit)

######  Connections made here  ########
		self.bCalculate.clicked.connect(self.rentValue)

		self.w=QtGui.QWidget()
		self.w.setWindowTitle("Rent Earnings")

		self.show()

    def rentValue(self):
		'''

		COLLECT VARIABLES

		'''    	
		self.months = 12
		self.weeks = 52
		self.rent = float(self.WeeklyRent.text())
		self.fee = float(self.AgencyFee.text())
		self.mortgage = float(self.MonthlyMortgage.text())

		self.paid = (self.rent*self.weeks)/self.months
		self.labelPaid.setText("Tenants Pay: {0:.2f} GBP".format(self.paid))
		self.labelPaid.setFont(QtGui.QFont("Verdana",14))

		self.agency = (self.fee*self.paid)/100
		self.labelAgency.setText("Agency Keeps: {0:.2f} GBP".format(self.agency))
		self.labelAgency.setFont(QtGui.QFont("Verdana",14))

		self.labelProfit.setText("We Earn: {0:.2f} GBP".format(self.paid-self.agency-self.mortgage))
		self.labelProfit.setFont(QtGui.QFont("Verdana",14))


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	mw = MainWindow()
	app.exec_()
