import sys
from PyQt5 import uic
from PyQt5.QtWidgets import * 



class FichaMago(QMainWindow):
    error = False
    gratuitos = 15

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('mago.ui', self)
        self.btn_crear.clicked.connect(self.crear_ficha)

        # Atributos
        self.spinFuerza.valueChanged.connect(self.datos_ficha)
        self.spinDestreza.valueChanged.connect(self.datos_ficha)
        self.spinResistencia.valueChanged.connect(self.datos_ficha)
        self.spinManipulacion.valueChanged.connect(self.datos_ficha)
        self.spinApariencia.valueChanged.connect(self.datos_ficha)
        self.spinPercepcion.valueChanged.connect(self.datos_ficha)
        self.spinInteligencia.valueChanged.connect(self.datos_ficha)
        self.spinAstucia.valueChanged.connect(self.datos_ficha)
        self.spinCarisma.valueChanged.connect(self.datos_ficha)

        # talentos
        self.spinAlerta.valueChanged.connect(self.datos_ficha)
        self.spinArte.valueChanged.connect(self.datos_ficha)
        self.spinAtletismo.valueChanged.connect(self.datos_ficha)
        self.spinCallejeo.valueChanged.connect(self.datos_ficha)
        self.spinConsciencia.valueChanged.connect(self.datos_ficha)
        self.spinEmpatia.valueChanged.connect(self.datos_ficha)
        self.spinExpresion.valueChanged.connect(self.datos_ficha)
        self.spinIntimidacion.valueChanged.connect(self.datos_ficha)
        self.spinLiderazgo.valueChanged.connect(self.datos_ficha)
        self.spinPelea.valueChanged.connect(self.datos_ficha)
        self.spinSubterfugio.valueChanged.connect(self.datos_ficha)

        # técnicas
        self.spinArmasFuego.valueChanged.connect(self.datos_ficha)
        self.spinMarciales.valueChanged.connect(self.datos_ficha)
        self.spinArtesania.valueChanged.connect(self.datos_ficha)
        self.spinConducir.valueChanged.connect(self.datos_ficha)
        self.spinDocumentacion.valueChanged.connect(self.datos_ficha)
        self.spinEtiqueta.valueChanged.connect(self.datos_ficha)
        self.spinMeditacion.valueChanged.connect(self.datos_ficha)
        self.spinArmas.valueChanged.connect(self.datos_ficha)
        self.spinSigilo.valueChanged.connect(self.datos_ficha)
        self.spinSupervivencia.valueChanged.connect(self.datos_ficha)
        self.spinTecnologia.valueChanged.connect(self.datos_ficha)

        # conocimientos
        self.spinAcademicismo.valueChanged.connect(self.datos_ficha)
        self.spinCiencias.valueChanged.connect(self.datos_ficha)
        self.spinCosmologia.valueChanged.connect(self.datos_ficha)
        self.spinEnigmas.valueChanged.connect(self.datos_ficha)
        self.spinEsoterismo.valueChanged.connect(self.datos_ficha)
        self.spinInformatica.valueChanged.connect(self.datos_ficha)
        self.spinInvestigacion.valueChanged.connect(self.datos_ficha)
        self.spinLeyes.valueChanged.connect(self.datos_ficha)
        self.spinMedicina.valueChanged.connect(self.datos_ficha)
        self.spinOcultismo.valueChanged.connect(self.datos_ficha)
        self.spinPolitica.valueChanged.connect(self.datos_ficha)
        

    
    def datos_ficha(self, crear_ficha):
        # Identificación
        self.NOMBRE = self.nombre.text()
        self.JUGADOR = self.jugador.text()
        self.CRONICA = self.cronica.text()
        self.NATURALEZA = self.naturaleza.text()
        self.CONDUCTA = self.conducta.text()
        self.ESENCIA = self.esencia.text()
        self.AFILIACION = self.afiliacion.text()
        self.SECTA = self.secta.text()
        self.CONCEPTO = self.concepto.text()

        # Atributos
        self.FUERZA = self.spinFuerza.value()
        self.DESTREZA = self.spinDestreza.value()
        self.RESISTENCIA = self.spinResistencia.value()
        self.CARISMA = self.spinCarisma.value()
        self.MANIPULACION = self.spinManipulacion.value()
        self.APARIENCIA = self.spinApariencia.value()
        self.PERCEPCION = self.spinPercepcion.value()
        self.INTELIGENCIA = self.spinInteligencia.value()
        self.ASTUCIA = self.spinAstucia.value()

        self.fisicos = [self.FUERZA, self.DESTREZA, self.RESISTENCIA]
        self.sociales = [self.CARISMA, self.MANIPULACION, self.APARIENCIA]
        self.mentales = [self.PERCEPCION, self.INTELIGENCIA, self.ASTUCIA]

        # esto es para reproducir la suma de cada una de las categorías de los atributos
        self.lbl_fisicos.setText(str((sum(self.fisicos)-3)))
        self.lbl_sociales.setText(str((sum(self.sociales)-3)))
        self.lbl_mentales.setText(str((sum(self.mentales)-3)))

        # Ahora vamos a hacer lo mismo con las habilidades.

        # talentos
        self.ALERTA = self.spinAlerta.value()
        self.ARTE = self.spinArte.value()
        self.ATLETISMO = self.spinAtletismo.value()
        self.CALLEJEO = self.spinCallejeo.value()
        self.CONSCIENCIA = self.spinConsciencia.value()
        self.EMPATIA = self.spinEmpatia.value()
        self.EXPRESION = self.spinExpresion.value()
        self.INTIMIDACION = self.spinIntimidacion.value()
        self.LIDERAZGO = self.spinLiderazgo.value()
        self.PELEA = self.spinPelea.value()
        self.SUBTERFUGIO = self.spinSubterfugio.value()

        # técnicas
        self.AFUEGO = self.spinArmasFuego.value()
        self.AMARCIALES = self.spinMarciales.value()
        self.ARTESANIA = self.spinArtesania.value()
        self.CONDUCIR = self.spinConducir.value()
        self.DOCUMENTACION = self.spinDocumentacion.value()
        self.ETIQUETA = self.spinEtiqueta.value()
        self.MEDITACION = self.spinMeditacion.value()
        self.PARMAS = self.spinArmas.value()
        self.SIGILO = self.spinSigilo.value()
        self.SUPERVIVENCIA = self.spinSupervivencia.value()
        self.TECNOLOGIA = self.spinTecnologia.value()

        # conocimientos
        self.ACADEMICISMO = self.spinAcademicismo.value()
        self.CIENCIAS = self.spinCiencias.value()
        self.COSMOLOGIA = self.spinCosmologia.value()
        self.ENIGMAS = self.spinEnigmas.value()
        self.ESOTERISMO = self.spinEsoterismo.value()
        self.INFORMATICA = self.spinInformatica.value()
        self.INVESTIGACION = self.spinInvestigacion.value()
        self.LEYES = self.spinLeyes.value()
        self.MEDICINA = self.spinMedicina.value()
        self.OCULTISMO = self.spinOcultismo.value()
        self.POLITICA = self.spinPolitica.value()

        self.talentos = [self.ALERTA, self.ARTE, self.ATLETISMO, self.CALLEJEO, self.CONSCIENCIA, self.EMPATIA, self.EXPRESION, self.INTIMIDACION, self.LIDERAZGO, self.PELEA, self.SUBTERFUGIO]
        self.tecnicas = [self.AFUEGO, self.AMARCIALES, self.ARTESANIA, self.CONDUCIR, self.DOCUMENTACION, self.ETIQUETA, self.MEDITACION, self.PARMAS, self.SIGILO, self.SUPERVIVENCIA, self.TECNOLOGIA]
        self.conocimientos = [self.ACADEMICISMO, self.CIENCIAS, self.COSMOLOGIA, self.ENIGMAS, self.ESOTERISMO, self.INFORMATICA, self.INVESTIGACION, self.LEYES, self.MEDICINA, self.OCULTISMO, self.POLITICA]
        
        self.lbl_tecnicas.setText(str((sum(self.fisicos)-3)))
        self.lbl_conocimientos.setText(str((sum(self.sociales)-3)))
        self.lbl_talentos.setText(str((sum(self.mentales)-3)))
        
        # esto es para reproducir la suma de cada una de las categorías de las habilidades
        self.lbl_talentos.setText(str(sum(self.talentos)))
        self.lbl_tecnicas.setText(str(sum(self.tecnicas)))
        self.lbl_conocimientos.setText(str(sum(self.conocimientos)))
    

    def crear_ficha(self):
    #if self.master_modo.isChecked() is False:
        # Identificación
        self.NOMBRE = self.nombre.text()
        self.JUGADOR = self.jugador.text()
        self.CRONICA = self.cronica.text()
        self.NATURALEZA = self.naturaleza.text()
        self.CONDUCTA = self.conducta.text()
        self.ESENCIA = self.esencia.text()
        self.AFILIACION = self.afiliacion.text()
        self.SECTA = self.secta.text()
        self.CONCEPTO = self.concepto.text()

        # Atributos
        self.FUERZA = self.spinFuerza.value()
        self.DESTREZA = self.spinDestreza.value()
        self.RESISTENCIA = self.spinResistencia.value()
        self.CARISMA = self.spinCarisma.value()
        self.MANIPULACION = self.spinManipulacion.value()
        self.APARIENCIA = self.spinApariencia.value()
        self.PERCEPCION = self.spinPercepcion.value()
        self.INTELIGENCIA = self.spinInteligencia.value()
        self.ASTUCIA = self.spinAstucia.value()

        #Ahora se agrupan en distintas listas y diccionarios
        self.dict_identificacion = {'Nombre' : self.NOMBRE, 'Jugador' : self.JUGADOR, 'Crónica' : self.CRONICA, 'Naturaleza' : self.NATURALEZA, 'Conducta' : self.CONDUCTA, 'Esencia' : self.ESENCIA, 'Afiliación' : self.AFILIACION, 'Secta' : self.SECTA, 'Concepto' : self.CONCEPTO}
        self.identificacion = [self.NOMBRE, self.JUGADOR, self.CRONICA, self.NATURALEZA, self.CONDUCTA, self.ESENCIA, self.AFILIACION, self.SECTA, self.CONCEPTO]
        self.fisicos = [self.FUERZA, self.DESTREZA, self.RESISTENCIA]
        self.sociales = [self.CARISMA, self.MANIPULACION, self.APARIENCIA]
        self.mentales = [self.PERCEPCION, self.INTELIGENCIA, self.ASTUCIA]
        self.dict_fisicos = {'Fuerza' : self.FUERZA , 'Destreza' : self.DESTREZA, 'Resistencia' : self.RESISTENCIA}
        self.dict_sociales = {'Carisma' : self.CARISMA , 'Manipulación' : self.MANIPULACION, 'Apariencia' : self.APARIENCIA}
        self.dict_mentales = {'Percepcion' : self.PERCEPCION , 'Inteligencia' : self.INTELIGENCIA, 'Astucia' : self.ASTUCIA}

        # esto es para reproducir la suma de cada una de las categorías de los atributos
        self.lbl_fisicos.setText(str((sum(self.fisicos)-3)))
        self.lbl_sociales.setText(str((sum(self.sociales)-3)))
        self.lbl_mentales.setText(str((sum(self.mentales)-3)))
        # en este fragmento vamos a comprobar que se cumplan las condiciones que nos pide la ficha respecto atributos

        if sum(self.fisicos) != 10 and sum(self.fisicos) != 8 and sum(self.fisicos) != 6:
        #    print('En la categoría "Físicos" no has sumado 3, 5 ni 7 puntos. Corrige este error o activa el modo máster.')
            self.error = True
        if sum(self.sociales) != 10 and sum(self.sociales) != 8 and sum(self.sociales) != 6:
        #    print('En la categoría "Sociales" no has sumado 3, 5 ni 7 puntos. Corrige este error o activa el modo máster.')
            self.error = True
        if sum(self.mentales) != 10 and sum(self.mentales) != 8 and sum(self.mentales) != 6:
        #    print('En la categoría "Mentales" no has sumado 3, 5 ni 7 puntos. Corrige este error o activa el modo máster.')
            self.error = True
        if sum(self.sociales) == sum(self.fisicos):
        #    print('Sociales y físicos tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.')
            self.error = True
        elif sum(self.mentales) == sum(self.fisicos):
        #    print('Mentales y físicos tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.')
            self.error = True
        elif sum(self.mentales) == sum(self.sociales):
        #    print('Mentales y sociales tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.')
            self.error = True
        
        # Ahora vamos a hacer lo mismo con las habilidades.

        # talentos
        self.ALERTA = self.spinAlerta.value()
        self.ARTE = self.spinArte.value()
        self.ATLETISMO = self.spinAtletismo.value()
        self.CALLEJEO = self.spinCallejeo.value()
        self.CONSCIENCIA = self.spinConsciencia.value()
        self.EMPATIA = self.spinEmpatia.value()
        self.EXPRESION = self.spinExpresion.value()
        self.INTIMIDACION = self.spinIntimidacion.value()
        self.LIDERAZGO = self.spinLiderazgo.value()
        self.PELEA = self.spinPelea.value()
        self.SUBTERFUGIO = self.spinSubterfugio.value()

        # técnicas
        self.AFUEGO = self.spinArmasFuego.value()
        self.AMARCIALES = self.spinMarciales.value()
        self.ARTESANIA = self.spinArtesania.value()
        self.CONDUCIR = self.spinConducir.value()
        self.DOCUMENTACION = self.spinDocumentacion.value()
        self.ETIQUETA = self.spinEtiqueta.value()
        self.MEDITACION = self.spinMeditacion.value()
        self.PARMAS = self.spinArmas.value()
        self.SIGILO = self.spinSigilo.value()
        self.SUPERVIVENCIA = self.spinSupervivencia.value()
        self.TECNOLOGIA = self.spinTecnologia.value()

        # conocimientos
        self.ACADEMICISMO = self.spinAcademicismo.value()
        self.CIENCIAS = self.spinCiencias.value()
        self.COSMOLOGIA = self.spinCosmologia.value()
        self.ENIGMAS = self.spinEnigmas.value()
        self.ESOTERISMO = self.spinEsoterismo.value()
        self.INFORMATICA = self.spinInformatica.value()
        self.INVESTIGACION = self.spinInvestigacion.value()
        self.LEYES = self.spinLeyes.value()
        self.MEDICINA = self.spinMedicina.value()
        self.OCULTISMO = self.spinOcultismo.value()
        self.POLITICA = self.spinPolitica.value()

        # los declaro como diccionarios y listas.
        self.dict_talentos = {'Alerta': self.ALERTA, 'Arte': self.ARTE, 'Atletismo': self.ATLETISMO, 'Callejeo': self.CALLEJEO, 'Consciencia': self.CONSCIENCIA, 'Empatia': self.EMPATIA, 'Expresión': self.EXPRESION,  'Intimidacion': self.INTIMIDACION, 'Liderazgo': self.LIDERAZGO, 'Pelea': self.PELEA, 'Subterfugio': self.SUBTERFUGIO}
        self.dict_tecnicas = {'Armas de fuego': self.AFUEGO, 'Artes Marciales': self.AMARCIALES, 'Artesania': self.ARTESANIA, 'Conducir': self.CONDUCIR, 'Documentación': self.DOCUMENTACION, 'Etiqueta': self.ETIQUETA, 'Meditacion': self.MEDITACION, 'Pelea con Armas': self.PARMAS, 'Sigilo': self.SIGILO, 'Supervivencia': self.SUPERVIVENCIA, 'Tecnologia': self.TECNOLOGIA}
        self.dict_conocimientos = {'Academicismo': self.ACADEMICISMO, 'Ciencias': self.CIENCIAS, 'Cosmologia': self.COSMOLOGIA, 'Enigmas': self.ENIGMAS, 'Esoterismo': self.ESOTERISMO, 'Informatica': self.INFORMATICA, 'Investigacion': self.INVESTIGACION, 'Leyes': self.LEYES, 'Medicina': self.MEDICINA, 'Ocultismo': self.OCULTISMO, 'Politica': self.POLITICA}
        self.talentos = [self.ALERTA, self.ARTE, self.ATLETISMO, self.CALLEJEO, self.CONSCIENCIA, self.EMPATIA, self.EXPRESION, self.INTIMIDACION, self.LIDERAZGO, self.PELEA, self.SUBTERFUGIO]
        self.tecnicas = [self.AFUEGO, self.AMARCIALES, self.ARTESANIA, self.CONDUCIR, self.DOCUMENTACION, self.ETIQUETA, self.MEDITACION, self.PARMAS, self.SIGILO, self.SUPERVIVENCIA, self.TECNOLOGIA]
        self.conocimientos = [self.ACADEMICISMO, self.CIENCIAS, self.COSMOLOGIA, self.ENIGMAS, self.ESOTERISMO, self.INFORMATICA, self.INVESTIGACION, self.LEYES, self.MEDICINA, self.OCULTISMO, self.POLITICA]
        
        # en este fragmento vamos a comprobar que se cumplan las condiciones que nos pide la ficha respecto habilidades
        if sum(self.talentos) != 13 and sum(self.talentos) != 9 and sum(self.talentos) != 5:
        #    print('En la categoría "Talentos" no has sumado 5, 9 ni 13 puntos. Corrige este error o activa el modo máster.')
            self.error = True
        if sum(self.conocimientos) != 13 and sum(self.conocimientos) != 9 and sum(self.conocimientos) != 5:
        #    print('En la categoría "Conocimientos" no has sumado 5, 9 ni 13 puntos. Corrige este error o activa el modo máster.')
            self.error = True
        if sum(self.tecnicas) != 13 and sum(self.tecnicas) != 9 and sum(self.tecnicas) != 5:
        #    print('En la categoría "Tecnicas" no has sumado 5, 9 ni 13 puntos. Corrige este error o activa el modo máster.')
            self.error = True
        if sum(self.talentos) == sum(self.conocimientos):
        #    print('Talentos y conocimientos tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.')
            self.error = True
        elif sum(self.talentos) == sum(self.tecnicas):
        #    print('Talentos y técnicas tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.')
            self.error = True
        elif sum(self.conocimientos) == sum(self.tecnicas):
        #    print('Conocimientos y técnicas tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.')
            self.error = True
        
        # esto es para reproducir la suma de cada una de las categorías de las habilidades
        self.lbl_talentos.setText(str(sum(self.talentos)))
        self.lbl_tecnicas.setText(str(sum(self.tecnicas)))
        self.lbl_conocimientos.setText(str(sum(self.conocimientos)))


        
        # Esferas
        self.CARDINAL = self.spinCardinal.value()
        self.CORRESPONDENCIA = self.spinCorrespondencia.value()
        self.ENTROPIA = self.spinEntropia.value()
        self.ESPIRITU = self.spinEspiritu.value()
        self.FUERZAS = self.spinFuerzas.value()
        self.MATERIA = self.spinMateria.value()
        self.MENTE = self.spinMente.value()
        self.TIEMPO = self.spinTiempo.value()
        self.VIDA = self.spinVida.value()
        self.esferas = [self.CARDINAL, self.CORRESPONDENCIA, self.ENTROPIA, self.ESPIRITU, self.FUERZAS, self.MATERIA, self.MENTE, self.TIEMPO, self.VIDA]
        self.Tesferas = ['Cardinal', 'Correspondencia', 'Entropia', 'Espiritu', 'Fuerzas', 'Materia', 'Mente', 'Tiempo', 'Vida']
        self.dict_esferas = dict(zip(self.Tesferas, self.esferas))
        
        # esfera afín
        if self.rdbtn_cardinal.isChecked():
            self.afin = self.Tesferas[0]
        elif self.rdbtn_correspondencia.isChecked():
            self.afin = self.Tesferas[1]
        elif self.rdbtn_entropia.isChecked():
            self.afin = self.Tesferas[2]
        elif self.rdbtn_espiritu.isChecked():
            self.afin = self.Tesferas[3]
        elif self.rdbtn_fuerzas.isChecked():
            self.afin = self.Tesferas[4]
        elif self.rdbtn_materia.isChecked():
            self.afin = self.Tesferas[5]
        elif self.rdbtn_mente.isChecked():
            self.afin = self.Tesferas[6]
        elif self.rdbtn_tiempo.isChecked():
            self.afin = self.Tesferas[7]
        elif self.rdbtn_vida.isChecked():
            self.afin = self.Tesferas[8]
        
        # ultimas características
        self.ARETE = self.spinArete.value()
        self.VOLUNTAD = self.spinVoluntad.value()
        self.QUINTAESENCIA = self.spinQuintaesencia.value()
        self.PARADOJA = self.spinParadoja.value()
        self.caracteristicas = [self.ARETE, self.VOLUNTAD, self.QUINTAESENCIA, self.PARADOJA]
        self.Tcaracteristicas = ['Arete', 'Voluntad', 'Quintaesencia', 'Paradoja']
        self.dict_caracteristicas = dict(zip(self.Tcaracteristicas, self.caracteristicas))

            





app = QApplication(sys.argv)
miVentana = FichaMago()
miVentana.show()
app.exec_()