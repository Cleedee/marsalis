from django import forms

from models import Servico, Ocorrencia

class FormNovoChamado(forms.ModelForm):
	class Meta:
		model = Servico
		exclude = ('cliente','autor','responsavel','status')
		
		
class FormChamado(forms.ModelForm):
	
	class Meta:
		model = Servico


class FormOcorrencia(forms.ModelForm):
	
	servico_id = forms.CharField(widget=forms.HiddenInput)
	
	class Meta:
		model = Ocorrencia
		exclude = ('servico','autor')
		
	def criar_ocorrencia(self):
		pass
		