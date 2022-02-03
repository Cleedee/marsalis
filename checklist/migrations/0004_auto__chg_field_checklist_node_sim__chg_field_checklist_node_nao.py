# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'CheckList.node_sim'
        db.alter_column('checklist_checklist', 'node_sim_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['checklist.CheckList']))

        # Changing field 'CheckList.node_nao'
        db.alter_column('checklist_checklist', 'node_nao_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['checklist.CheckList']))
    
    
    def backwards(self, orm):
        
        # Changing field 'CheckList.node_sim'
        db.alter_column('checklist_checklist', 'node_sim_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['checklist.CheckList']))

        # Changing field 'CheckList.node_nao'
        db.alter_column('checklist_checklist', 'node_nao_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['checklist.CheckList']))
    
    
    models = {
        'checklist.checklist': {
            'Meta': {'object_name': 'CheckList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node_nao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lista_nao'", 'null': 'True', 'to': "orm['checklist.CheckList']"}),
            'node_sim': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lista_sim'", 'null': 'True', 'to': "orm['checklist.CheckList']"}),
            'pergunta': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'privativo': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'problema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['checklist.Problema']", 'null': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'checklist.node': {
            'Meta': {'object_name': 'Node'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'checklist.nodepergunta': {
            'Meta': {'object_name': 'NodePergunta', '_ormbases': ['checklist.Node']},
            'node_nao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lista_nao'", 'to': "orm['checklist.Node']"}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['checklist.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'node_sim': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lista_sim'", 'to': "orm['checklist.Node']"}),
            'pergunta': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'checklist.noderaiz': {
            'Meta': {'object_name': 'NodeRaiz', '_ormbases': ['checklist.Node']},
            'node_nao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'nao_lista'", 'to': "orm['checklist.Node']"}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['checklist.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'node_sim': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sim_lista'", 'to': "orm['checklist.Node']"}),
            'pergunta': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'problema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['checklist.Problema']"})
        },
        'checklist.noderoteiro': {
            'Meta': {'object_name': 'NodeRoteiro', '_ormbases': ['checklist.Node']},
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['checklist.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'privativo': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {})
        },
        'checklist.nodetecnico': {
            'Meta': {'object_name': 'NodeTecnico', '_ormbases': ['checklist.Node']},
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['checklist.Node']", 'unique': 'True', 'primary_key': 'True'})
        },
        'checklist.problema': {
            'Meta': {'object_name': 'Problema'},
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servico.Produto']"})
        },
        'servico.produto': {
            'Meta': {'object_name': 'Produto'},
            'descricao': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['checklist']
