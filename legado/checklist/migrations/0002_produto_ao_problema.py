
from south.db import db
from django.db import models
from checklist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Problema.produto'
        db.add_column('checklist_problema', 'produto', orm['checklist.problema:produto'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Problema.produto'
        db.delete_column('checklist_problema', 'produto_id')
        
    
    
    models = {
        'checklist.node': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'checklist.nodepergunta': {
            'node_nao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lista_nao'", 'to': "orm['checklist.Node']"}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['checklist.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'node_sim': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lista_sim'", 'to': "orm['checklist.Node']"}),
            'pergunta': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'checklist.noderaiz': {
            'node_nao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'nao_lista'", 'to': "orm['checklist.Node']"}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['checklist.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'node_sim': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sim_lista'", 'to': "orm['checklist.Node']"}),
            'pergunta': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'problema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['checklist.Problema']"})
        },
        'checklist.noderoteiro': {
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['checklist.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'privativo': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {})
        },
        'checklist.nodetecnico': {
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['checklist.Node']", 'unique': 'True', 'primary_key': 'True'})
        },
        'checklist.problema': {
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servico.Produto']"})
        },
        'servico.produto': {
            'descricao': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['checklist']
