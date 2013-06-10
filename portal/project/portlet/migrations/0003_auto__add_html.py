# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HTML'
        db.create_table(u'portlet_html', (
            (u'portlet_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['slot.Portlet'], unique=True, primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('code', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'portlet', ['HTML'])


    def backwards(self, orm):
        # Deleting model 'HTML'
        db.delete_table(u'portlet_html')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'portlet.basico': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Basico'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'imagem_posicao': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'portlet.html': {
            'Meta': {'object_name': 'HTML', '_ormbases': [u'slot.Portlet']},
            'code': ('django.db.models.fields.TextField', [], {}),
            u'portlet_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['slot.Portlet']", 'unique': 'True', 'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'portlet.noticia': {
            'Meta': {'object_name': 'Noticia', '_ormbases': [u'slot.Portlet']},
            u'portlet_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['slot.Portlet']", 'unique': 'True', 'primary_key': 'True'}),
            'simplenews': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simplenews.SimpleNews']", 'unique': 'True'})
        },
        u'portlet.ultimasnoticias': {
            'Meta': {'object_name': 'UltimasNoticias', '_ormbases': [u'slot.Portlet']},
            'numero': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5'}),
            u'portlet_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['slot.Portlet']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'simplenews.simplenews': {
            'Meta': {'ordering': "['-publish_date']", 'object_name': 'SimpleNews'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expire_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '255', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'slot.portlet': {
            'Meta': {'object_name': 'Portlet'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['portlet']