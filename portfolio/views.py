from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.views.generic import FormView
from django.views.generic.edit import FormMixin
from django.core.mail import send_mail, BadHeaderError
#from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render ,redirect
from .forms import ContactForm
#from core.settings import EMAIL_HOST_USER
# Create your views here.


class PageView(View):
    template_name = 'index.html'
    form_class = ContactForm

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name, {'form':self.form_class})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            from_email = form.cleaned_data['Email']
            subject = form.cleaned_data['Subject']
            message = form.cleaned_data['Message']

            try:
                #instead of admin@gmail.com you should put gmail of client

                send_mail(subject,message,from_email,to=['admin@gmail.com'])

            except:

                return HttpResponse("Invalid header Found!")

            return redirect('main:success')

        return render(request, self.template_name, {'form':self.form_class})

class SuccessView(TemplateView):
    template_name = 'success.html'
