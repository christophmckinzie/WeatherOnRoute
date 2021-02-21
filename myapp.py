import sys
import os
import io
import WeatherClass
from PyQt5.QtGui import QPixmap, QTextCursor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtCore import QSize, Qt, QRect, QDate, QDateTime, QUrl
from PyQt5.QtWidgets import (
      QApplication,
      QLineEdit,
      QMainWindow,
      QWidget,
      QLabel,
      QDateEdit,
      QPushButton,
      QComboBox,
      QFormLayout,
      QTextBrowser
)

class MainWindow(QMainWindow):
      def __init__(self):
            super().__init__()

            self.setWindowTitle('Weather On Route Application')
            self.resize(800, 600)
            self.layout = QFormLayout() # layout object
            self.setStyleSheet("background-color: white")

            self.origin = QLineEdit()
            self.origin.setStyleSheet("background: white;")
            self.origin.setPlaceholderText("Starting address here")
            self.origin.textChanged.connect(self.get_user_origin)

            self.destination = QLineEdit()
            # self.destination.setStyleSheet("background: white;")
            self.destination.setPlaceholderText("Ending address here")
            self.destination.textChanged.connect(self.get_user_destination)
            
            self.weather_type = QComboBox()
            self.weather_type.currentTextChanged.connect(self.get_user_weather_type)
            self.weather_type.addItems(['Snow', 'Rain', 'Clouds'])

            self.date = QDateEdit()
            self.date.dateChanged.connect(self.get_user_date)

            self.number_of_checks = QLineEdit()
            # self.number_of_checks.setStyleSheet("background: white;")
            self.number_of_checks.setPlaceholderText("Number of locations to check for weather")
            self.number_of_checks.textChanged.connect(self.get_user_number_of_checks)

            self.qlabel_origin = QLabel("Origin")
            # self.qlabel_origin.setStyleSheet("color: white;")
            self.layout.addRow(self.qlabel_origin, self.origin)

            self.qlabel_destination = QLabel("Destination")
            # self.qlabel_destination.setStyleSheet("color: white;")
            self.layout.addRow(self.qlabel_destination, self.destination)

            self.qlabel_weather = QLabel("Weather Type")
            # self.qlabel_weather.setStyleSheet("color: white;")
            self.layout.addRow(self.qlabel_weather, self.weather_type)

            self.qlabel_date = QLabel("Date of Travel")
            # self.qlabel_date.setStyleSheet("color: white;")
            self.layout.addRow(self.qlabel_date, self.date)

            self.qlabel_number_of_checks = QLabel("Number of Checks")
            # self.qlabel_number_of_checks.setStyleSheet("color: white;")
            self.layout.addRow(self.qlabel_number_of_checks, self.number_of_checks)

            # adding pushbutton 
            self.pushButton = QPushButton()
            self.pushButton.setText("Produce Map")
            self.pushButton.setStyleSheet("font-size: 10pt; \
                                 border-style: solid; \
                                 border-radius: 15px; \
                                 border-width: 1.5px; \
                                 border-color: rgb(20, 173, 173);")
            self.pushButton.setGeometry(QRect(200, 150, 93, 28))

            # adding signal and slot  
            self.pushButton.clicked.connect(self.produce_map)
            self.layout.addWidget(self.pushButton)  

            # add widget for housing html
            self.browser = QWebEngineView()

            # add layout to widget and set as central widget
            widget = QWidget()
            widget.setLayout(self.layout)
            self.setCentralWidget(widget)

      def get_user_origin(self, s):
            self.origin_input = s
            
      def get_user_destination(self, s):
            self.destination_input = s

      def get_user_weather_type(self, s):
            self.weather_type_input = s

      def get_user_date(self, s):
            self.date_input = s.toPyDate()
            self.date_input = self.date_input.strftime("%Y-%m-%d")

      def get_user_number_of_checks(self, s):
            self.number_of_checks_input = int(s)

      def produce_map(self):
            # call WeatherClass.py and create map
            w = WeatherClass.WeatherMapping(origin=self.origin_input, destination=self.destination_input, weather_type=self.weather_type_input, date_of_travel=self.date_input, num_of_checks=self.number_of_checks_input)
            self.map = w.weather_map()

            # save map data
            data = io.BytesIO()
            self.map.save(data, close_file=False)

            # get map data
            self.browser.setHtml(data.getvalue().decode())
            self.layout.addWidget(self.browser)
            
if __name__ == '__main__':
      app = QApplication(sys.argv)
      window = MainWindow()
      window.show()
      app.exec_()
