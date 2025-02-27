import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon

# ! the resources.py
import resources_rc
import p1
import download

from pathlib import Path






class MainWindow(QMainWindow ,p1.Ui_MainWindow ):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("Downloader Y")

        self.pushButton_9.clicked.connect(self.button_clicked)
        self.pushButton_9.clicked.connect(self.download_video)



    def button_clicked(self):
        print("Button clicked!")

    def download_video(self):
        url = []
        url.append( self.lineEdit_3.text())
        print("the text:   "+ self.lineEdit_3.text())
        # print(url)
        # print(self.checkBox.isChecked())


        # ! now the download 
        compelete =False
    
        thePath = self.lineEdit_4.text()
        print(thePath)
        if thePath == "":
            thePath = "./downloads/"
                
        thePath = str(Path(thePath).absolute()).replace("\\", "/")  # Resolve to absolute path , then replace the \ with /
        print("the paaath is :  ")
        print(thePath)

        quality_to_download =self.quality_comboBox.currentText()

        if self.checkBox.isChecked():
            try:
                self.label_7.setText("Downloading...")
                download.Download(url ,thePath, True,quality_to_download)
                compelete = True
            except:
                print("error downloading1")
            finally:
                self.label_7.setText("...")





        else: #if not a playlist
            try:
                self.label_7.setText("Downloading...")
                # print("the value is:    " ,end ="")
                # print(self.quality_comboBox.currentText())
                download.Download(url ,thePath, False ,quality_to_download)
                compelete = True


            except:
                print("error downloading")
            finally:
                self.label_7.setText("...")

        if compelete:
            self.label_7.setText("Downloaded")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())