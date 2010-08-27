# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'URL.priority'
        db.add_column('testMarchenko_url', 'priority', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'URL.priority'
        db.delete_column('testMarchenko_url', 'priority')


    models = {
        'testMarchenko.modelactions': {
            'Meta': {'object_name': 'ModelActions'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'testMarchenko.url': {
            'Meta': {'object_name': 'URL'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'testMarchenko.user': {
            'Meta': {'object_name': 'User'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'birthDate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['testMarchenko']
