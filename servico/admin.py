from django.contrib import admin
from servico.models import Usuario, Servico, Ocorrencia, Produto

	
class UsuarioAdmin(admin.ModelAdmin):
	pass
	
class ServicoAdmin(admin.ModelAdmin):
	pass

class OcorrenciaAdmin(admin.ModelAdmin):
	pass
	
class ProdutoAdmin(admin.ModelAdmin):
	pass
		
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Ocorrencia, OcorrenciaAdmin)
admin.site.register(Produto, ProdutoAdmin)
