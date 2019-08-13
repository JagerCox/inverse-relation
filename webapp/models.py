from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    Nombre = models.CharField(max_length=25, help_text="Ejemplo: Dario", null=False, blank=False)
    Apellidos = models.CharField(max_length=200, help_text="Ejemplo: García Exposito", null=False, blank=False)
    Fecha_de_nacimiento = models.DateField(help_text="Formato YYYY-MM-DD.  Ejemplos: 1982-06-20 o 1982-12-05    **OPCIONAL", null=True, blank=True)
    Tags_que_nos_vinculan = models.CharField(max_length=512,  help_text="Cuantos más pongas mejor. Ejemplos: Tenerife, Madrid, Congreso, IAC, TLP, Indra, Kreitek, SC, Hacking, Defensa, Aikido",
                             null=False, blank=False)

    Movil_principal = PhoneNumberField(help_text="Ejemplo: +34611111111", null=False, blank=False)
    Movil_secundario = PhoneNumberField(help_text="Ejemplo: +34622222222    **OPTIONAL", null=True, blank=True)

    Email_principal = models.CharField(max_length=250, help_text="Ejemplo: drio@mail.com", null=False, blank=True)
    Email_secundario = models.CharField(max_length=250, help_text="Ejemplo: drio@yahoo.com    **OPCIONAL", null=True, blank=True)

    Direccion_de_correo_postal_principal = models.CharField(max_length=500, null=True, blank=True, help_text="Calle Escudero N13 B4, 28001 Madrid, España    **OPCIONAL")
    Direccion_de_correo_postal_secundaria = models.CharField(max_length=500, null=True, blank=True, help_text="Calle Escudero N13 B4, 28001 Madrid, España    **OPCIONAL")

    Usuario_en_Telegram = models.CharField(max_length=30, null=True, blank=True, help_text="Ejemplo: @drio    **OPCIONAL")
    Usuario_en_Github = models.CharField(max_length=30, null=True, blank=True, help_text="Ejemplo: drio    **OPCIONAL")
    Usuario_en_BitBucket = models.CharField(max_length=30, null=True, blank=True, help_text="Ejemplo: drio    **OPCIONAL")

    Ultimos_lugares_donde_trabajaste = models.CharField(max_length=100, null=True, blank=True, help_text="Pon los tres últimos si se da el caso (incluyendo el actual) Ejemplo: Universidad, Facebook, Inem    **OPCIONAL")

    Informacion_adicional = models.TextField(max_length=500, null=True, blank=True, help_text="¿Donde nos conocimos?¿Qué temas tenemos en común?    **OPCIONAL")

    def __str__(self):
        return 'Nombre/Apellidos({}/{})'.format(self.Nombre, self.Apellidos)
