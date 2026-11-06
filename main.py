import sys
import getpass
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt # Importar Qt para alineaciones

app = QApplication(sys.argv)

visor = QWidget()
visor.setWindowTitle("Laboratorio PyQt6 - Metrología")
visor.resize(500, 400)

# 1. Crear el distribuidor de espacio vertical
layout_principal = QVBoxLayout()

usuario = getpass.getuser()

# 2. Crear los elementos (Widgets)
titulo = QLabel(f"Bienvenido {usuario}")
boton_inicio = QPushButton("Iniciar Evaluación GUM")
boton_atras = QPushButton("Andar atras")

# (Opcional) Darle formato al título para que parezca un encabezado
titulo.setAlignment(Qt.AlignmentFlag.AlignHCenter)
fuente = titulo.font()
fuente.setPointSize(20)
titulo.setFont(fuente)

# 3. Agregar los elementos al Layout
layout_principal.addWidget(titulo)
layout_principal.addWidget(boton_inicio)
layout_principal.addWidget(boton_atras)

# 4. Asignar el Layout a la ventana principal
visor.setLayout(layout_principal)

visor.show()
sys.exit(app.exec())