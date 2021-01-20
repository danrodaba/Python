import sys
from PyQt5 import uic
from PyQt5.QtWidgets import * 


class FichaMago(QMainWindow):
    #enorme batería de variables:
    NOMBRE = ''
    JUGADOR = ''
    CRONICA = ''
    NATURALEZA = ''
    CONDUCTA = ''
    ESENCIA = ''
    AFILIACION = ''
    SECTA = ''
    CONCEPTO = ''
    identificacion = [NOMBRE, JUGADOR, CRONICA, NATURALEZA, CONDUCTA, ESENCIA, AFILIACION, SECTA, CONCEPTO]
    FUERZA = ''
    DESTREZA = ''
    RESISTENCIA = ''
    fisicos = [FUERZA, DESTREZA, RESISTENCIA]
    CARISMA = ''
    MANIPULACION = ''
    APARIENCIA = ''
    sociales = [CARISMA, MANIPULACION, APARIENCIA]
    PERCEPCION = ''
    INTELIGENCIA = ''
    ASTUCIA = ''
    mentales = [PERCEPCION, INTELIGENCIA, ASTUCIA]