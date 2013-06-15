# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Person.updated'
        db.alter_column(u'tradeschool_person', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Person.created'
        db.alter_column(u'tradeschool_person', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Feedback.updated'
        db.alter_column(u'tradeschool_feedback', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Feedback.created'
        db.alter_column(u'tradeschool_feedback', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Branch.updated'
        db.alter_column(u'tradeschool_branch', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Branch.created'
        db.alter_column(u'tradeschool_branch', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'BranchPage.updated'
        db.alter_column(u'tradeschool_branchpage', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'BranchPage.created'
        db.alter_column(u'tradeschool_branchpage', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'BarterItem.updated'
        db.alter_column(u'tradeschool_barteritem', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'BarterItem.created'
        db.alter_column(u'tradeschool_barteritem', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'TeacherClassApproval.updated'
        db.alter_column(u'tradeschool_teacherclassapproval', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'TeacherClassApproval.created'
        db.alter_column(u'tradeschool_teacherclassapproval', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'BranchEmailContainer.updated'
        db.alter_column(u'tradeschool_branchemailcontainer', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'BranchEmailContainer.created'
        db.alter_column(u'tradeschool_branchemailcontainer', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'TimeRange.updated'
        db.alter_column(u'tradeschool_timerange', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'TimeRange.created'
        db.alter_column(u'tradeschool_timerange', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Photo.updated'
        db.alter_column(u'tradeschool_photo', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Photo.created'
        db.alter_column(u'tradeschool_photo', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'TeacherReminder.updated'
        db.alter_column(u'tradeschool_teacherreminder', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'TeacherReminder.created'
        db.alter_column(u'tradeschool_teacherreminder', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Venue.updated'
        db.alter_column(u'tradeschool_venue', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Venue.created'
        db.alter_column(u'tradeschool_venue', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'TeacherConfirmation.updated'
        db.alter_column(u'tradeschool_teacherconfirmation', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'TeacherConfirmation.created'
        db.alter_column(u'tradeschool_teacherconfirmation', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Time.updated'
        db.alter_column(u'tradeschool_time', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Time.created'
        db.alter_column(u'tradeschool_time', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Course.updated'
        db.alter_column(u'tradeschool_course', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Course.created'
        db.alter_column(u'tradeschool_course', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'StudentConfirmation.updated'
        db.alter_column(u'tradeschool_studentconfirmation', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'StudentConfirmation.created'
        db.alter_column(u'tradeschool_studentconfirmation', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'TeacherFeedback.updated'
        db.alter_column(u'tradeschool_teacherfeedback', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'TeacherFeedback.created'
        db.alter_column(u'tradeschool_teacherfeedback', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Cluster.updated'
        db.alter_column(u'tradeschool_cluster', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Cluster.created'
        db.alter_column(u'tradeschool_cluster', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'RegisteredItem.updated'
        db.alter_column(u'tradeschool_registereditem', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'RegisteredItem.created'
        db.alter_column(u'tradeschool_registereditem', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'StudentReminder.updated'
        db.alter_column(u'tradeschool_studentreminder', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'StudentReminder.created'
        db.alter_column(u'tradeschool_studentreminder', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Registration.updated'
        db.alter_column(u'tradeschool_registration', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Registration.created'
        db.alter_column(u'tradeschool_registration', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'ScheduleEmailContainer.updated'
        db.alter_column(u'tradeschool_scheduleemailcontainer', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'ScheduleEmailContainer.created'
        db.alter_column(u'tradeschool_scheduleemailcontainer', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'DefaultEmailContainer.updated'
        db.alter_column(u'tradeschool_defaultemailcontainer', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'DefaultEmailContainer.created'
        db.alter_column(u'tradeschool_defaultemailcontainer', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'StudentFeedback.updated'
        db.alter_column(u'tradeschool_studentfeedback', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'StudentFeedback.created'
        db.alter_column(u'tradeschool_studentfeedback', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Schedule.updated'
        db.alter_column(u'tradeschool_schedule', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Schedule.created'
        db.alter_column(u'tradeschool_schedule', 'created', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Person.updated'
        db.alter_column(u'tradeschool_person', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Person.created'
        db.alter_column(u'tradeschool_person', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Feedback.updated'
        db.alter_column(u'tradeschool_feedback', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Feedback.created'
        db.alter_column(u'tradeschool_feedback', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Branch.updated'
        db.alter_column(u'tradeschool_branch', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Branch.created'
        db.alter_column(u'tradeschool_branch', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'BranchPage.updated'
        db.alter_column(u'tradeschool_branchpage', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'BranchPage.created'
        db.alter_column(u'tradeschool_branchpage', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'BarterItem.updated'
        db.alter_column(u'tradeschool_barteritem', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'BarterItem.created'
        db.alter_column(u'tradeschool_barteritem', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'TeacherClassApproval.updated'
        db.alter_column(u'tradeschool_teacherclassapproval', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'TeacherClassApproval.created'
        db.alter_column(u'tradeschool_teacherclassapproval', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'BranchEmailContainer.updated'
        db.alter_column(u'tradeschool_branchemailcontainer', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'BranchEmailContainer.created'
        db.alter_column(u'tradeschool_branchemailcontainer', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'TimeRange.updated'
        db.alter_column(u'tradeschool_timerange', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'TimeRange.created'
        db.alter_column(u'tradeschool_timerange', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Photo.updated'
        db.alter_column(u'tradeschool_photo', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Photo.created'
        db.alter_column(u'tradeschool_photo', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'TeacherReminder.updated'
        db.alter_column(u'tradeschool_teacherreminder', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'TeacherReminder.created'
        db.alter_column(u'tradeschool_teacherreminder', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Venue.updated'
        db.alter_column(u'tradeschool_venue', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Venue.created'
        db.alter_column(u'tradeschool_venue', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'TeacherConfirmation.updated'
        db.alter_column(u'tradeschool_teacherconfirmation', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'TeacherConfirmation.created'
        db.alter_column(u'tradeschool_teacherconfirmation', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Time.updated'
        db.alter_column(u'tradeschool_time', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Time.created'
        db.alter_column(u'tradeschool_time', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Course.updated'
        db.alter_column(u'tradeschool_course', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Course.created'
        db.alter_column(u'tradeschool_course', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'StudentConfirmation.updated'
        db.alter_column(u'tradeschool_studentconfirmation', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'StudentConfirmation.created'
        db.alter_column(u'tradeschool_studentconfirmation', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'TeacherFeedback.updated'
        db.alter_column(u'tradeschool_teacherfeedback', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'TeacherFeedback.created'
        db.alter_column(u'tradeschool_teacherfeedback', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Cluster.updated'
        db.alter_column(u'tradeschool_cluster', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Cluster.created'
        db.alter_column(u'tradeschool_cluster', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'RegisteredItem.updated'
        db.alter_column(u'tradeschool_registereditem', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'RegisteredItem.created'
        db.alter_column(u'tradeschool_registereditem', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'StudentReminder.updated'
        db.alter_column(u'tradeschool_studentreminder', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'StudentReminder.created'
        db.alter_column(u'tradeschool_studentreminder', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Registration.updated'
        db.alter_column(u'tradeschool_registration', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Registration.created'
        db.alter_column(u'tradeschool_registration', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'ScheduleEmailContainer.updated'
        db.alter_column(u'tradeschool_scheduleemailcontainer', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'ScheduleEmailContainer.created'
        db.alter_column(u'tradeschool_scheduleemailcontainer', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'DefaultEmailContainer.updated'
        db.alter_column(u'tradeschool_defaultemailcontainer', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'DefaultEmailContainer.created'
        db.alter_column(u'tradeschool_defaultemailcontainer', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'StudentFeedback.updated'
        db.alter_column(u'tradeschool_studentfeedback', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'StudentFeedback.created'
        db.alter_column(u'tradeschool_studentfeedback', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Schedule.updated'
        db.alter_column(u'tradeschool_schedule', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Schedule.created'
        db.alter_column(u'tradeschool_schedule', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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
            'Meta': {'object_name': 'BarterItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.branch': {
            'Meta': {'ordering': "['title']", 'object_name': 'Branch'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cluster': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Cluster']", 'null': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'footer_copy': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'header_copy': ('tinymce.models.HTMLField', [], {'default': "'Barter for knowledge'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_copy': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'organizers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.branchemailcontainer': {
            'Meta': {'object_name': 'BranchEmailContainer'},
            'branch': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'emails'", 'unique': 'True', 'to': u"orm['tradeschool.Branch']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student_confirmation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.StudentConfirmation']"}),
            'student_feedback': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.StudentFeedback']"}),
            'student_reminder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.StudentReminder']"}),
            'teacher_class_approval': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherClassApproval']"}),
            'teacher_confirmation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherConfirmation']"}),
            'teacher_feedback': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherFeedback']"}),
            'teacher_reminder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherReminder']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.branchpage': {
            'Meta': {'ordering': "(u'url',)", 'object_name': 'BranchPage', '_ormbases': [u'flatpages.FlatPage']},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Branch']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'flatpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['flatpages.FlatPage']", 'unique': 'True', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.cluster': {
            'Meta': {'object_name': 'Cluster'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.course': {
            'Meta': {'object_name': 'Course'},
            'branch': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tradeschool.Branch']", 'symmetrical': 'False'}),
            'category': ('django.db.models.fields.SmallIntegerField', [], {'default': '3', 'max_length': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'max_students': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120', 'null': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'courses_taught'", 'to': u"orm['tradeschool.Person']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.defaultemailcontainer': {
            'Meta': {'object_name': 'DefaultEmailContainer'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student_confirmation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.StudentConfirmation']"}),
            'student_feedback': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.StudentFeedback']"}),
            'student_reminder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.StudentReminder']"}),
            'teacher_class_approval': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherClassApproval']"}),
            'teacher_confirmation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherConfirmation']"}),
            'teacher_feedback': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherFeedback']"}),
            'teacher_reminder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherReminder']"}),
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
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'branch': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tradeschool.Branch']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
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
        u'tradeschool.registereditem': {
            'Meta': {'object_name': 'RegisteredItem'},
            'barter_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.BarterItem']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'registered': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '3'}),
            'registration': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Registration']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.registration': {
            'Meta': {'unique_together': "(('schedule', 'student'),)", 'object_name': 'Registration'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tradeschool.BarterItem']", 'through': u"orm['tradeschool.RegisteredItem']", 'symmetrical': 'False'}),
            'registration_status': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '20'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Schedule']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'registrations'", 'to': u"orm['tradeschool.Person']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.schedule': {
            'Meta': {'ordering': "['course_status', 'start_time', '-venue']", 'object_name': 'Schedule'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Course']"}),
            'course_status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'max_length': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 15, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tradeschool.BarterItem']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120', 'unique': 'True', 'null': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 15, 0, 0)'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tradeschool.Person']", 'through': u"orm['tradeschool.Registration']", 'symmetrical': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Venue']", 'null': 'True', 'blank': 'True'})
        },
        u'tradeschool.scheduleemailcontainer': {
            'Meta': {'object_name': 'ScheduleEmailContainer'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'schedule': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'emails'", 'unique': 'True', 'to': u"orm['tradeschool.Schedule']"}),
            'student_confirmation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.StudentConfirmation']"}),
            'student_feedback': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.StudentFeedback']"}),
            'student_reminder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.StudentReminder']"}),
            'teacher_class_approval': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherClassApproval']"}),
            'teacher_confirmation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherConfirmation']"}),
            'teacher_feedback': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherFeedback']"}),
            'teacher_reminder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.TeacherReminder']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.studentconfirmation': {
            'Meta': {'object_name': 'StudentConfirmation'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.studentfeedback': {
            'Meta': {'object_name': 'StudentFeedback'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'days_delta': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'send_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'send_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(10, 0)'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.studentreminder': {
            'Meta': {'object_name': 'StudentReminder'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'days_delta': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'send_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'send_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(10, 0)'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.teacherclassapproval': {
            'Meta': {'object_name': 'TeacherClassApproval'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.teacherconfirmation': {
            'Meta': {'object_name': 'TeacherConfirmation'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.teacherfeedback': {
            'Meta': {'object_name': 'TeacherFeedback'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'days_delta': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'send_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'send_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(10, 0)'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.teacherreminder': {
            'Meta': {'object_name': 'TeacherReminder'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'days_delta': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'email_status': ('django.db.models.fields.CharField', [], {'default': "'not_sent'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'send_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'send_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(10, 0)'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'tradeschool.time': {
            'Meta': {'object_name': 'Time'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Branch']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 15, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 15, 0, 0)'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Venue']", 'null': 'True', 'blank': 'True'})
        },
        u'tradeschool.timerange': {
            'Meta': {'object_name': 'TimeRange'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Branch']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 6, 15, 0, 0)'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2008, 1, 31, 0, 0)'}),
            'friday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'monday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'saturday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 6, 15, 0, 0)'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2008, 1, 31, 0, 0)'}),
            'sunday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thursday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'wednesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'tradeschool.venue': {
            'Meta': {'object_name': 'Venue'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tradeschool.Branch']"}),
            'capacity': ('django.db.models.fields.SmallIntegerField', [], {'default': '20', 'max_length': '4'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'#b28d26'", 'max_length': '7'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'resources': ('django.db.models.fields.TextField', [], {'default': "'For Example: Chairs, Tables'", 'null': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'venue_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'max_length': '1'})
        }
    }

    complete_apps = ['tradeschool']