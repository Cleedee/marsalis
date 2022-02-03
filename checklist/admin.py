from django.contrib import admin
from checklist.models import Node, NodeRaiz, NodePergunta, Problema

	
class NodeAdmin(admin.ModelAdmin):
	pass
	
class NodeRaizAdmin(admin.ModelAdmin):
	pass
	
class NodePerguntaAdmin(admin.ModelAdmin):
	pass
	
class ProblemaAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Node, NodeAdmin)
admin.site.register(NodeRaiz, NodeRaizAdmin)
admin.site.register(NodePergunta, NodePerguntaAdmin)
admin.site.register(Problema, ProblemaAdmin)
