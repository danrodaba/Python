import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from accesobd import AccesoBD



class FichaMago(QMainWindow):
    error = False
    gratuitos = 15
    trasfondos = ['-', 'Aliados', 'Arcano', 'Armamento Secreto', 'Avatar', 'Bendición', 'Biblioteca', 'Capilla', 'Certificación', 'Contactos', 'Criados', 'Culto', 'Destino', 'Espías', 'Estatus', 'Fama', 'Familiar', 'Heredad', 'Identidad Alternativa', 'Influencia', 'Leyenda', 'Maravilla', 'Mejora $', 'Mentor', 'Nodo', 'Patrón', 'Rango', 'Recursos', 'Refuerzos', 'Requerimientos *', 'Sanctum', 'Sueño ', 'Tótem $', 'Vidas Pasadas']
    meritos = ['-', 'Idioma', 'Sentidos Agudos', 'Lazos', 'Tríada Oscura', 'Guardián de la Tormenta', 'Afinidad Umbral', 'Berserker', 'Demasiado Duro para morir', 'Fe verdadera']
    defectos = ['-', 'Adicción', 'Ataismo por Estrés', 'Maldito', 'Ecos', 'Enemigo', 'Constructo', 'TEPD', 'Trastornado', ]

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('mago.ui', self)
        self.btn_crear.clicked.connect(self.crear_ficha)

        self.Trasfondos.addItems(self.trasfondos)
        self.Trasfondos_2.addItems(self.trasfondos)
        self.Trasfondos_3.addItems(self.trasfondos)
        self.Trasfondos_4.addItems(self.trasfondos)
        self.Trasfondos_5.addItems(self.trasfondos)
        self.Meritos.addItems(self.meritos)
        self.Meritos_2.addItems(self.meritos)
        self.Meritos_3.addItems(self.meritos)
        self.Meritos_4.addItems(self.meritos)
        self.Meritos_5.addItems(self.meritos)
        self.Defectos.addItems(self.defectos)
        self.Defectos_2.addItems(self.defectos)
        self.Defectos_3.addItems(self.defectos)
        self.Defectos_4.addItems(self.defectos)
        self.Defectos_5.addItems(self.defectos)

        # identificación
        self.nombre.textChanged.connect(self.datos_ficha)
        self.jugador.textChanged.connect(self.datos_ficha)
        self.cronica.textChanged.connect(self.datos_ficha)
        self.naturaleza.textChanged.connect(self.datos_ficha)
        self.conducta.textChanged.connect(self.datos_ficha)
        self.esencia.textChanged.connect(self.datos_ficha)
        self.afiliacion.textChanged.connect(self.datos_ficha)
        self.secta.textChanged.connect(self.datos_ficha)
        self.concepto.textChanged.connect(self.datos_ficha)
        
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

        # Radiobutton de esfera afín
        self.rdbtn_cardinal.toggled.connect(self.datos_ficha)
        self.rdbtn_correspondencia.toggled.connect(self.datos_ficha)
        self.rdbtn_entropia.toggled.connect(self.datos_ficha)
        self.rdbtn_espiritu.toggled.connect(self.datos_ficha)
        self.rdbtn_fuerzas.toggled.connect(self.datos_ficha)
        self.rdbtn_materia.toggled.connect(self.datos_ficha)
        self.rdbtn_mente.toggled.connect(self.datos_ficha)
        self.rdbtn_tiempo.toggled.connect(self.datos_ficha)
        self.rdbtn_vida.toggled.connect(self.datos_ficha)

        # esferas
        self.spinEntropia.valueChanged.connect(self.datos_ficha)
        self.spinEspiritu.valueChanged.connect(self.datos_ficha)
        self.spinFuerzas.valueChanged.connect(self.datos_ficha)
        self.spinMateria.valueChanged.connect(self.datos_ficha)
        self.spinMente.valueChanged.connect(self.datos_ficha)
        self.spinTiempo.valueChanged.connect(self.datos_ficha)
        self.spinVida.valueChanged.connect(self.datos_ficha)

        # trasfondos
        self.Trasfondos.activated.connect(self.datos_ficha)
        self.Trasfondos_2.activated.connect(self.datos_ficha)
        self.Trasfondos_3.activated.connect(self.datos_ficha)
        self.Trasfondos_4.activated.connect(self.datos_ficha)
        self.Trasfondos_5.activated.connect(self.datos_ficha)
        self.Trasfondo_libre.textChanged.connect(self.datos_ficha)

        self.spinTrasfondo.valueChanged.connect(self.datos_ficha)
        self.spinTrasfondo_2.valueChanged.connect(self.datos_ficha)
        self.spinTrasfondo_3.valueChanged.connect(self.datos_ficha)
        self.spinTrasfondo_4.valueChanged.connect(self.datos_ficha)
        self.spinTrasfondo_5.valueChanged.connect(self.datos_ficha)
        self.spinTrasfondo_6.valueChanged.connect(self.datos_ficha)

        # méritos
        self.Meritos.activated.connect(self.datos_ficha)
        self.Meritos_2.activated.connect(self.datos_ficha)
        self.Meritos_3.activated.connect(self.datos_ficha)
        self.Meritos_4.activated.connect(self.datos_ficha)
        self.Meritos_5.activated.connect(self.datos_ficha)
        self.Merito_libre.textChanged.connect(self.datos_ficha)

        self.spinMeritos.valueChanged.connect(self.datos_ficha)
        self.spinMeritos_2.valueChanged.connect(self.datos_ficha)
        self.spinMeritos_3.valueChanged.connect(self.datos_ficha)
        self.spinMeritos_4.valueChanged.connect(self.datos_ficha)
        self.spinMeritos_5.valueChanged.connect(self.datos_ficha)
        self.spinMeritos_6.valueChanged.connect(self.datos_ficha)

        # defectos
        self.Defectos.activated.connect(self.datos_ficha)
        self.Defectos_2.activated.connect(self.datos_ficha)
        self.Defectos_3.activated.connect(self.datos_ficha)
        self.Defectos_4.activated.connect(self.datos_ficha)
        self.Defectos_5.activated.connect(self.datos_ficha)
        self.Defecto_libre.textChanged.connect(self.datos_ficha)

        self.spinDefectos.valueChanged.connect(self.datos_ficha)
        self.spinDefectos_2.valueChanged.connect(self.datos_ficha)
        self.spinDefectos_3.valueChanged.connect(self.datos_ficha)
        self.spinDefectos_4.valueChanged.connect(self.datos_ficha)
        self.spinDefectos_5.valueChanged.connect(self.datos_ficha)
        self.spinDefectos_6.valueChanged.connect(self.datos_ficha)


    def gratuitos(self):
        self.PG_Atributo = 5
        self.PG_Habilidad = 2
        self.PG_Trasfondo = 1
        self.PG_Esfera = 7
        self.PG_Arete = 4 # max = 3
        self.PG_Voluntad = 1
        self.PG_Quintaesencia = 4
        self.PG_Merito
        self.PG_Defecto

    def is_list_empty(list):
        # returning boolean value of current list
        # empty list bool value is False
        # non-empty list boolea value is True
        return not bool(list)
  

    def datos_ficha(self):
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

        # Captamos la lista de meritos.

        self.dict_trasfondos = {self.Trasfondos.currentText(): self.spinTrasfondo.value(), self.Trasfondos_2.currentText(): self.spinTrasfondo_2.value(), self.Trasfondos_3.currentText(): self.spinTrasfondo_3.value(), self.Trasfondos_4.currentText(): self.spinTrasfondo_4.value(), self.Trasfondos_5.currentText(): self.spinTrasfondo_5.value(), self.Trasfondo_libre.text(): self.spinTrasfondo_6.value()}
        self.Ptrasfondos = sum(self.dict_trasfondos.values())


    def crear_ficha(self):
    #if self.master_modo.isChecked() is False:
        self.errores = []
        #Ahora se agrupan en distintas listas y diccionarios
        self.dict_identificacion = {'Nombre': self.NOMBRE, 'Jugador': self.JUGADOR, 'Crónica': self.CRONICA, 'Naturaleza': self.NATURALEZA, 'Conducta': self.CONDUCTA, 'Esencia': self.ESENCIA, 'Afiliación': self.AFILIACION, 'Secta': self.SECTA, 'Concepto': self.CONCEPTO}
        self.identificacion = [self.NOMBRE, self.JUGADOR, self.CRONICA, self.NATURALEZA, self.CONDUCTA, self.ESENCIA, self.AFILIACION, self.SECTA, self.CONCEPTO]
        self.fisicos = [self.FUERZA, self.DESTREZA, self.RESISTENCIA]
        self.sociales = [self.CARISMA, self.MANIPULACION, self.APARIENCIA]
        self.mentales = [self.PERCEPCION, self.INTELIGENCIA, self.ASTUCIA]
        self.dict_fisicos = {'Fuerza' : self.FUERZA , 'Destreza' : self.DESTREZA, 'Resistencia' : self.RESISTENCIA}
        self.dict_sociales = {'Carisma' : self.CARISMA , 'Manipulación' : self.MANIPULACION, 'Apariencia' : self.APARIENCIA}
        self.dict_mentales = {'Percepcion' : self.PERCEPCION , 'Inteligencia' : self.INTELIGENCIA, 'Astucia' : self.ASTUCIA}
        # en este fragmento vamos a comprobar que se cumplan las condiciones que nos pide la ficha respecto atributos
        if sum(self.fisicos) != 10 and sum(self.fisicos) != 8 and sum(self.fisicos) != 6:
            self.fallo = 'En la categoría "Físicos" no has sumado 3, 5 ni 7 puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
        if sum(self.sociales) != 10 and sum(self.sociales) != 8 and sum(self.sociales) != 6:
            self.fallo = 'En la categoría "Sociales" no has sumado 3, 5 ni 7 puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
        if sum(self.mentales) != 10 and sum(self.mentales) != 8 and sum(self.mentales) != 6:
            self.fallo = 'En la categoría "Mentales" no has sumado 3, 5 ni 7 puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
        if sum(self.sociales) == sum(self.fisicos):
            self.fallo = 'Sociales y físicos tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
        elif sum(self.mentales) == sum(self.fisicos):
            self.fallo = 'Mentales y físicos tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
        elif sum(self.mentales) == sum(self.sociales):
            self.fallo = 'Mentales y sociales tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
        # los declaro como diccionarios y listas.
        self.dict_talentos = {'Alerta': self.ALERTA, 'Arte': self.ARTE, 'Atletismo': self.ATLETISMO, 'Callejeo': self.CALLEJEO, 'Consciencia': self.CONSCIENCIA, 'Empatia': self.EMPATIA, 'Expresión': self.EXPRESION,  'Intimidacion': self.INTIMIDACION, 'Liderazgo': self.LIDERAZGO, 'Pelea': self.PELEA, 'Subterfugio': self.SUBTERFUGIO}
        self.dict_tecnicas = {'Armas de fuego': self.AFUEGO, 'Artes Marciales': self.AMARCIALES, 'Artesania': self.ARTESANIA, 'Conducir': self.CONDUCIR, 'Documentación': self.DOCUMENTACION, 'Etiqueta': self.ETIQUETA, 'Meditacion': self.MEDITACION, 'Pelea con Armas': self.PARMAS, 'Sigilo': self.SIGILO, 'Supervivencia': self.SUPERVIVENCIA, 'Tecnologia': self.TECNOLOGIA}
        self.dict_conocimientos = {'Academicismo': self.ACADEMICISMO, 'Ciencias': self.CIENCIAS, 'Cosmologia': self.COSMOLOGIA, 'Enigmas': self.ENIGMAS, 'Esoterismo': self.ESOTERISMO, 'Informatica': self.INFORMATICA, 'Investigacion': self.INVESTIGACION, 'Leyes': self.LEYES, 'Medicina': self.MEDICINA, 'Ocultismo': self.OCULTISMO, 'Politica': self.POLITICA}
        self.talentos = [self.ALERTA, self.ARTE, self.ATLETISMO, self.CALLEJEO, self.CONSCIENCIA, self.EMPATIA, self.EXPRESION, self.INTIMIDACION, self.LIDERAZGO, self.PELEA, self.SUBTERFUGIO]
        self.tecnicas = [self.AFUEGO, self.AMARCIALES, self.ARTESANIA, self.CONDUCIR, self.DOCUMENTACION, self.ETIQUETA, self.MEDITACION, self.PARMAS, self.SIGILO, self.SUPERVIVENCIA, self.TECNOLOGIA]
        self.conocimientos = [self.ACADEMICISMO, self.CIENCIAS, self.COSMOLOGIA, self.ENIGMAS, self.ESOTERISMO, self.INFORMATICA, self.INVESTIGACION, self.LEYES, self.MEDICINA, self.OCULTISMO, self.POLITICA]
        # en este fragmento vamos a comprobar que se cumplan las condiciones que nos pide la ficha respecto habilidades
        if sum(self.talentos) != 13 and sum(self.talentos) != 9 and sum(self.talentos) != 5:
            self.fallo = 'En la categoría "Talentos" no has sumado 5, 9 ni 13 puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
        elif sum(self.conocimientos) != 13 and sum(self.conocimientos) != 9 and sum(self.conocimientos) != 5:
            self.fallo = 'En la categoría "Conocimientos" no has sumado 5, 9 ni 13 puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
        elif sum(self.tecnicas) != 13 and sum(self.tecnicas) != 9 and sum(self.tecnicas) != 5:
            self.fallo = 'En la categoría "Tecnicas" no has sumado 5, 9 ni 13 puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
        if sum(self.talentos) == sum(self.conocimientos):
            self.fallo = 'Talentos y conocimientos tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
        elif sum(self.talentos) == sum(self.tecnicas):
            self.fallo = 'Talentos y técnicas tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
        elif sum(self.conocimientos) == sum(self.tecnicas):
            self.fallo = 'Conocimientos y técnicas tienen asignada la misma cantidad de puntos. Corrige este error o activa el modo máster.'
            self.error = True
            self.errores.append(self.fallo)
            
        # ahora vamos a comprobar si hay errores y en función de ello, dar un mensaje o inyectar a la base de datos
        if self.error is True:
            self.QDialog.warning(self.error)
            self.setFixedSize(400, 200)



app = QApplication(sys.argv)
miVentana = FichaMago()
miVentana.show()
app.exec_()