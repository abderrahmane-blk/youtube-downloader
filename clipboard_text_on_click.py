from PySide6.QtWidgets import QApplication, QLineEdit
from PySide6.QtGui import QClipboard

class ClipboardPasteLineEdit(QLineEdit):
    def mousePressEvent(self, event):
        super().mousePressEvent(event)  # Call the original event handler
        clipboard = QApplication.clipboard()
        self.setText(clipboard.text())