
from south.db import db
from django.db import models
from checklist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'NodeRoteiro'
        db.create_table('checklist_noderoteiro', (
            ('node_ptr', orm['checklist.NodeRoteiro:node_ptr']),
            ('privativo', orm['checklist.NodeRoteiro:privativo']),
            ('texto', orm['checklist.NodeRoteiro:texto']),
        ))
        db.send_create_signal('checklist', ['NodeRoteiro'])
        
        # Adding model 'Node'
        db.create_table('checklist_node', (
            ('id', orm['checklist.Node:id']),
            ('tipo', orm['checklist.Node:tipo']),
        ))
        db.send_create_signal('checklist', ['Node'])
        
        # Adding model 'NodeRaiz'
        db.create_table('checklist_noderaiz', (
            ('node_ptr', orm['checklist.NodeRaiz:node_ptr']),
            ('problema', orm['checklist.NodeRaiz:problema']),
            ('pergunta', orm['checklist.NodeRaiz:pergunta']),
            ('node_sim', orm['checklist.NodeRaiz:node_sim']),
            ('node_nao', orm['checklist.NodeRaiz:node_nao']),
        ))
        db.send_create_signal('checklist', ['NodeRaiz'])
        
        # Adding model 'NodeTecnico'
        db.create_table('checklist_nodetecnico', (
            ('node_ptr', orm['checklist.NodeTecnico:node_ptr']),
        ))
        db.send_create_signal('checklist', ['NodeTecnico'])
        
        # Adding model 'NodePergunta'
        db.create_table('checklist_nodepergunta', (
            ('node_ptr', orm['checklist.NodePergunta:node_ptr']),
            ('pergunta', orm['checklist.NodePergunta:pergunta']),
            ('node_sim', orm['checklist.NodePergunta:node_sim']),
            ('node_nao', orm['checklist.NodePergunta:node_nao']),
        ))
        db.send_create_signal('checklist', ['NodePergunta'])
        
        # Adding model 'Problema'
        db.create_table('checklist_problema', (
            ('id', orm['checklist.Problema:id']),
            ('descricao', orm['checklist.Problema:descricao']),
        ))
        db.send_create_signal('checklist', ['Problema'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'NodeRoteiro'
        db.delete_table('checklist_noderoteiro')
        
        # Deleting model 'Node'
        db.delete_table('checklist_node')
        
        # Deleting model 'NodeRaiz'
        db.delete_table('checklist_noderaiz')
        
        # Deleting model 'NodeTecnico'
        db.delete_table('checklist_nodetecnico')
        
        # Deleting model 'NodePergunta'
        db.delete_table('checklist_nodepergunta')
        
        # Deleting model 'Problema'
        db.delete_table('checklist_problema')
        
    
    
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['checklist']
