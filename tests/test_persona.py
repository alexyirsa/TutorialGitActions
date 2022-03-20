import datetime
import unittest

from faker import Faker
from comunidad.base import Session

from comunidad.persona import Persona

class PersonaTestCase(unittest.TestCase):
    
    """def setUp(self):
        self.persona1 = Persona(nombre='Alejandra', edad=25)
        self.persona2 = Persona(nombre='Diego', edad=22)
        self.persona3 = Persona(nombre='Alejandra', edad=25)
        self.persona4 = Persona(nombre='Diana', edad=25)
        self.grupo = [self.persona1, self.persona2, self.persona3]"""
    
    def setUp(self):
        self.data_factory = Faker()
        self.data = [] 
        self.personas = []
        for i in range(0,10):
            self.data.append((self.data_factory.name(), self.data_factory.random_number()))
            self.personas.append(Persona(nombre = self.data[-1][0], edad = self.data[-1][-1]))
        
        
    """def test_constructor(self):
       self.assertEqual(self.persona1.dar_nombre(), 'Alejandra')
       self.assertEqual(self.persona1.dar_edad(), 25)"""
    
    def test_constructor(self):
        for persona, dat in zip(self.personas, self.data):
            self.assertEqual(persona.dar_nombre(), dat[0])
            self.assertEqual(persona.dar_edad(), dat[-1])
    
    def test_prueba(self):
       self.assertEqual(0, 0)
       
    """def test_anio_nacimiento(self):
       self.assertEqual(self.persona1.calcular_anio_nacimiento(True), datetime.datetime.now().year - 25)
       self.assertNotEqual(self.persona1.calcular_anio_nacimiento(False), datetime.datetime.now().year - 25)
       self.assertEqual(self.persona1.calcular_anio_nacimiento(False), datetime.datetime.now().year - 25 + 1)
       self.assertNotEqual(self.persona1.calcular_anio_nacimiento(True), datetime.datetime.now().year - 25 + 1)"""
       
    def test_anio_nacimiento(self):
       for persona, dat in zip(self.personas, self.data):
            self.assertEqual(persona.calcular_anio_nacimiento(True), datetime.datetime.now().year - dat[-1])

    """def test_asignacion(self):
        self.persona2.asignar_edad(28)
        self.persona2.asignar_nombre("Felipe")
        self.assertFalse(self.persona2.dar_nombre()=='Diego')
        self.assertFalse(self.persona2.dar_edad()==22)
        self.assertTrue(self.persona2.dar_nombre()=='Felipe')
        self.assertTrue(self.persona2.dar_edad()==28)"""
        
    def test_asignacion(self):
        original_data = (self.data_factory.name(), self.data_factory.random_number())
        persona_prueba = Persona(nombre = original_data[0], edad = original_data[-1])
        new_data = (self.data_factory.name(), self.data_factory.random_number())
        while new_data[0] == original_data[0] or new_data[-1] == original_data[-1]:
            new_data = (self.data_factory.name(), self.data_factory.random_number())
        persona_prueba.asignar_nombre(new_data[0])
        persona_prueba.asignar_edad(new_data[-1])    
        self.assertFalse(persona_prueba.dar_nombre()==original_data[0])
        self.assertFalse(persona_prueba.dar_edad()==original_data[-1])
        self.assertTrue(persona_prueba.dar_nombre()==new_data[0])
        self.assertTrue(persona_prueba.dar_edad()==new_data[-1])
        
    """def test_objetos_iguales(self):
       persona_nueva = self.persona1
       self.assertIsNot(self.persona1, self.persona3)
       self.assertIs(self.persona1, persona_nueva)"""
       
    def test_objetos_iguales(self):
        persona_nueva = self.personas[-1]
        self.assertIsNot(persona_nueva, self.personas[0])
        self.assertIs(persona_nueva, self.personas[-1])
       
    """def test_elemento_en_conjunto(self):
       self.assertIn(self.persona3, self.grupo)
       self.assertNotIn(self.persona4, self.grupo)"""
       
    def test_elemento_en_conjunto(self):
        original_data = (self.data_factory.name(), self.data_factory.random_number())
        persona_prueba = Persona(nombre = original_data[0], edad = original_data[-1])
        self.assertIn(self.personas[0], self.personas)
        self.assertNotIn(persona_prueba, self.personas)
       
    """def test_instancia_clase(self):
       self.assertIsInstance(self.persona1, Persona)
       self.assertNotIsInstance(self.grupo, Persona)"""
       
    def test_instancia_clase(self):
        self.assertIsInstance(self.personas[0], Persona)
        self.assertNotIsInstance(self.personas, Persona)
       
    """def test_alamacenar(self):
       self.persona1.almacenar()

       session = Session()
       persona = session.query(Persona).filter(Persona.nombre == 'Alejandra' and Persona.edad == 25).first()

       self.assertEqual(persona.dar_nombre(),'Alejandra')
       self.assertEqual(persona.dar_edad(),25)"""
       
    def test_almacenar(self):
        self.personas[0].almacenar()

        session = Session()
        persona = session.query(Persona).filter(Persona.nombre == self.data[0][0] and Persona.edad == self.data[0][1]).first()

        self.assertEqual(persona.dar_nombre(),self.data[0][0])
        self.assertEqual(persona.dar_edad(),self.data[0][-1])

    def test_recuperar(self):
        session = Session()
        session.add(self.personas[0])
        session.commit()
        session.close()

        persona = Persona("",0)
        persona.recuperar(self.data[0][0], self.data[0][-1])

        self.assertEqual(persona.dar_nombre(),self.data[0][0])
        self.assertEqual(persona.dar_edad(),self.data[0][-1])
       
    """def test_recuperar(self):
       session = Session()
       session.add(self.persona2)
       session.commit()
       session.close()

       persona = Persona("",0)
       persona.recuperar("Diego", 22)

       self.assertEqual(persona.dar_nombre(),'Diego')
       self.assertEqual(persona.dar_edad(),22)"""