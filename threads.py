import sys ,traceback
import time
from PySide6.QtCore import QThread, Signal,QObject, QRunnable, Slot
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton


class Wait_Thread(QThread):
    update_signal = Signal(str)
    done = Signal()

    def run(self):
        # for i in range(5):
        #     time.sleep(1)
        #     self.update_signal.emit(f"Count: {i + 1}")
        time.sleep(1)
        self.done.emit()





class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)





class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super().__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # #? Add the callback to our kwargs
        # self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done




















# !--------------------------------------------------

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.label = QLabel("Press the button to start the thread")
#         self.button = QPushButton("Start Thread")
#         self.button.clicked.connect(self.start_thread)

#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.button)
#         self.setLayout(layout)

#         self.thread = Download_WorkerThread()
#         self.thread.update_signal.connect(self.update_label)

#     def start_thread(self):
#         self.thread.start()

#     def update_label(self, text):
#         self.label.setText(text)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())