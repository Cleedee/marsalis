# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'CheckList'
        db.create_table('checklist_checklist', (
            ('node_sim', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lista_sim', to=orm['checklist.CheckList'])),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('node_nao', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lista_nao', to=orm['checklist.CheckList'])),
            ('privativo', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pergunta', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('problema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['checklist.Problema'], null=True)),
        ))
        db.send_create_signal('checklist', ['CheckList'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'CheckList'
        db.delete_table('checklist_checklist')
    
    
    models = {
        'checklist.checklist': {
            'Meta': {'object_name': 'CheckList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node_nao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lista_nao'", 'to': "orm['checklist.CheckList']"}),
            'node_sim': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lista_sim'", 'to': "orm['checklist.CheckList']"}),
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
