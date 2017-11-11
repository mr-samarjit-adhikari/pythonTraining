from PySide.QtCore import QTime, QTimer, Qt
from PySide.QtGui import QApplication, QLabel

import sys
import time

def quitApplication(app):
    return app.quit

if __name__=='__main__':

    app = QApplication(sys.argv)
    due = QTime.currentTime()
    message = "Alert! "

    try:
        if len(sys.argv) < 2:
            raise ValueError("Not enough arguments")

        hours, minutes = sys.argv[1].split(":")
	    #python SimpleApp.py 09:32 <optional message>

        due = QTime(int(hours),int(minutes))
        if not due.isValid():
            raise ValueError("Input time is not Valid")

        if len(sys.argv) > 2:
            message += " ".join(sys.argv[2:])

    except ValueError as e:
        print e.args
        print "Usage: python  SimpleApp.py HH:MM  [message]"
        sys.exit(0)

    while QTime.currentTime() < due:
        time.sleep(5)

    label = QLabel("<font color=red size=36 >"+message+"</font>")
    label.setWindowFlags(Qt.SplashScreen)
    label.show()

    QTimer.singleShot(10000,quitApplication(app))
    app.exec_() # Run the application
