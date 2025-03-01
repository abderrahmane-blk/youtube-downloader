import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSettings


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




        # ! the settings

        
        # Initialize QSettings (in the registry on Windows, in plist on macOS) as QSettings("YourCompany", "YourApp")
        self.settings = QSettings("abdou_dev", "downloader y")
        #? Load saved settings
        self.load_settings()


    def button_clicked(self):
        print("Button clicked!")

    def download_video(self):
        url = []
        url.append( self.lineEdit_3.text())
        print("the url:   "+ self.lineEdit_3.text())
        # print(url)
        # print(self.checkBox.isChecked())


        # ! now the download 
        compelete =False
    
        thePath = self.lineEdit_4.text()
        print(thePath)
        if thePath == "":
            thePath = "./"
                
        thePath = str(Path(thePath).absolute()).replace("\\", "/")  # Resolve to absolute path , then replace the \ with /
        print("the paaath is :  ")
        print(thePath)

        quality_to_download =self.quality_comboBox.currentText()

        if self.checkBox.isChecked():
            try:
                self.label_7.setText("Downloading...")
                complete = download.Download(url ,thePath, True,quality_to_download)

            except:
                print("error downloading1")
            finally:
                self.label_7.setText("...")





        else: #if not a playlist
            try:
                self.label_7.setText("Downloading...")
                complete = download.Download(url ,thePath, False ,quality_to_download) 
                




                #? now check the quality
                # !just checking here
                # print("\n\ncheck the quality:---------------------------------- " )
                # quality = quality_to_download
                # if quality == "best quality":
                #     quality_format = 'bestvideo+bestaudio/best'
                # # elif quality == "audio only":
                # #     quality_format = 'bestaudio/best'
                # elif quality in ['144' , '360' ,'480', '520' ,'560' , '720' ,'1080' , '1440', '2160' ,'2560', '4320']:
                #     quality_format = f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'
                # else:
                #     quality_format = 'bestvideo+bestaudio/best'
                #     print("quality not found, downloading the best quality available")

                
                # print("the quality is : ",end="")
                # print(quality_format)
                # print("the quality type is : ",end="")
                # print(type(quality_format))


                # print("end-check the quality:----------------------------------\n " )
                
                # ! end of checking



                


            except:
                print("error downloading")
            finally:
                self.label_7.setText("...")

        if compelete:
            self.label_3.setText("Downloaded")
            self.label_7.setText("no")
        else:
            self.label_3.setText("an error occured : not downloaded")
            self.label_7.setText("no")



#   ! these 3 methods are for the settings
    def load_settings(self):
        # Example: Load a saved value for a line edit
        download_path = self.settings.value("where_to_download", "./downloads/")
        self.lineEdit_4.setText(download_path)
    
        # the quality combobox
        quality = self.settings.value("combo_box_value", "1080")    
        self.quality_comboBox.setCurrentText(quality)


    def save_settings(self):
        # Example: Save the current text in a line edit
        self.settings.setValue("where_to_download", self.lineEdit_4.text())
        self.settings.setValue("combo_box_value", self.quality_comboBox.currentText())


    def closeEvent(self, event):
        # Save settings when the app is closed
        self.save_settings()
        super().closeEvent(event)



# ! the main and the start of the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())