# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Portlet'
        db.create_table(u'slot_portlet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classname', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal(u'slot', ['Portlet'])

        # Adding model 'Slot'
        db.create_table(u'slot_slot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.TextField')(unique=True, db_index=True)),
        ))
        db.send_create_signal(u'slot', ['Slot'])

        # Adding M2M table for field portlets on 'Slot'
        m2m_table_name = db.shorten_name(u'slot_slot_portlets')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('slot', models.ForeignKey(orm[u'slot.slot'], null=False)),
            ('portlet', models.ForeignKey(orm[u'slot.portlet'], null=False))
        ))
        db.create_unique(m2m_table_name, ['slot_id', 'portlet_id'])


    def backwards(self, orm):
        # Deleting model 'Portlet'
        db.delete_table(u'slot_portlet')

        # Deleting model 'Slot'
        db.delete_table(u'slot_slot')

        # Removing M2M table for field portlets on 'Slot'
        db.delete_table(db.shorten_name(u'slot_slot_portlets'))


    models = {
        u'slot.portlet': {
            'Meta': {'object_name': 'Portlet'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'slot.slot': {
            'Meta': {'object_name': 'Slot'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.TextField', [], {'unique': 'True', 'db_index': 'True'}),
            'portlets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['slot.Portlet']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['slot']