# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'TeacherFeedback.Schedule'
        db.alter_column(u'tradeschool_teacherfeedback', 'Schedule_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Schedule'], unique=True, null=True))
        # Adding unique constraint on 'TeacherFeedback', fields ['Schedule']
        db.create_unique(u'tradeschool_teacherfeedback', ['Schedule_id'])


        # Changing field 'TeacherFeedback.Branch'
        db.alter_column(u'tradeschool_teacherfeedback', 'Branch_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Branch'], unique=True, null=True))
        # Adding unique constraint on 'TeacherFeedback', fields ['Branch']
        db.create_unique(u'tradeschool_teacherfeedback', ['Branch_id'])


        # Changing field 'StudentReminder.Schedule'
        db.alter_column(u'tradeschool_studentreminder', 'Schedule_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Schedule'], unique=True, null=True))
        # Adding unique constraint on 'StudentReminder', fields ['Schedule']
        db.create_unique(u'tradeschool_studentreminder', ['Schedule_id'])


        # Changing field 'StudentReminder.Branch'
        db.alter_column(u'tradeschool_studentreminder', 'Branch_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Branch'], unique=True, null=True))
        # Adding unique constraint on 'StudentReminder', fields ['Branch']
        db.create_unique(u'tradeschool_studentreminder', ['Branch_id'])


        # Changing field 'TeacherReminder.Schedule'
        db.alter_column(u'tradeschool_teacherreminder', 'Schedule_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Schedule'], unique=True, null=True))
        # Adding unique constraint on 'TeacherReminder', fields ['Schedule']
        db.create_unique(u'tradeschool_teacherreminder', ['Schedule_id'])


        # Changing field 'TeacherReminder.Branch'
        db.alter_column(u'tradeschool_teacherreminder', 'Branch_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Branch'], unique=True, null=True))
        # Adding unique constraint on 'TeacherReminder', fields ['Branch']
        db.create_unique(u'tradeschool_teacherreminder', ['Branch_id'])


        # Changing field 'TeacherConfirmation.Schedule'
        db.alter_column(u'tradeschool_teacherconfirmation', 'Schedule_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Schedule'], unique=True, null=True))
        # Adding unique constraint on 'TeacherConfirmation', fields ['Schedule']
        db.create_unique(u'tradeschool_teacherconfirmation', ['Schedule_id'])


        # Changing field 'TeacherConfirmation.Branch'
        db.alter_column(u'tradeschool_teacherconfirmation', 'Branch_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Branch'], unique=True, null=True))
        # Adding unique constraint on 'TeacherConfirmation', fields ['Branch']
        db.create_unique(u'tradeschool_teacherconfirmation', ['Branch_id'])


        # Changing field 'TeacherClassApproval.Schedule'
        db.alter_column(u'tradeschool_teacherclassapproval', 'Schedule_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Schedule'], unique=True, null=True))
        # Adding unique constraint on 'TeacherClassApproval', fields ['Schedule']
        db.create_unique(u'tradeschool_teacherclassapproval', ['Schedule_id'])


        # Changing field 'TeacherClassApproval.Branch'
        db.alter_column(u'tradeschool_teacherclassapproval', 'Branch_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Branch'], unique=True, null=True))
        # Adding unique constraint on 'TeacherClassApproval', fields ['Branch']
        db.create_unique(u'tradeschool_teacherclassapproval', ['Branch_id'])


        # Changing field 'StudentFeedback.Schedule'
        db.alter_column(u'tradeschool_studentfeedback', 'Schedule_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Schedule'], unique=True, null=True))
        # Adding unique constraint on 'StudentFeedback', fields ['Schedule']
        db.create_unique(u'tradeschool_studentfeedback', ['Schedule_id'])


        # Changing field 'StudentFeedback.Branch'
        db.alter_column(u'tradeschool_studentfeedback', 'Branch_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Branch'], unique=True, null=True))
        # Adding unique constraint on 'StudentFeedback', fields ['Branch']
        db.create_unique(u'tradeschool_studentfeedback', ['Branch_id'])


        # Changing field 'StudentConfirmation.Schedule'
        db.alter_column(u'tradeschool_studentconfirmation', 'Schedule_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Schedule'], unique=True, null=True))
        # Adding unique constraint on 'StudentConfirmation', fields ['Schedule']
        db.create_unique(u'tradeschool_studentconfirmation', ['Schedule_id'])


        # Changing field 'StudentConfirmation.Branch'
        db.alter_column(u'tradeschool_studentconfirmation', 'Branch_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tradeschool.Branch'], unique=True, null=True))
        # Adding unique constraint on 'StudentConfirmation', fields ['Branch']
        db.create_unique(u'tradeschool_studentconfirmation', ['Branch_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'StudentConfirmation', fields ['Branch']
        db.delete_unique(u'tradeschool_studentconfirmation', ['Branch_id'])

        # Removing unique constraint on 'StudentConfirmation', fields ['Schedule']
        db.delete_unique(u'tradeschool_studentconfirmation', ['Schedule_id'])

        # Removing unique constraint on 'StudentFeedback', fields ['Branch']
        db.delete_unique(u'tradeschool_studentfeedback', ['Branch_id'])

        # Removing unique constraint on 'StudentFeedback', fields ['Schedule']
        db.delete_unique(u'tradeschool_studentfeedback', ['Schedule_id'])

        # Removing unique constraint on 'TeacherClassApproval', fields ['Branch']
        db.delete_unique(u'tradeschool_teacherclassapproval', ['Branch_id'])

        # Removing unique constraint on 'TeacherClassApproval', fields ['Schedule']
        db.delete_unique(u'tradeschool_teacherclassapproval', ['Schedule_id'])

        # Removing unique constraint on 'TeacherConfirmation', fields ['Branch']
        db.delete_unique(u'tradeschool_teacherconfirmation', ['Branch_id'])

        # Removing unique constraint on 'TeacherConfirmation', fields ['Schedule']
        db.delete_unique(u'tradeschool_teacherconfirmation', ['Schedule_id'])

        # Removing unique constraint on 'TeacherReminder', fields ['Branch']
        db.delete_unique(u'tradeschool_teacherreminder', ['Branch_id'])

        # Removing unique constraint on 'TeacherReminder', fields ['Schedule']
        db.delete_unique(u'tradeschool_teacherreminder', ['Schedule_id'])

        # Removing unique constraint on 'StudentReminder', fields ['Branch']
        db.delete_unique(u'tradeschool_studentreminder', ['Branch_id'])

        # Removing unique constraint on 'StudentReminder', fields ['Schedule']
        db.delete_unique(u'tradeschool_studentreminder', ['Schedule_id'])

        # Removing unique constraint on 'TeacherFeedback', fields ['Branch']
        db.delete_unique(u'tradeschool_teacherfeedback', ['Branch_id'])

        # Removing unique constraint on 'TeacherFeedback', fields ['Schedule']
        db.delete_unique(u'tradeschool_teacherfeedback', ['Schedule_id'])


        # Changing field 'TeacherFeedback.Schedule'
        db.alter_column(u'tradeschool_teacherfeedback', 'Schedule_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Schedule'], null=True))

        # Changing field 'TeacherFeedback.Branch'
        db.alter_column(u'tradeschool_teacherfeedback', 'Branch_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Branch'], null=True))

        # Changing field 'StudentReminder.Schedule'
        db.alter_column(u'tradeschool_studentreminder', 'Schedule_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Schedule'], null=True))

        # Changing field 'StudentReminder.Branch'
        db.alter_column(u'tradeschool_studentreminder', 'Branch_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Branch'], null=True))

        # Changing field 'TeacherReminder.Schedule'
        db.alter_column(u'tradeschool_teacherreminder', 'Schedule_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Schedule'], null=True))

        # Changing field 'TeacherReminder.Branch'
        db.alter_column(u'tradeschool_teacherreminder', 'Branch_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Branch'], null=True))

        # Changing field 'TeacherConfirmation.Schedule'
        db.alter_column(u'tradeschool_teacherconfirmation', 'Schedule_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Schedule'], null=True))

        # Changing field 'TeacherConfirmation.Branch'
        db.alter_column(u'tradeschool_teacherconfirmation', 'Branch_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Branch'], null=True))

        # Changing field 'TeacherClassApproval.Schedule'
        db.alter_column(u'tradeschool_teacherclassapproval', 'Schedule_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Schedule'], null=True))

        # Changing field 'TeacherClassApproval.Branch'
        db.alter_column(u'tradeschool_teacherclassapproval', 'Branch_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Branch'], null=True))

        # Changing field 'StudentFeedback.Schedule'
        db.alter_column(u'tradeschool_studentfeedback', 'Schedule_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Schedule'], null=True))

        # Changing field 'StudentFeedback.Branch'
        db.alter_column(u'tradeschool_studentfeedback', 'Branch_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Branch'], null=True))

        # Changing field 'StudentConfirmation.Schedule'
        db.alter_column(u'tradeschool_studentconfirmation', 'Schedule_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Schedule'], null=True))

        # Changing field 'StudentConfirmation.Branch'
        db.alter_column(u'tradeschool_studentconfirmation', 'Branch_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tradeschool.Branch'], null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'flatpages.flatpage': {
            'Meta': {'ordering': "(u'url',)", 'object_name': 'FlatPage', 'db_table': "u'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tradeschool.barteritem': {
            'Meta': {'ordering': "['title']", 'object_name': 'BarterItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Schedule']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.branch': {
            'Meta': {'ordering': "['title']", 'object_name': 'Branch'},
            'branch_status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cluster': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Cluster']", 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'footer_copy': ('tinymce.models.HTMLField', [], {'default': "'Information for the footer of the page'", 'null': 'True', 'blank': 'True'}),
            'header_copy': ('tinymce.models.HTMLField', [], {'default': "'Barter for knowledge'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_copy': ('tinymce.models.HTMLField', [], {'default': "'Information for the header of the page'", 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'organizers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'branches_organized'", 'symmetrical': 'False', 'db_column': "'person_id'", 'to': u"orm['tradeschool.Person']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'student_confirmation': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.StudentConfirmation']", 'unique': 'True'}),
            'student_feedback': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.StudentFeedback']", 'unique': 'True'}),
            'student_reminder': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.StudentReminder']", 'unique': 'True'}),
            'teacher_class_approval': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherClassApproval']", 'unique': 'True'}),
            'teacher_confirmation': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherConfirmation']", 'unique': 'True'}),
            'teacher_feedback': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherFeedback']", 'unique': 'True'}),
            'teacher_reminder': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherReminder']", 'unique': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.branchpage': {
            'Meta': {'ordering': "['branch', 'title']", 'object_name': 'BranchPage', '_ormbases': [u'flatpages.FlatPage']},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Branch']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'flatpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['flatpages.FlatPage']", 'unique': 'True', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.cluster': {
            'Meta': {'ordering': "['name']", 'object_name': 'Cluster'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.course': {
            'Meta': {'ordering': "['title']", 'object_name': 'Course'},
            'branches': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tradeschool.Branch']", 'symmetrical': 'False'}),
            'category': ('django.db.models.fields.SmallIntegerField', [], {'default': '3', 'max_length': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'max_students': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'courses_taught'", 'to': u"orm['tradeschool.Person']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.defaultemailcontainer': {
            'Meta': {'object_name': 'DefaultEmailContainer'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student_confirmation': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.StudentConfirmation']", 'unique': 'True'}),
            'student_feedback': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.StudentFeedback']", 'unique': 'True'}),
            'student_reminder': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.StudentReminder']", 'unique': 'True'}),
            'teacher_class_approval': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherClassApproval']", 'unique': 'True'}),
            'teacher_confirmation': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherConfirmation']", 'unique': 'True'}),
            'teacher_feedback': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherFeedback']", 'unique': 'True'}),
            'teacher_reminder': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherReminder']", 'unique': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'feedback_type': ('django.db.models.fields.CharField', [], {'default': "'student'", 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Schedule']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.person': {
            'Meta': {'ordering': "['fullname']", 'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'branches': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tradeschool.Branch']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '50', 'null': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '220'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'tradeschool.photo': {
            'Meta': {'ordering': "['position']", 'object_name': 'Photo'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Branch']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'filename': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.registration': {
            'Meta': {'ordering': "['schedule', 'registration_status', 'student']", 'unique_together': "(('schedule', 'student'),)", 'object_name': 'Registration'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tradeschool.BarterItem']", 'symmetrical': 'False'}),
            'registration_status': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '20'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Schedule']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'registrations'", 'to': u"orm['tradeschool.Person']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.schedule': {
            'Meta': {'ordering': "['schedule_status', 'start_time', '-venue']", 'object_name': 'Schedule'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Course']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'schedule_status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)'}),
            'student_confirmation': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.StudentConfirmation']", 'unique': 'True'}),
            'student_feedback': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.StudentFeedback']", 'unique': 'True'}),
            'student_reminder': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.StudentReminder']", 'unique': 'True'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tradeschool.Person']", 'through': u"orm['tradeschool.Registration']", 'symmetrical': 'False'}),
            'teacher_class_approval': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherClassApproval']", 'unique': 'True'}),
            'teacher_confirmation': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherConfirmation']", 'unique': 'True'}),
            'teacher_feedback': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherFeedback']", 'unique': 'True'}),
            'teacher_reminder': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.TeacherReminder']", 'unique': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Venue']", 'null': 'True', 'blank': 'True'})
        },
        u'tradeschool.studentconfirmation': {
            'Branch': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Branch']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'StudentConfirmation'},
            'Schedule': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Schedule']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'tradeschool.studentfeedback': {
            'Branch': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Branch']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'StudentFeedback'},
            'Schedule': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Schedule']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'days_delta': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'send_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'send_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(10, 0)'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'tradeschool.studentreminder': {
            'Branch': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Branch']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'StudentReminder'},
            'Schedule': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Schedule']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'days_delta': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'send_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'send_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(10, 0)'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'tradeschool.teacherclassapproval': {
            'Branch': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Branch']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'TeacherClassApproval'},
            'Schedule': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Schedule']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'tradeschool.teacherconfirmation': {
            'Branch': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Branch']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'TeacherConfirmation'},
            'Schedule': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Schedule']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'tradeschool.teacherfeedback': {
            'Branch': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Branch']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'TeacherFeedback'},
            'Schedule': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Schedule']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'days_delta': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'send_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'send_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(10, 0)'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'tradeschool.teacherreminder': {
            'Branch': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Branch']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'TeacherReminder'},
            'Schedule': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tradeschool.Schedule']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'days_delta': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'send_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'send_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(10, 0)'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'tradeschool.time': {
            'Meta': {'object_name': 'Time'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Branch']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Venue']", 'null': 'True', 'blank': 'True'})
        },
        u'tradeschool.timerange': {
            'Meta': {'object_name': 'TimeRange'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Branch']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2008, 1, 31, 0, 0)'}),
            'friday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'monday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'saturday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2008, 1, 31, 0, 0)'}),
            'sunday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thursday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Venue']", 'null': 'True', 'blank': 'True'}),
            'wednesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'tradeschool.venue': {
            'Meta': {'ordering': "['branch', 'is_active', 'title']", 'object_name': 'Venue'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Branch']"}),
            'capacity': ('django.db.models.fields.SmallIntegerField', [], {'default': '20', 'max_length': '4'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'#49afde'", 'max_length': '7'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'resources': ('django.db.models.fields.TextField', [], {'default': "'For Example: Chairs, Tables'", 'null': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['tradeschool']