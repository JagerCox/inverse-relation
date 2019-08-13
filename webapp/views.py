import vobject
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from .forms import ContactForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView


class ContactCreateView(CreateView):
    model = Contact
    success_url = reverse_lazy('success-url')
    form_class = ContactForm


class SuccessTemplateView(TemplateView):
    template_name = "webapp/success.html"


class err404View(TemplateView):
    template_name = "webapp/err404.html"


class err500View(TemplateView):
    template_name = "webapp/err500.html"


def counter_contacts(request):
    counter_contacts = Contact.objects.count()
    if request.user.is_superuser:
        return HttpResponse(counter_contacts)
    else:
        return HttpResponseRedirect('/')


def download_vcard(request):
    if request.user.is_superuser:
        c_a = Contact.objects.all()
        total = ""
        for v in c_a:
            j = vobject.vCard()

            try:
                o = j.add('fn')
                o.value = v.Nombre + " " + v.Apellidos
            except:
                pass

            try:
                o = j.add('n')  # Apellido
                o.value = vobject.vcard.Name(family=v.Apellidos, given=v.Nombre)
            except:
                pass

            try:
                o = j.add('tel')
                o.type_param = "work"
                o.value = str(v.Movil_principal)
            except:
                pass

            try:
                o = j.add('tel')
                o.type_param = "home"
                o.value = str(v.Movil_secundario)
            except:
                pass

            try:
                o = j.add('email')
                o.type_param = 'home'
                o.value = str(v.Email_principal)
            except:
                pass

            try:
                o = j.add('email')
                o.type_param = 'work'
                o.value = str(v.Email_secundario)
            except:
                pass

            try:
                o = j.add('bday')
                o.value = str(v.Fecha_de_nacimiento)
            except:
                pass

            try:
                o = j.add('adr')
                o.type_param = "home"
                o.value = vobject.vcard.Address(
                    street=v.Direccion_de_correo_postal_principal or '',
                    city='',
                    region='',
                    code='',
                    country='',
                    box='',
                    extended=''
                )
            except:
                pass

            try:
                o = j.add('adr')
                o.value = vobject.vcard.Address(
                    street=v.Direccion_de_correo_postal_secundaria or '',
                    city='',
                    region='',
                    code='',
                    country='',
                    box='',
                    extended=''
                )
            except:
                pass

            j.add('note')
            note_full = ""

            try:
                note_full += "Tags: " + v.Tags_que_nos_vinculan + "\r\n"
            except:
                pass

            try:
                note_full += "Empresas: " + v.Ultimos_lugares_donde_trabajaste + "\r\n"
            except:
                pass

            try:
                note_full += "Adicional: " + v.Informacion_adicional
            except:
                pass

            j.note.value = note_full

            total += j.serialize()

        filename = "global.vcf"
        response = HttpResponse(total, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        return response
    else:
        return HttpResponseRedirect('/')



