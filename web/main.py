import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import * 
                                                     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = QWebEngineView()
    # print(QFile.exists("index.html"))
    # f = QFile("index.html", QIODevice.ReadWrite)
    # html = f.readAll()
    # f.close()
    # print(html)
    # view.setHtml(html)

    view.load(QUrl("www.baidu.com"))
    view.show()
    sys.exit(app.exec_())