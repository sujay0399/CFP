from django.forms import ModelForm
from .models import Proposal

class ProposalForm(ModelForm):
    class Meta:
        model = Proposal
        fields = ['name', 'outline', 'pitch', 'talktime']
