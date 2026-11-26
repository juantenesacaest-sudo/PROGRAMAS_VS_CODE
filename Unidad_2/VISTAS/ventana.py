#Ventana con PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)  
ventana = QMainWindow()      
ventana.setWindowTitle("Ventana Corporativa")
ventana.setFixedSize(400, 200)
ventana.resize(500, 200)
ventana.show()
sys.exit(app.exec())