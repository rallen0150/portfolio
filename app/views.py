from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from django.urls import reverse_lazy

from app.forms import ContactForm
from django.core.mail import send_mail
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class ContactMeView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = ContactForm()
        return context

class SendMailView(FormView):
    template_name = 'contact.html'
    success_url = reverse_lazy("index_view")
    form_class = ContactForm

    def form_valid(self, form):
        form.send_email()
        time.sleep(5)
        return super().form_valid(form)
