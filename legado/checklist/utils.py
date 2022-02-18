from checklist.models import CheckList

def criar_folhas():
	sim = CheckList()
	sim.tipo = CheckList.TIPO_TECNICO
	sim.save()
	nao = CheckList()
	nao.tipo = CheckList.TIPO_TECNICO
	nao.save()
	return sim, nao