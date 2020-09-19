from django.forms import ModelForm
from .models import Communication

class CommunicationForm(ModelForm):
  class Meta:
    model = Communication
    fields = ['date', 'contact_method']