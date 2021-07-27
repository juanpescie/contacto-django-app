from django.db import models

# Create your models here.
# MODELO CIUDAD
class Ciudad(models.Model):
    codigo = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}"

# CHOICES PARA SEXO DE LA PERSONA
generos = [("F", "Femenino"), ("M", "Masculino"), ("X", "Otro")]
# MODELO PERSONA
class Persona(models.Model):
    dni = models.CharField(max_length=11, primary_key=True)
    apellido = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=generos, default="F")
    fechaNacimiento = models.DateField()
    ciudad = models.ForeignKey(Ciudad, null=False, blank=False, on_delete=models.CASCADE)
    

    def nombreCompleto(self):
        return f"{self.apellido}, {self.nombres}"

    def __str__(self):
        return self.nombreCompleto()

# MODELO TELEFONO
class Telefono(models.Model):
    persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    numero = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.numero} ({self.persona})"
# MODELO EMAIL
class Email(models.Model):
    persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.email} ({self.persona})"



