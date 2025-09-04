# [[file:README.org::*Direkte indlæsning af designfil][Direkte indlæsning af designfil:1]]
import sys

# Import af filen/modulet roeversprog.py -
# Læg mærke til at .py ikke er taget med.
import roeversprog

from PySide6.QtWidgets import QApplication 
from PySide6.QtUiTools import QUiLoader
# Læg mærke tile at QMainWindow ikke importeres.
# I stedet importeres QObject i stedet for.
# QMainWindow er anvendt i Designer.
from PySide6.QtCore import QObject


# loader-objekt som bruges til at loade .ui-filen
loader = QUiLoader()





# Læg mærke til at klassen nedarver fra QObject i stedet for QMainWindow
class Roeversprogsoversaetter(QObject):
    def __init__(self):
        super().__init__()
        self.translate_roeversprog = True
        # Her loades brugerfladen fra Designer.
        self.ui = loader.load("roeversprogsoversaetter.ui", None)
        # self.ui refererer til selve brugerfladen som for nu er af typen
        # QMainWindow, og som indeholder et gridLayout og en pushbutton
        self.ui.setWindowTitle("Direkte indlæsning fra ui")
        # Her sættes signal og slot op for oversaetknap og metoden oversaet
        self.ui.oversaet_knap.clicked.connect(self.oversaet)
        self.ui.skift_oversaetning.clicked.connect(self.translate_bool)
        # self.ui.show()

    def translate_bool(self):
        """ Reverse the translation. """
        self.translate_roeversprog = not self.translate_roeversprog
        self.ui.text1.setPlainText("")
        self.ui.text2.setPlainText("")
        if self.translate_roeversprog == False:
            self.ui.label.setText("Røversprog")
            self.ui.label_2.setText("Regular language")
        else:
            self.ui.label_2.setText("Røversprog")
            self.ui.label.setText("Regular language")


    def oversaet(self):
        # Denne metode anvender funktionen oversaet_til_roeversprog, som
        # ligger i modulet roeversprog (som er importeret i starten)
        if self.translate_roeversprog == True:
            output_fra_oversaetteren = roeversprog.oversaet_til_roeversprog(
                self.ui.text1.toPlainText()
            )
        elif self.translate_roeversprog == False:
            output_fra_oversaetteren = roeversprog.oversaet_fra_roeversprog_til_andet_sprog(
                self.ui.text1.toPlainText()
            )
            
        self.ui.text2.setPlainText(output_fra_oversaetteren)

        # I skal selv sørge for at forbedre den metode, så den gør
        # som I ønsker


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
roeversprogsoversaetter = Roeversprogsoversaetter()
roeversprogsoversaetter.ui.show()
program.exec()
# Direkte indlæsning af designfil:1 ends here
