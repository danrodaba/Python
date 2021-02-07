import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from accesobd import AccesoBD



class FichaMago(QMainWindow):
    error = False
    
    trasfondos = ['-', 'Aliados', 'Arcano', 'Armamento Secreto', 'Avatar', 'Bendición', 'Biblioteca', 'Capilla', 'Certificación', 'Contactos', 'Criados', 'Culto', 'Destino', 'Espías', 'Estatus', 'Fama', 'Familiar', 'Heredad', 'Identidad Alternativa', 'Influencia', 'Leyenda', 'Maravilla', 'Mejora $', 'Mentor', 'Nodo', 'Patrón', 'Rango', 'Recursos', 'Refuerzos', 'Requerimientos *', 'Sanctum', 'Sueño ', 'Tótem $', 'Vidas Pasadas']
    meritos = ['-', 'Idioma', 'Sentidos Agudos', 'Lazos', 'Tríada Oscura', 'Guardián de la Tormenta', 'Afinidad Umbral', 'Berserker', 'Demasiado Duro para morir', 'Fe verdadera']
    defectos = ['-', 'Adicción', 'Ataismo por Estrés', 'Maldito', 'Ecos', 'Enemigo', 'Constructo', 'TEPD', 'Trastornado', ]

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('mago.ui', self)
        # Este mismo botón hará cosas distintas dependiendo de si estams en la fase de puntos gratuitos.
        # La función de cálculo de gratuitos usará los puntos previos al uso de los puntos gratuitos (self.Pprevios)
        self.gratuitos = 15
        self.fasegratuitos = 0
        if self.fasegratuitos == 0:
            self.btn_crear.clicked.connect(self.datos_ficha)
            self.btn_crear.clicked.connect(self.crear_ficha)
        else:
            self.btn_crear.clicked.connect(self.calculo_gratuitos(self.Pprevios))
        self.errores = []
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
        self.spinCardinal.valueChanged.connect(self.datos_ficha)
        self.spinCorrespondencia.valueChanged.connect(self.datos_ficha)
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

        self.master_modo.stateChanged.connect(self.datos_ficha)
        try:
            self.gratuitos2 = self.gratuitos - self.PG_Atributo * self.incrementos[0] - self.PG_Habilidad * self.incrementos[1] - self.PG_Trasfondo * self.incrementos[2] - self.PG_Esfera * self.incrementos[3] - self.PG_Arete * self.incrementos[4] - self.PG_Voluntad * self.incrementos[5] - self.PG_Quintaesencia * self.incrementos[6] - self.incrementos[7] + self.incrementos[8]
            self.label_75.setText(str(self.gratuitos2))
        except:
            self.label_75.setText(str(self.gratuitos))

    def calculo_gratuitos(datos_entrada):
        # los puntos gratuítos que tengamos serán:
        self.gratuitos -= sum(self.Pmeritos) + sum(self.Pdefectos)
        # 0 atributos, 1 habilidades, 2 trasfondos, 3 esferas, 4 areté, 5 voluntad y 6 quintaesencia.
        self.Pfinal = [sum(self.fisicos) + sum(self.sociales) + sum(self.mentales), sum(self.talentos) + sum(self.tecnicas) + sum(self.conocimientos), self.Ptrasfondo, sum(self.esferas), self.VOLUNTAD, self.QUINTAESENCIA ]
        self.incrementos = [self.Pfinal[0] - datos_entrada[0], self.Pfinal[1] - datos_entrada[1], self.Pfinal[2] - datos_entrada[2], self.Pfinal[3] - datos_entrada[3], self.Pfinal[4] - datos_entrada[4], self.Pfinal[5] - datos_entrada[5], self.Pfinal[6] - datos_entrada[6]]

        # y se gastarán a razón de:
        self.PG_Atributo = 5
        self.PG_Habilidad = 2
        self.PG_Trasfondo = 1
        self.PG_Esfera = 7
        self.PG_Arete = 4  # max = 3
        self.PG_Voluntad = 1
        self.PG_Quintaesencia = 4

        # y ya puedo calcular el número de puntos gratuitos
        self.gratuitos -= (self.incrementos[0] * self.PG_Atributo + self.incrementos[1] * self.PG_Habilidad + self.incrementos[2] * self.PG_Trasfondo + self.incrementos[3] * self.PG_Esfera + self.incrementos[4] * self.PG_Arete + self.incrementos[5] * self.PG_Voluntad + self.incrementos[6] * self.PG_Quintaesencia)
        return self.gratuitos

    def datos_ficha(self):
        # este primer condicional de los errores es porque por la estructura del error de la esfera afín, esta mierda hacía algo muy chungo
        # Soy novato, asúmelo
        if 'Selecciona una esfera afín.' in self.errores:
            self.errores.remove('Selecciona una esfera afín.')
        if self.master_modo.isChecked() is True:
            self.btn_crear.setText('Crear Ficha')
        elif self.master_modo.isChecked() is False:
            self.btn_crear.setText('Puntos Gratuitos')

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
            self.spinCardinal.setValue(1)
        elif self.rdbtn_correspondencia.isChecked():
            self.afin = self.Tesferas[1]
            self.spinCorrespondencia.setValue(1)
        elif self.rdbtn_entropia.isChecked():
            self.afin = self.Tesferas[2]
            self.spinEntropia.setValue(1)
        elif self.rdbtn_espiritu.isChecked():
            self.afin = self.Tesferas[3]
            self.spinEspiritu.setValue(1)
        elif self.rdbtn_fuerzas.isChecked():
            self.afin = self.Tesferas[4]
            self.spinFuerzas.setValue(1)            # Si cambio de esfera afín, debe volver a 0
        elif self.rdbtn_materia.isChecked():
            self.afin = self.Tesferas[5]
            self.spinMateria.setValue(1)
        elif self.rdbtn_mente.isChecked():
            self.afin = self.Tesferas[6]
            self.spinMente.setValue(1)
        elif self.rdbtn_tiempo.isChecked():
            self.afin = self.Tesferas[7]
            self.spinTiempo.setValue(1)
        elif self.rdbtn_vida.isChecked():
            self.afin = self.Tesferas[8]
            self.spinVida.setValue(1)
        else:
            self.fallo = 'Selecciona una esfera afín.'
            self.error = True
            if self.fallo not in self.errores:
                self.errores.append(self.fallo)
            self.afin = '-'
        
        # self.label_75.setText(str(self.gratuitos))
        
        # ultimas características
        self.ARETE = self.spinArete.value()
        self.VOLUNTAD = self.spinVoluntad.value()
        self.QUINTAESENCIA = self.spinQuintaesencia.value()
        self.PARADOJA = self.spinParadoja.value()
        self.caracteristicas = [self.ARETE, self.VOLUNTAD, self.QUINTAESENCIA, self.PARADOJA]
        self.Tcaracteristicas = ['Arete', 'Voluntad', 'Quintaesencia', 'Paradoja']
        self.dict_caracteristicas = dict(zip(self.Tcaracteristicas, self.caracteristicas))
        if self.ARETE > 3:
            self.fallo = 'El Areté no puede ser mayor de 3.'
            self.error = True
            self.errores.append(self.fallo)

        # Captamos la lista de meritos.

        self.dict_trasfondos = {'Trasfondo' : self.Trasfondos.currentText(), 'Ptrasfondo': self.spinTrasfondo.value(), 'Trasfondo_2' : self.Trasfondos_2.currentText(), 'Ptrasfondo_2': self.spinTrasfondo_2.value(), 'Trasfondo_3' : self.Trasfondos_3.currentText(), 'Ptrasfondo_3': self.spinTrasfondo_3.value(), 'Trasfondo_4' : self.Trasfondos_4.currentText(), 'Ptrasfondo_4': self.spinTrasfondo_4.value(), 'Trasfondo_5' : self.Trasfondos_5.currentText(), 'Ptrasfondo_5': self.spinTrasfondo_5.value(), 'Trasfondo_6' : self.Trasfondo_libre.text(), 'Ptrasfondo_6': self.spinTrasfondo_6.value()}
        self.dict_meritos = {'merito' : self.Meritos.currentText(), 'Pmerito': self.spinMeritos.value(), 'merito_2' : self.Meritos_2.currentText(), 'Pmerito_2': self.spinMeritos_2.value(), 'merito_3' : self.Meritos_3.currentText(), 'Pmerito_3': self.spinMeritos_3.value(), 'merito_4' : self.Meritos_4.currentText(), 'Pmerito_4': self.spinMeritos_4.value(), 'merito_5' : self.Meritos_5.currentText(), 'Pmerito_5': self.spinMeritos_5.value(), 'merito_6' : self.Merito_libre.text(), 'Pmerito_6': self.spinMeritos_6.value()}
        self.dict_defectos = {'defecto' : self.Defectos.currentText(), 'Pdefecto': self.spinDefectos.value(), 'defecto_2' : self.Defectos_2.currentText(), 'Pdefecto_2': self.spinDefectos_2.value(), 'defecto_3' : self.Defectos_3.currentText(), 'Pdefecto_3': self.spinDefectos_3.value(), 'defecto_4' : self.Defectos_4.currentText(), 'Pdefecto_4': self.spinDefectos_4.value(), 'defecto_5' : self.Defectos_5.currentText(), 'Pdefecto_5': self.spinDefectos_5.value(), 'defecto_6' : self.Defecto_libre.text(), 'Pdefecto_6': self.spinDefectos_6.value()}
        self.Pmeritos = [self.spinMeritos.value(), self.spinMeritos_2.value(), self.spinMeritos_3.value(), self.spinMeritos_4.value(), self.spinMeritos_5.value(), self.spinMeritos_6.value()]
        self.Pdefectos = [self.spinDefectos.value(), self.spinDefectos_2.value(), self.spinDefectos_3.value(), self.spinDefectos_4.value(), self.spinDefectos_5.value(), self.spinDefectos_6.value(), ]
        self.Ptrasfondos = [self.spinTrasfondo.value(), self.spinTrasfondo_2.value(), self.spinTrasfondo_3.value(), self.spinTrasfondo_4.value(), self.spinTrasfondo_5.value(), self.spinTrasfondo_6.value()]

    
    def crear_ficha(self):
        # Ahora se agrupan en distintas listas y diccionarios
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
        self.dict_tecnicas = {'Armas_fuego': self.AFUEGO, 'Artes_Marciales': self.AMARCIALES, 'Artesania': self.ARTESANIA, 'Conducir': self.CONDUCIR, 'Documentación': self.DOCUMENTACION, 'Etiqueta': self.ETIQUETA, 'Meditacion': self.MEDITACION, 'Pelea_Armas': self.PARMAS, 'Sigilo': self.SIGILO, 'Supervivencia': self.SUPERVIVENCIA, 'Tecnologia': self.TECNOLOGIA}
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
        # Con todos los datos reunidos en los diferentes diccionarios, creamos un macro diccionario que usaremos para hacer la inyección
        self.dict_final = {}
        self.dict_final.update(self.dict_identificacion)
        self.dict_final.update({'Esfera_afin': self.afin})
        self.dict_final.update(self.dict_fisicos)
        self.dict_final.update(self.dict_sociales)
        self.dict_final.update(self.dict_mentales)
        self.dict_final.update(self.dict_talentos)
        self.dict_final.update(self.dict_tecnicas)
        self.dict_final.update(self.dict_conocimientos)
        self.dict_final.update(self.dict_esferas)
        self.dict_final.update(self.dict_caracteristicas)
        self.dict_final.update(self.dict_trasfondos)
        self.dict_final.update(self.dict_meritos)
        self.dict_final.update(self.dict_defectos)

        # ahora vamos a comprobar si hay errores y en función de ello, dar un mensaje o inyectar a la base de datos
        if self.fasegratuitos == 0: # para saber si ya estamos en la fase de puntos gratuítos. Si es así, se saltarán estos mensajes y se hará uno nuevo
            if self.errores != [] and self.master_modo.isChecked() is False:
                self.errores_text = ''
                mensaje = QMessageBox()
                mensaje.setIcon(QMessageBox.Critical)
                for i in self.errores:
                    self.errores_text += '-' + i + '\n'
                mensaje.setText(self.errores_text)
                mensaje.setWindowTitle("Errores")
                mensaje.setStandardButtons(QMessageBox.Ok)
                retval = mensaje.exec_()
        
            # Ahora, si todo está correcto, pasamos a usar los puntos gratuitos.
            elif self.errores == [] and self.master_modo.isChecked() is False:
                self.fasegratuitos = 1
                # comprobamos los puntos actuales a cada categoría para saber en donde los hemos subido.
                # los puntos actuales son: 0 atributos, 1 habilidades, 2 trasfondos, 3 esferas, 4 areté, 5 voluntad y 6 quintaesencia.
                self.datos_entrada = [sum(self.fisicos) + sum(self.sociales) + sum(self.mentales), sum(self.talentos) + sum(self.tecnicas) + sum(self.conocimientos), sum(self.Ptrasfondos), sum(self.esferas), self.ARETE, self.VOLUNTAD, self.QUINTAESENCIA, sum(self.Pmeritos), sum(self.Pdefectos)]
                self.btn_crear.setText('Crear Ficha')
                self.gratuitos -= sum(self.Pmeritos) + sum(self.Pdefectos)
                # 0 atributos, 1 habilidades, 2 trasfondos, 3 esferas, 4 areté, 5 voluntad y 6 quintaesencia.

            

            self.errores = []
            # -----------
            # los puntos gratuítos que tengamos serán:

        # y se gastarán a razón de:
        self.PG_Atributo = 5
        self.PG_Habilidad = 2
        self.PG_Trasfondo = 1
        self.PG_Esfera = 7
        self.PG_Arete = 4
        self.PG_Voluntad = 1
        self.PG_Quintaesencia = 4
        self.Pfinal = [sum(self.fisicos) + sum(self.sociales) + sum(self.mentales), sum(self.talentos) + sum(self.tecnicas) + sum(self.conocimientos), sum(self.Ptrasfondos), sum(self.esferas), self.ARETE, self.VOLUNTAD, self.QUINTAESENCIA, sum(self.Pmeritos), sum(self.Pdefectos)]
        self.incrementos = [self.Pfinal[0] - self.datos_entrada[0], self.Pfinal[1] - self.datos_entrada[1], self.Pfinal[2] - self.datos_entrada[2], self.Pfinal[3] - self.datos_entrada[3], self.Pfinal[4] - self.datos_entrada[4], self.Pfinal[5] - self.datos_entrada[5], self.Pfinal[6] - self.datos_entrada[6], self.Pfinal[7] - self.datos_entrada[7], self.Pfinal[8] - self.datos_entrada[8]]
        
        self.gratuitos2 = self.gratuitos - self.PG_Atributo * self.incrementos[0] - self.PG_Habilidad * self.incrementos[1] - self.PG_Trasfondo * self.incrementos[2] - self.PG_Esfera * self.incrementos[3] - self.PG_Arete * self.incrementos[4] - self.PG_Voluntad * self.incrementos[5] - self.PG_Quintaesencia * self.incrementos[6] - self.incrementos[7] + self.incrementos[8]
        print(self.incrementos)
        print(self.gratuitos2)

        if self.gratuitos == 0:
            print(self.incrementos)
        


            
        SQL_inyeccion = 'insert into fichas ('




            

if __name__=="__main__":
    #Instancia para iniciar una aplicación    
    app = QApplication(sys.argv)
    #Crear un objeto de la clase
    VentanaMago = FichaMago()
    #Mostrar la ventana
    VentanaMago.show()
    #Ejecutar la aplicación
    app.exec_()
    #Estas últias 4 sentencias, lanzan la aplicación. El if evita que se abra en caso de que no sea la principal.