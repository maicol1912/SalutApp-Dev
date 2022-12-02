from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Tip(models.Model):
    """
    La siguiente tabla se usa para almacenar encuestas que se le hacen 
    a los usuarios de la app acerca de opiniones
    """
    tip_encabezado = models.CharField(max_length=200)
    tip_desc = models.TextField()
    def __str__(self):
        return f"encuesta: {self.encuesta_tipo}"


class Usuario(models.Model):
    """
    La siguiente tabla se usa para almacenar los datos de las personas que 
    se registren en nuestra aplicacion y con estos datos poder desdplegar 
    diferentes herramientas
    """
    usuario_id = models.IntegerField(primary_key=True)
    usuario_nombre = models.CharField(max_length=200)
    usuario_correo = models.EmailField(max_length=300)
    usuario_password = models.CharField(max_length=300)
    usuario_peso = models.IntegerField()
    usuario_altura = models.IntegerField()
    usuario_edad = models.IntegerField()
    usuario_rol = models.CharField(max_length=200)
    usuario_nro_semanas = models.IntegerField()
    usuario_fecha_avance = models.CharField(max_length=200)
    usuario_nro_tarea = models.IntegerField()

    def __str__(self):
        return f"cedula: {self.usuario_id} nombre: {self.usuario_nombre} "


class Meta(models.Model):
    """
    En esta tabla se almacenan los  datos de cada usuario para asi poder
    definir cual es el plan que este debe llevar , relacionada a :model: `database.Usuario`.
    """
    meta_tipo = models.CharField(max_length=200)
    meta_desc = models.TextField()
    meta_peso_ideal = models.FloatField()
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"meta: {self.meta_tipo}"


class Pqr(models.Model):
    """
    En esta tabla se contienen todas las peticiones, quejas, y reclamos,
    relacionada a :model: `database.Usuario`
    """
    pqr_tipo = models.CharField(max_length=200)
    pqr_desc = models.TextField()
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"pqr: {self.pqr_tipo}"


class Especificacion(models.Model):
    """
    En esta tabla se contienen dietas especificas predefinidas para recomendar
    a el usuario dependiendo de sus caracteristicas y esta divida en los 7 dias de la semana
    """
    especificacion_id = models.IntegerField(primary_key=True)
    especificacion_nombre = models.CharField(max_length=200)
    especificacion_recomendacion = models.TextField()
    especificacion_dia_1 = models.TextField()
    especificacion_dia_2 = models.TextField()
    especificacion_dia_3 = models.TextField()
    especificacion_dia_4 = models.TextField()
    especificacion_dia_5 = models.TextField()
    especificacion_dia_6 = models.TextField()
    especificacion_dia_7 = models.TextField()

    def __str__(self):
        return f"especificacion: {self.especificacion_id}"


class Plan(models.Model):
    """
    En esta tabla se contiene la descripcion y una introduccion al plan que el usuario
    va a llevar sin entrar en mucho detalle, relacionada a  :model: `database.Especificacion`
    """
    plan_desc = models.TextField()
    plan_recomendaciones = models.TextField()
    especificacion_id = models.ForeignKey(Especificacion, on_delete=models.CASCADE)
    meta_id = models.ForeignKey(Meta, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"plan: {self.plan_desc}"


class Tarea(models.Model):
    """
    En esta tabla se contiene la confirmacion de los usuarios acerca de la realizacion
    de las actividades asignadas, relacionada a :model: `database.Usuario`
    """
    tarea_id = models.CharField(primary_key=True, max_length=200)
    tarea_check_1 = models.CharField(null=True,max_length=3)
    peso_check_1 = models.IntegerField(null=True)
    tarea_check_2 = models.CharField(null=True,max_length=3)
    peso_check_2 = models.IntegerField(null=True)
    tarea_check_3 = models.CharField(null=True,max_length=3)
    peso_check_3 = models.IntegerField(null=True)
    tarea_check_4 = models.CharField(null=True,max_length=3)
    peso_check_4 = models.IntegerField(null=True)
    especificacion_id = models.ForeignKey(Especificacion, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Tarea: {self.tarea_id}"
