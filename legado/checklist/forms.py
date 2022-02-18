from django import forms
from servico.models import Produto

class NodeRaizForm(forms.Form):
	problema_id = forms.CharField(widget=forms.HiddenInput)
	pergunta = forms.CharField(widget=forms.Textarea)
	
class RoteiroForm(forms.Form):
	pai_id = forms.CharField(widget=forms.HiddenInput)
	resposta  = forms.CharField(widget=forms.HiddenInput)
	privativo = forms.CharField(widget=forms.CheckboxInput)
	texto = forms.CharField(widget=forms.Textarea)
	
class PerguntaForm(forms.Form):
	checklist_id = forms.CharField(widget=forms.HiddenInput)
	pergunta = forms.CharField(widget=forms.Textarea)