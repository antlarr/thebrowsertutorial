from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTranslator, QLocale
from mainwindow import MainWindow
import sys
import os

def main():
    app = QApplication(sys.argv)
    
    locale_name = QLocale.system().name()
    filename = "thebrowser." + locale_name
    languages_directory = os.path.dirname(__file__) + "/../../cpp/languages/"
    translator = QTranslator()
    if not translator.load(filename, languages_directory):
        print(f"The language file wasn't found in {languages_directory} . "
              "Please adjust the sources to search for the translation files "
              f"in the right directory or add a translation for {locale_name}")
    app.installTranslator(translator)

    
    w = MainWindow(app)
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
