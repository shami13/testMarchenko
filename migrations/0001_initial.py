# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'User'
        db.create_table('testMarchenko_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bio', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('birthDate', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('testMarchenko', ['User'])

        # Adding model 'URL'
        db.create_table('testMarchenko_url', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('testMarchenko', ['URL'])

        # Adding model 'ModelActions'
        db.create_table('testMarchenko_modelactions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('testMarchenko', ['ModelActions'])

    def backwards(self, orm):

        # Deleting model 'User'
        db.delete_table('testMarchenko_user')

        # Deleting model 'URL'
        db.delete_table('testMarchenko_url')

        # Deleting model 'ModelActions'
        db.delete_table('testMarchenko_modelactions')

    models = {
        'testMarchenko.modelactions': {
            'Meta': {'object_name': 'ModelActions'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'})},
        'testMarchenko.url': {
            'Meta': {'object_name': 'URL'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})},
        'testMarchenko.user': {
            'Meta': {'object_name': 'User'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'birthDate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '50'})}}

    complete_apps = ['testMarchenko']
