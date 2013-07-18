# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Settings'
        db.create_table('easy_twitter_settings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_token_uri', self.gf('django.db.models.fields.URLField')(default='https://api.twitter.com/oauth/request_token', max_length=500)),
            ('auth_token_uri', self.gf('django.db.models.fields.URLField')(default='https://api.twitter.com/oauth/authorize', max_length=500)),
            ('access_token_uri', self.gf('django.db.models.fields.URLField')(default='https://api.twitter.com/oauth/access_token', max_length=500)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('access_token_secret', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('auth_token', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('consumer_key', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('consumer_secret', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('count_limit', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('easy_twitter', ['Settings'])


    def backwards(self, orm):
        
        # Deleting model 'Settings'
        db.delete_table('easy_twitter_settings')


    models = {
        'easy_twitter.settings': {
            'Meta': {'object_name': 'Settings'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'access_token_uri': ('django.db.models.fields.URLField', [], {'default': "'https://api.twitter.com/oauth/access_token'", 'max_length': '500'}),
            'auth_token': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'auth_token_uri': ('django.db.models.fields.URLField', [], {'default': "'https://api.twitter.com/oauth/authorize'", 'max_length': '500'}),
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'consumer_secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'count_limit': ('django.db.models.fields.IntegerField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_token_uri': ('django.db.models.fields.URLField', [], {'default': "'https://api.twitter.com/oauth/request_token'", 'max_length': '500'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['easy_twitter']
