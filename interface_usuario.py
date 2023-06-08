import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from statistics import mode
import numpy as np
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(self.frame)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 42))
        self.frame_superior.setStyleSheet("QtFrame{\n"
                                          "background-color:rgb(0,0,0)\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton{\n"
                                          "background-color:#000000;\n"
                                          "border-radius:20px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "background-color: rgb(61,61,61);\n"
                                          "border-radius:20px;\n"
                                          "}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Proyecto_Estadistica = QtWidgets.QLabel(self.frame_superior)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Proyecto_Estadistica.setFont(font)
        self.label_Proyecto_Estadistica.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Proyecto_Estadistica.setObjectName("label_Proyecto_Estadistica")
        self.horizontalLayout_3.addWidget(self.label_Proyecto_Estadistica)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_contenido = QtWidgets.QFrame(self.frame)
        self.frame_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenido.setObjectName("frame_contenido")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_contenido)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_menu = QtWidgets.QFrame(self.frame_contenido)
        self.frame_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_menu.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_menu.setStyleSheet("QFrame{\n"
                                      "background-color:rgb(0, 204, 204);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton{\n"
                                      "background-color:rgb(61,61,61);\n"
                                      "border-top-left-radius:20px;\n"
                                      "border-bottom-left-radius:20px;\n"
                                      "color:rgb(255,255,255);\n"
                                      "font 77 10pt \"Arial Black\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "background-color: white;\n"
                                      "border-top-left-radius:20px;\n"
                                      "border-bottom-left-radius:20px;\n"
                                      "color: rgb(0,0,0);\n"
                                      "font 77 10pt \"Arial Black\";\n"
                                      "}")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_base_de_datos = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_base_de_datos.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_base_de_datos.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1420398.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_base_de_datos.setIcon(icon)
        self.pushButton_base_de_datos.setObjectName("pushButton_base_de_datos")
        self.verticalLayout_3.addWidget(self.pushButton_base_de_datos)
        self.pushButton_calculos = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_calculos.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_calculos.setFont(font)
        self.pushButton_calculos.setIcon(icon)
        self.pushButton_calculos.setObjectName("pushButton_calculos")
        self.verticalLayout_3.addWidget(self.pushButton_calculos)
        self.horizontalLayout.addWidget(self.frame_menu)
        self.frame_pagina = QtWidgets.QFrame(self.frame_contenido)
        self.frame_pagina.setStyleSheet("QFrame{\n"
                                        "background-color:rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel{\n"
                                        "font: 87 14pt \"Arial Black\";\n"
                                        "background-color:#000000ff;\n"
                                        "color:rgb(61,61,61);\n"
                                        "border:0px solid #14C8DC;\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit{\n"
                                        "border:0px;\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border-bottom:2px solid rgb(61,61,61);\n"
                                        "font: 75 14pt \"Times New Roman\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton{\n"
                                        "background-color: rgb(61, 61, 61);\n"
                                        "border-radius:15px;\n"
                                        "color: rgb(255,255,255);\n"
                                        "font: 77 12pt \"Arial Black\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius:15px;\n"
                                        "color: rgb(0,0,0);\n"
                                        "font: 77 12pt \"Arial Black\";\n"
                                        "}\n"
                                        "\n"
                                        "QTableWidget{\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0,0,0);\n"
                                        "grindline-color:rgb(0, 204, 204);\n"
                                        "font-size: 12pt;\n"
                                        "color: #000000;\n"
                                        "}\n"
                                        "\n"
                                        "QHeaderView::section{\n"
                                        "background-color:rgb(0, 204, 204);\n"
                                        "border:1px solid rgb(0,0,0);\n"
                                        "font-size: 12pt;\n"
                                        "}\n"
                                        "\n"
                                        "QTableWidget QTableCornerButton::section{\n"
                                        "background-color: rgb(0, 0, 0);\n"
                                        "border:1px solid rgb(0,0,0);\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox {\n"
                                        "    border: 1px solid rgb(61, 61, 61);\n"
                                        "    border-radius: 5px;\n"
                                        "    padding: 1px 18px 1px 3px;\n"
                                        "    min-width: 8em;\n"
                                        "    background-color: rgb(61, 61, 61);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font: 75 12pt \"Arial Black\";\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox::drop-down {\n"
                                        "    subcontrol-origin: padding;\n"
                                        "    subcontrol-position: top right;\n"
                                        "    width: 15px;\n"
                                        "\n"
                                        "    border-left-width: 1px;\n"
                                        "    border-left-color: rgb(255, 255, 255);\n"
                                        "    border-left-style: solid;\n"
                                        "    border-top-right-radius: 5px;\n"
                                        "    border-bottom-right-radius: 5px;\n"
                                        "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                        "                                stop:0 #f6f7fa, stop:1 #dadbde);\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox QAbstractItemView {\n"
                                        "    border: 1px solid rgb(61, 61, 61);\n"
                                        "    selection-background-color: rgb(61, 61, 61);\n"
                                        "    background-color: rgb(172, 176, 175);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    font-size: 12pt;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.frame_pagina.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pagina.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pagina.setObjectName("frame_pagina")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_pagina)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget_paginas = QtWidgets.QStackedWidget(self.frame_pagina)
        self.stackedWidget_paginas.setObjectName("stackedWidget_paginas")
        self.page_base_de_datos = QtWidgets.QWidget()
        self.pushButton_base_de_datos.clicked.connect(
            lambda: self.stackedWidget_paginas.setCurrentWidget(self.page_base_de_datos))
        self.page_base_de_datos.setObjectName("page_base_de_datos")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_base_de_datos)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.subir_archivo = QtWidgets.QLabel(self.page_base_de_datos)
        self.subir_archivo.setAlignment(QtCore.Qt.AlignCenter)
        self.subir_archivo.setObjectName("subir_archivo")
        self.verticalLayout.addWidget(self.subir_archivo)
        self.pushButton_subir_archivo = QtWidgets.QPushButton(self.page_base_de_datos)
        self.pushButton_subir_archivo.clicked.connect(self.cargar_archivo)
        self.label_mensaje = QtWidgets.QLabel(self.page_base_de_datos)
        self.label_mensaje.setGeometry(QtCore.QRect(10, 10, 400, 20))

        self.pushButton_subir_archivo.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_subir_archivo.setObjectName("pushButton_subir_archivo")
        self.verticalLayout.addWidget(self.pushButton_subir_archivo)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.stackedWidget_paginas.addWidget(self.page_base_de_datos)
        self.page_calculos = QtWidgets.QWidget()
        self.pushButton_calculos.clicked.connect(lambda: self.stackedWidget_paginas.setCurrentWidget(self.page_calculos))
        self.page_calculos.setObjectName("page_calculos")
        self.layoutWidget = QtWidgets.QWidget(self.page_calculos)
        self.layoutWidget.setGeometry(QtCore.QRect(15, 20, 521, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.titulo_calculos = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.titulo_calculos.setFont(font)
        self.titulo_calculos.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_calculos.setObjectName("titulo_calculos")
        self.verticalLayout_5.addWidget(self.titulo_calculos)
        self.tableWidget_resultados = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget_resultados.setObjectName("tableWidget_resultados")
        self.tableWidget_resultados.setColumnCount(6)
        self.tableWidget_resultados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_resultados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_resultados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_resultados.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_resultados.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_resultados.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_resultados.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.verticalLayout_5.addWidget(self.tableWidget_resultados)
        self.stackedWidget_paginas.addWidget(self.page_calculos)
        self.verticalLayout_4.addWidget(self.stackedWidget_paginas)
        self.horizontalLayout.addWidget(self.frame_pagina)
        self.verticalLayout_2.addWidget(self.frame_contenido)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout_6.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_paginas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cargar_archivo(self):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.page_base_de_datos, 'Seleccionar archivo CSV', '',
                                                   'Archivos CSV (*.csv)')

        if file_path:
            try:
                # Leer los datos del archivo CSV y almacenarlos en una lista
                with open(file_path, 'r') as file:
                    reader = csv.reader(file)
                    datos_cargados = list(reader)
                    datos_cargados = [item.replace(',', '.') for sublist in datos_cargados for item in sublist]

                self.label_mensaje.setText("Archivo cargado correctamente")
                self.calcular_estadisticas(datos_cargados)
                self.datos_cargados = datos_cargados  # Establecer los datos cargados en el atributo de la clase
            except IOError:
                print("Error al leer el archivo")
        else:
            print("No se seleccionó ningún archivo")

    def calcular_estadisticas(self, datos_cargados):
        # Convertir los datos a números de punto flotante
        datos_flattened = [float(item) for item in datos_cargados if item != '']

        # Verificar que los datos no estén vacíos
        if not datos_flattened:
            print("No se encontraron datos")
            return

        # Realizar los cálculos estadísticos
        media = np.mean(datos_flattened)

        if len(datos_flattened) == 1:
            moda = mode(datos_flattened)[0]
        else:
            moda = mode(datos_flattened)

        mediana = np.median(datos_flattened)
        rango = np.max(datos_flattened) - np.min(datos_flattened)
        desviacion_estandar = np.std(datos_flattened)
        varianza = np.var(datos_flattened)

        # Llenar la tabla con los resultados
        self.tableWidget_resultados.setColumnCount(6)
        self.tableWidget_resultados.setRowCount(1)

        # Insertar los resultados en la tabla
        self.tableWidget_resultados.setItem(0, 0, QtWidgets.QTableWidgetItem(str(media)))
        self.tableWidget_resultados.setItem(0, 1, QtWidgets.QTableWidgetItem(f"{moda} (ocurrencias: {moda})"))
        self.tableWidget_resultados.setItem(0, 2, QtWidgets.QTableWidgetItem(str(mediana)))
        self.tableWidget_resultados.setItem(0, 3, QtWidgets.QTableWidgetItem(str(rango)))
        self.tableWidget_resultados.setItem(0, 4, QtWidgets.QTableWidgetItem(str(desviacion_estandar)))
        self.tableWidget_resultados.setItem(0, 5, QtWidgets.QTableWidgetItem(str(varianza)))

        self.graficar_datos(media, moda, mediana, rango, desviacion_estandar, varianza)

    def graficar_datos(self, media, moda, mediana, rango, desviacion_estandar, varianza):
        etiquetas = ['Media', 'Moda', 'Mediana', 'Rango', 'Desviación Estándar', 'Varianza']
        valores = [media, moda, mediana, rango, desviacion_estandar, varianza]

        # Convertir los valores a números de punto flotante
        valores = [float(valor) for valor in valores]

        # Crear la gráfica de barras
        plt.bar(etiquetas, valores)
        plt.xlabel('Estadísticas')
        plt.ylabel('Valores')
        plt.title('Estadísticas de los datos')

        # Mostrar la gráfica
        plt.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Proyecto_Estadistica.setText(_translate("MainWindow", "PROYECTO ESTADÍSTICA"))
        self.pushButton_base_de_datos.setText(_translate("MainWindow", " Base de Datos"))
        self.pushButton_calculos.setText(_translate("MainWindow", "Cálculos"))
        self.subir_archivo.setText(_translate("MainWindow", "Subir archivo .csv"))
        self.pushButton_subir_archivo.setText(_translate("MainWindow", "Subir archivo.."))
        self.titulo_calculos.setText(_translate("MainWindow", "Cálculos estadísticos"))
        item = self.tableWidget_resultados.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Media"))
        item = self.tableWidget_resultados.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Moda"))
        item = self.tableWidget_resultados.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mediana"))
        item = self.tableWidget_resultados.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Rango"))
        item = self.tableWidget_resultados.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Desviación Estándar"))
        item = self.tableWidget_resultados.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Varianza"))
        item = self.tableWidget_resultados.horizontalHeaderItem(6)

