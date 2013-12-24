from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.flatpages.admin import FlatpageForm
from django.contrib import admin
from admin_enhancer import admin as enhanced_admin
from tradeschool.models import *
from tradeschool.forms import *


class BaseAdmin(enhanced_admin.EnhancedModelAdminMixin, admin.ModelAdmin):
    """
    Base admin model. Filters objects queryset according to the current branch.
    """

    def queryset(self, request, q=None):
        """
        queryset is filtered against the Branch objects that the logged in
        Person is organizing. In the case the logged in Person is a superuser,
        they see all of the data without filtering.
        """
        qs = super(BaseAdmin, self).queryset(request)

        # superusers get to see all data,
        # only filter queryset if the user is not a superuser
        if not request.user.is_superuser:
            # other users see data filtered by
            # the branches they're organizing.
            if q is None:
                q = Q(branches__in=request.user.branches_organized.all)
            qs = qs.filter(q)

        # we need this from the superclass method
        # otherwise we might try to *None, which is bad
        ordering = self.ordering or ()

        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        when an admin model has a branch foreign key field
        filter the queryset of the barnch field by the branches
        that the logged in user is ogranizing.
        """
        if db_field.name == 'branch':
            kwargs['queryset'], kwargs['initial'] = self.filter_dbfield(
                request,
                Branch,
                Q(pk__in=request.user.branches_organized.all)
            )
        return super(BaseAdmin, self).formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """
        when an admin model has a branch manytomany field
        filter the queryset of the barnches field by the branches
        that the logged in user is organizing. Make the user's
        defulat_branch selected in the form widget.
        """
        if db_field.name == 'branches':
            qs = Branch.objects.filter(
                pk__in=request.user.branches_organized.all
            )
            kwargs['queryset'] = qs

            #  Make the user's defulat_branch selected in the form widget.
            kwargs['initial'] = [request.user.default_branch, ]

        return super(BaseAdmin, self).formfield_for_manytomany(
            db_field,
            request,
            **kwargs
        )

    def filter_dbfield(self, request, model, q, **kwargs):
        """
        This is a shortcut method to filter a field of a model
        by the a Q object that's pased as an argument.
        The filtering is done only when the logged in user
        is not a superuser, to be consistent with the entire admin,
        which lets superusers see all data.
        This method also returns an 'initial' key argument, which is set to
        the first item in the queryset, unless the model passed is Branch.
        In that case the 'initial' is set the the logged in user's
        default_branch.
        """
        # only perform filtering if the user is not a superuser
        if not request.user.is_superuser:

            # query the db and filter by the passed in Q obhects
            qs = model.objects.filter(q).distinct()

            # set the queryset key argument.
            kwargs['queryset'] = qs

            # set the user's default_branch if the passed in model is Branch
            if model == Branch:
                kwargs['initial'] = request.user.default_branch

            # only set an 'initial' value if there is at least
            # one item in the queryset
            else:
                if qs.count() > 0:
                    kwargs['initial'] = qs[0]

        # if the user IS a superuser, don't filter, but do try to
        # return an 'initial' key argument if there is one
        else:
            qs = model.objects.all()
            kwargs['queryset'] = qs
            try:
                kwargs['initial'] = qs[0]
            except IndexError:
                kwargs['initial'] = None
        return kwargs['queryset'], kwargs['initial']


class BaseTabularInline(admin.TabularInline):
    def queryset(self, request, q):
        """
        TODO: This is actualy a duplication of the BaseAdmin method
        and should extend it instead.
        """
        qs = super(BaseTabularInline, self).queryset(request)

        # superusers get to see all data,
        # only filter queryset if the user is not a superuser
        if not request.user.is_superuser:
            # other users see data filtered by
            # the branches they're organizing.
            if q is None:
                q = Q(branches__in=request.user.branches_organized.all)
            qs = qs.filter(q)

        # we need this from the superclass method
        # otherwise we might try to *None, which is bad
        ordering = self.ordering or ()

        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def filter_dbfield(self, request, model, q, **kwargs):
        """
        TODO: This is actualy a duplication of the BaseAdmin method
        and should extend it instead.
        """
        # only perform filtering if the user is not a superuser
        if not request.user.is_superuser:

            # query the db and filter by the passed in Q obhects
            qs = model.objects.filter(q)

            # set the queryset key argument.
            kwargs['queryset'] = qs

            # set the user's default_branch if the passed in model is Branch
            if model == Branch:
                kwargs['initial'] = request.user.default_branch

            # only set an 'initial' value if there is at least
            # one item in the queryset
            else:
                if qs.count() > 0:
                    kwargs['initial'] = qs[0]

        # if the user IS a superuser, don't filter, but do try to
        # return an 'initial' key argument if there is one
        else:
            qs = model.objects.all()
            kwargs['queryset'] = qs
            try:
                kwargs['initial'] = qs[0]
            except IndexError:
                kwargs['initial'] = None
        return kwargs['queryset'], kwargs['initial']


class BaseStackedInline(admin.StackedInline):
    def queryset(self, request, q):
        """
        TODO: This is actualy a duplication of the BaseAdmin method
        and should extend it instead.
        """
        qs = super(BaseStackedInline, self).queryset(request)

        # superusers get to see all data,
        # only filter queryset if the user is not a superuser
        if not request.user.is_superuser:
            # other users see data filtered by
            # the branches they're organizing.
            if q is None:
                q = Q(branches__in=request.user.branches_organized.all)
            qs = qs.filter(q)

        # we need this from the superclass method
        # otherwise we might try to *None, which is bad
        ordering = self.ordering or ()

        if ordering:
            qs = qs.order_by(*ordering)
        return qs


class TimedEmailBranchInline(BaseTabularInline):
    """
    All branch TimedEmails are displayed as inlines in the Branch admin model.

    We want to expose different fields of the Email model in the context
    of editing a branch, since the user is in fact editing a template that
    will be copied from to each Schedule that's created. Therefore we only
    display fields that determine the way the send_on is calculated,
    like 'days_delta' & 'send_time'), but not the fields that reflect the
    status of a Schedule email, like 'send_on' & 'email_status'.

    Do not allow more than 1 instance of the TimedEmail model,
    since there is a one-to-one relationship between the email and the branch.
    """
    def queryset(self, request):
        """Return the super queryset method with no filtering."""
        return super(TimedEmailBranchInline, self).queryset(request, Q())
    extra = 0
    max_num = 0
    fields = ('subject', 'content', 'days_delta', 'send_time')


class TimedEmailScheduleInline(BaseTabularInline):
    """
    All schedule TimedEmails are displayed as inlines in the Schedule
    admin model.

    We want to expose different fields of the Email model in the context
    of editing a schedue, since the user is in fact editing an email that
    will be sent out Therefore we only display fields that reflect the
    status of a TimedEmail, like 'send_on' & 'email_status', and not any fields
    that determine the way the send_on is calculated,

    Do not allow more than 1 instance of the TimedEmail model,
    since there is a onetoone relationship between the email and the scheudle.
    """
    def queryset(self, request):
        """Return the super queryset method with no filtering."""
        return super(TimedEmailScheduleInline, self).queryset(request, Q())
    extra = 0
    max_num = 0
    fields = ('subject', 'content', 'email_status', 'send_on')


class EmailBranchInline(BaseTabularInline):
    """
    All branch Emails are displayed as inlines in the Branch admin model.

    Do not allow more than 1 instance of the TimedEmail model,
    since there is a one-to-one relationship between the email and the branch.
    """
    def queryset(self, request):
        """Return the super queryset method with no filtering."""
        return super(EmailBranchInline, self).queryset(request, Q())
    extra = 0
    max_num = 0
    fields = ('subject', 'content')


class EmailScheduleInline(BaseTabularInline):
    """
    All schedule TimedEmails are displayed as inlines in the Schedule
    admin model.

    Do not allow more than 1 instance of the TimedEmail model,
    since there is a onetoone relationship between the email and the scheudle.
    """
    def queryset(self, request):
        """Return the super queryset method with no filtering."""
        return super(EmailScheduleInline, self).queryset(request, Q())
    extra = 0
    max_num = 0
    fields = ('subject', 'content', 'email_status')


class StudentConfirmationBranchInline(EmailBranchInline):
    model = StudentConfirmation


class StudentConfirmationScheduleInline(EmailScheduleInline):
    model = StudentConfirmation


class StudentReminderBranchInline(TimedEmailBranchInline):
    model = StudentReminder


class StudentReminderScheduleInline(TimedEmailScheduleInline):
    model = StudentReminder


class StudentFeedbackBranchInline(TimedEmailBranchInline):
    model = StudentFeedback


class StudentFeedbackScheduleInline(TimedEmailScheduleInline):
    model = StudentFeedback


class TeacherConfirmationBranchInline(EmailBranchInline):
    model = TeacherConfirmation


class TeacherConfirmationScheduleInline(EmailScheduleInline):
    model = TeacherConfirmation


class TeacherClassApprovalBranchInline(EmailBranchInline):
    model = TeacherClassApproval


class TeacherClassApprovalScheduleInline(EmailScheduleInline):
    model = TeacherClassApproval


class TeacherReminderBranchInline(TimedEmailBranchInline):
    model = TeacherReminder


class TeacherReminderScheduleInline(TimedEmailScheduleInline):
    model = TeacherReminder


class TeacherFeedbackBranchInline(TimedEmailBranchInline):
    model = TeacherFeedback


class TeacherFeedbackScheduleInline(TimedEmailScheduleInline):
    model = TeacherFeedback


class OrganizedBranchInline(BaseTabularInline):
    """
    This inline model is used when adding or changing an Organizer.
    It exposes the reverse of the Branch.organizers m2m field, thus
    letting admins create Organizers who already have branch they
    are organizing.
    """
    def queryset(self, request):
        """Return the super queryset method with no filtering."""
        return super(OrganizedBranchInline, self).queryset(request, Q())

    model = Branch.organizers.through
    verbose_name = "Branch Organized by This Person"
    verbose_name_plural = "Branches Organized by This Person"
    extra = 1


class ClusteredBranchInline(BaseTabularInline):
    """
    This inline model is used when adding or changing an Cluster.
    It exposes the reverse of the Branch.clusters m2m field, thus
    letting admins create Clusters who already have branches.
    """
    def queryset(self, request):
        """Return the super queryset method with no filtering."""
        return super(ClusteredBranchInline, self).queryset(request, Q())

    model = Branch.clusters.through
    extra = 1


class ScheduleInline(BaseTabularInline):
    """
    Schedule model inline admin modell is use in order to let admins
    create repeat schedules quickly.
    """
    def queryset(self, request):
        """Filter branches by those organized by the logged in user."""
        return super(ScheduleInline, self).queryset(
            request,
            Q(branch__in=request.user.branches_organized.all)
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Filter Schedule's venues by those that are related
        to branches organized by the logged in user.
        """
        if db_field.name == 'venue':
            kwargs['queryset'] = Venue.objects.filter(
                branch__in=request.user.branches_organized.all
            )
        return super(ScheduleInline, self).formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )

    model = Schedule
    extra = 0
    fields = ('start_time', 'end_time', 'venue')


class RegistrationInline(enhanced_admin.EnhancedModelAdminMixin, BaseTabularInline):
    """
    The Registration inline model is used in the Schedule Admin Model
    in order to give an overview of Schedule's registrations.
    """
    def queryset(self, request):
        """
        Filter Registrations by those that are related to Schedules that
        are scheduled in branches that are organized by the logged in user.
        """
        return super(RegistrationInline, self).queryset(
            request,
            Q(schedule__branch__in=request.user.branches_organized.all)
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Filter Registration's students by those that are related
        to branches organized by the logged in user.
        """
        if db_field.name == 'student':
            kwargs['queryset'], kwargs['initial'] = self.filter_dbfield(
                request,
                Student,
                Q(branch__in=request.user.branches_organized.all)
            )
        return super(RegistrationInline, self).formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )

    def registration_link(self, obj):
        """
        Return HTML with a link to the Registration object's admin change form.
        This is used as a readonly field, so each Registration can be edited if
        necassary in a new window from the Schedule Admin Model.
        """
        # url to registration admin edit form
        url = reverse('admin:tradeschool_registration_change', args=(obj.pk,))

        # return a safe output so the html can be rendered in the template
        return mark_safe(
            '<a target="_blank" href="%s">%s</a>' % (url, obj.student.fullname)
        )
    registration_link.short_description = _('Title')

    model = Registration
    readonly_fields = (
        'registration_link',
        'items',
        'registration_status'
    )
    fields = (
        'registration_link',
        'items',
        'registration_status',
    )
    extra = 0


class BarterItemInline(BaseTabularInline):
    """
    The BarterItem inline model is used in the Schedule Admin Model
    in order to give an overview of Schedule's BarterItems and allow
    for quick editing of the list if necassary.
    """
    def queryset(self, request):
        """
        Filter BarterItems that are related to Schedules that are scheduled
        in branches that are organized by the logged in user.
        """
        return super(BarterItemInline, self).queryset(
            request,
            Q(schedule__branch__in=request.user.branches_organized.all)
        )

    def title_link(self, obj):
        """
        Return HTML with a link to the BarterItem object's admin change form.
        This is used as a readonly field, so each BarterItem can be edited in
        a new window, easily accessible from the Schedule Admin Model.
        """
        # url to registration admin edit form
        url = reverse('admin:tradeschool_barteritem_change', args=(obj.pk,))

        # return a safe output so the html can be rendered in the template
        return mark_safe(
            '<a target="_blank" href="%s">%s</a>' % (url, obj.title)
        )
    title_link.short_description = _('Title')

    model = BarterItem
    extra = 0


class BarterItemReadOnlyInline(BarterItemInline):
    """
    """
    fields = ('title_link',)
    readonly_fields = ('title_link',)


class BarterItemEditableInline(BarterItemInline):
    """
    """
    fields = ('title',)


class FeedbackInline(enhanced_admin.EnhancedAdminMixin, BaseTabularInline):
    """
    The Feedback inline model is used in the PsstSchedule Admin Model
    in order to give an overview of the Feedback that was submitted
    about the Schedule by registered students and the teacher.
    """
    def queryset(self, request):
        """
        Filter to Feedbacks that are related to Schedules that are scheduled
        in branches that are organized by the logged in user.
        """
        return super(FeedbackInline, self).queryset(
            request,
            Q(schedule__branch__in=request.user.branches_organized.all)
        )

    model = Feedback
    fields = ('feedback_type', 'content',)
    readonly_fields = ('feedback_type',)
    extra = 0


class PhotoInline(enhanced_admin.EnhancedAdminMixin, BaseTabularInline):
    """
    The Photo inline model is used in the Branch Admin Model in order to
    give an overview of the Photo that appear in the homepage gallery.
    """
    def queryset(self, request):
        """
        Filter photos by those that are related to branches that are
        organized by the logged in user.
        """
        return super(PhotoInline, self).queryset(
            request,
            Q(branch__in=request.user.branches_organized.all)
        )

    def render_image(self, obj):
        """Return HTML with an img tag showing a thumbnail of the Photo."""
        return mark_safe(
            '<img src="%s" class="branch_image"/>' % obj.filename.url
        )
    render_image.short_description = _("Thumbnail")

    model = Photo
    fields = (
        'render_image',
        'filename',
        'position',
    )
    readonly_fields = ('render_image',)
    extra = 0
    sortable_field_name = 'position'


class BranchAdmin(BaseAdmin):
    """
    BranchAdmin is used to manage a Branch. When adding a new Branch,
    it lets you edit the basic fields, and when editing one it also
    lets you edit the Emails that will be copied to each Scheduled class.

    Some fields have extra significance in the TS system:
        * Branch.timezone sets the timezone by which all of the dates and times
          are calculated on both the frontend and the backend.
        * Branch.language sets the language that the frontend
          will be translated to.
        * Branch.slug will set the URL that the branch website will be on.
    """
    def queryset(self, request):
        """
        Filter to Branches that are organized by the logged in user.
        """
        return super(BranchAdmin, self).queryset(
            request,
            (
                Q(pk__in=request.user.branches_organized.all)
                | Q(branch_status='pending')
            )
        )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
        Include the Email inlines and Photo inlines only when editing a Branch.
        There is no need to show them when creating a new one, as the Emails
        are genereated automatically and will just make the add form confusing.
        """
        self.inlines = (
            StudentConfirmationBranchInline,
            TeacherConfirmationBranchInline,
            TeacherClassApprovalBranchInline,
            TeacherReminderBranchInline,
            TeacherFeedbackBranchInline,
            StudentReminderBranchInline,
            StudentFeedbackBranchInline,
            PhotoInline,
        )
        return super(BranchAdmin, self).change_view(request, object_id)

    def add_view(self, request, form_url='', extra_context=None):
        """The Photo inline should be a part of the add Branch form."""
        self.inlines = (PhotoInline, )
        return super(BranchAdmin, self).add_view(request)

    def generate_notifications(self, request, queryset):
        """
        Call the populate_notifications() method in order to delete
        existing Email objects in a set of Branches and copy them again
        from the DefulatBranchContainer.
        """
        for branch in queryset:
            branch.populate_notifications()
    generate_notifications.short_description = _("Generate Emails")

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """
        Filter branch.organizers to Person objects that are marked as staff.
        """
        if db_field.name == 'organizers':
            kwargs['queryset'] = Person.objects.filter(is_staff=True)
        return super(BranchAdmin, self).formfield_for_manytomany(
            db_field,
            request,
            **kwargs
        )

    list_display = (
        'title',
        'slug',
        'site',
        'city',
        'country',
        'email',
        'branch_status',
        'is_active'
    )
    list_editable = ('is_active', 'branch_status',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('organizers', 'clusters')
    inlines = ()
    fieldsets = (
        # Translators: This is the a header in the branch admin form
        (_('Basic Info'), {
            'fields': (
                'title',
                'slug',
                'timezone',
                'language',
                'branch_status',
            )
        }),
        # Translators: This is the a header in the branch admin form
        (_('Contact Info'), {
            'fields': (
                'city',
                'state',
                'country',
                'email',
                'phone',
            )
        }),
        # Translators: This is the a header in the branch admin form
        (_('Website Content'), {
            'fields': (
                'header_copy',
                'intro_copy',
                'footer_copy'
            )
        }),
        # Translators: This is the a header in the branch admin form
        (_('Organizers'), {
            'fields': (
                'organizers',
                'clusters'
            )
        }),
    )


class VenueAdmin(BaseAdmin):
    """
    VenueAdmin is used to manage a Branch's Venues.

    * The address fields are used both in the frontend and to populate
      Emails that are sent related to a Schedule.
    * Venue.capacity DOES NOT create a limit on how many Students can register,
      it's just used for organizers to figure out Schedules.
    """
    def queryset(self, request):
        """
        Filter to Venues in Branches that are organized by the logged in user.
        """
        return super(VenueAdmin, self).queryset(
            request,
            Q(branch__in=request.user.branches_organized.all)
        )

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        """
        Select the country and state fields of the
        logged in user's branch.
        """
        # select the Branch's country
        if db_field.name == 'country':

            # first find the country of the first branch that's
            # organized by the logged in user
            initial_country = Branch.objects.filter(
                pk__in=request.user.branches_organized.all)[0].country

            # if the user has a default_branch set,
            # select its country instead.
            if request.user.default_branch is not None:
                initial_country = request.user.default_branch.country

            # set the actual initial value
            kwargs['initial'] = initial_country

        # select the Branch's state
        if db_field.name == 'state':
            # first find the state of the first branch that's
            # organized by the logged in user
            initial_state = Branch.objects.filter(
                pk__in=request.user.branches_organized.all)[0].state

            # if the user has a default_branch set,
            # select its state instead.
            if request.user.default_branch is not None:
                initial_state = request.user.default_branch.state

            # select the Branch's state
            kwargs['initial'] = initial_state

        return super(VenueAdmin, self).formfield_for_choice_field(
            db_field,
            request,
            **kwargs
        )

    list_display = (
        'title',
        'branch',
        'address_1',
        'city',
        'capacity',
        'is_active'
    )
    list_editable = (
        'address_1',
        'city',
        'capacity',
        'is_active',
    )
    fieldsets = (
        # Translators: This is the a header in the branch admin form
        (_('Basic Info'), {
            'fields': ('title', 'branch',)
        }),
        # Translators: This is the a header in the branch admin form
        (_('Contact Info'), {
            'fields': ('address_1', 'city', 'state', 'country', 'phone')
        }),
        # Translators: This is the a header in the branch admin form
        (_('Additional Info'), {
            'fields': ('capacity', 'resources',)
        }),
    )


class PersonAdmin(BaseAdmin):
    """
    PersonAdmin is used to add and edit people in the user's Branches.
    It includes Students, Teachers, and Organizers.
    """
    def queryset(self, request, q=None):
        """
        Annotate the queryset with counts of registrations and courses taught
        associated with the Person.
        """
        return super(PersonAdmin, self).queryset(
            request,
            Q(branches__in=request.user.branches_organized.all)
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'default_branch':
            kwargs['queryset'], kwargs['initial'] = self.filter_dbfield(
                request,
                Branch,
                Q(pk__in=request.user.branches_organized.all)
            )
        return super(PersonAdmin, self).formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )

    list_display = (
        'fullname',
        'email',
        'phone',
        'courses_taken_count',
        'courses_taught_count',
        'branches_string',
        'created',
    )
    search_fields = (
        'fullname',
        'email',
        'phone',
    )
    fields = (
        'fullname',
        'username',
        'email',
        'phone',
        'website',
        'bio',
    )
    #prepopulated_fields = {'slug': ('username',)}


class OrganizerAdmin(PersonAdmin):
    """
    """
    def change_password_link(self, obj):
        """
        """
        # link to change password admin form
        url = reverse('admin:password_change', args=(obj.pk,))
        html = '<a target="_blank" href="%s">change password</a>' % (url,)
        return mark_safe(html)
    change_password_link.short_description = _('change password')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'default_branch':
            kwargs['queryset'], kwargs['initial'] = self.filter_dbfield(
                request, Branch, Q(pk__in=request.user.branches_organized.all))

        return super(OrganizerAdmin, self).\
            formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = (
        'username',
        'fullname',
        'email',
        'branches_organized_string'
    )
    fields = (
        'username',
        'fullname',
        'email',
        'language',
        'default_branch',
        'groups'
    )
    inlines = (
        OrganizedBranchInline,
    )


class TeacherAdmin(PersonAdmin):
    """ TeacherAdmin lets you add and edit teachers in the Trade School system,
        A Teacher is a proxy model of Person.
        The only distinction is that a teacher is a person who taught
        at least 1 class
    """
    def queryset(self, request):
        """
        Filter queryset by the courses taught count,
        so only people who taught at least one class are returned.
        """
        return super(TeacherAdmin, self).queryset(
            request,
            Q(
                courses_taught_count__gt=0,
                branches__in=request.user.branches_organized.all
            )
        )

    list_display = (
        'fullname',
        'email',
        'phone',
        'courses_taught_count',
        'created'
    )


class StudentAdmin(PersonAdmin):
    """
    StudentAdmin lets you add and edit students in the Trade School system,
    A Student is a proxy model of Person.
    The only distinction is that a student is a person who
    registered to at least 1 class.
    """
    def queryset(self, request):
        """
        Filter queryset by the registration count,
        so only people who took at least one class are returned.
        """
        return super(StudentAdmin, self).queryset(
            request,
            Q(branches__in=request.user.branches_organized.all)
        )


class TimeAdmin(BaseAdmin):
    """
    TimeAdmin lets you add and edit time slots in the Trade School system.
    """
    def get_form(self, request, obj=None, **kwargs):
        form = super(TimeAdmin, self).get_form(request, obj, **kwargs)

        if obj is not None:
            form.base_fields['venue'].queryset = Venue.objects.filter(
                branch=obj.branch)

            form.base_fields['branch'].queryset = Branch.objects.filter(
                pk=obj.branch.pk)

        else:
            form.base_fields['venue'].queryset = Venue.objects.filter(
                branch__in=request.user.branches_organized.all)

            form.base_fields['branch'].queryset = Branch.objects.filter(
                pk__in=request.user.branches_organized.all)

            form.base_fields['branch'].initial = request.user.default_branch

        return form

    def queryset(self, request):
        return super(TimeAdmin, self).queryset(
            request,
            Q(branch__in=request.user.branches_organized.all)
        )

    list_display = (
        'start_time',
        'end_time',
        'venue'
    )
    fields = (
        'start_time',
        'end_time',
        'venue',
        'branch'
    )


class TimeRangeAdmin(BaseAdmin):
    """
    TimeRangeAdmin is a way to create batch time slots.
    A post save signal adds Time objects.
    """
    def queryset(self, request):
        return super(TimeRangeAdmin, self).queryset(
            request,
            Q(branch__in=request.user.branches_organized.all)
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'venue':
            kwargs['queryset'], kwargs['initial'] = self.filter_dbfield(
                request,
                Venue,
                Q(
                    is_active=True,
                    branch__in=request.user.branches_organized.all
                )
            )

        if db_field.name == 'branch':
            kwargs['queryset'], kwargs['initial'] = self.filter_dbfield(
                request,
                Branch,
                Q(pk__in=request.user.branches_organized.all)
            )
            kwargs['queryset'] = Branch.objects.filter(
                pk__in=request.user.branches_organized.all
            )

        return super(TimeRangeAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    list_display = (
        'start_time',
        'end_time',
        'start_date',
        'end_date',
        'venue'
    )
    fields = (
        'start_time',
        'end_time',
        'start_date',
        'end_date',
        'sunday',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'venue',
        'branch'
    )


class ScheduleAdmin(BaseAdmin):
    """
    ScheduleAdmin lets you add and edit class schedules,
    their barter items, registrations, and email templates.
    """
    def queryset(self, request):
        return super(ScheduleAdmin, self).queryset(
            request,
            Q(branch__in=request.user.branches_organized.all)
        )

    def formfield_for_dbfield(self, db_field, **kwargs):
        request = kwargs['request']
        formfield = super(
            ScheduleAdmin, self).formfield_for_dbfield(db_field, **kwargs)

        # if db_field.name == 'slug':
        #     if formfield.initial is None:
        #         formfield.initial = 'a'

        if db_field.name == 'venue':
            venue_choices_cache = getattr(request, 'venue_choices_cache', None)
            if venue_choices_cache is not None:
                formfield.choices = venue_choices_cache
            else:
                request.venue_choices_cache = formfield.choices
        return formfield

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Filter Venue, and Teacher objects to those who are related
        to Branches that are organized by the logged in user.
        """
        if db_field.name == 'venue':
            kwargs['queryset'], kwargs['initial'] = self.filter_dbfield(
                request,
                Venue,
                Q(branch__in=request.user.branches_organized.all)
            )
        if db_field.name == 'teacher':
            kwargs['queryset'] = Teacher.objects.filter(
                branches__in=request.user.branches_organized.all
            )

        return super(ScheduleAdmin, self).formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )

        return super(ScheduleAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.inlines = (
            BarterItemEditableInline,
            RegistrationInline,
            StudentConfirmationScheduleInline,
            TeacherConfirmationScheduleInline,
            TeacherClassApprovalScheduleInline,
            TeacherReminderScheduleInline,
            TeacherFeedbackScheduleInline,
            StudentReminderScheduleInline,
            StudentFeedbackScheduleInline,
            FeedbackInline,
        )
        return super(ScheduleAdmin, self).change_view(request, object_id)

    def add_view(self, request, form_url='', extra_context=None):
        self.inlines = (BarterItemEditableInline, )
        return super(ScheduleAdmin, self).add_view(request)

    def populate_notifications(self, request, queryset):
        """
        call the populate_notifications() method in order to
        reset email templates for the schedule.
        """
        for schedule in queryset:
            schedule.populate_notifications()
    populate_notifications.short_description = _("Generate Email Notifications")

    def teacher_fullname(self, obj):
        """
        Return related teacher so it can be used in list_display.
        """
        teacher = obj.teacher
        # link to teacher edit admin form
        url = reverse('admin:tradeschool_teacher_change', args=(teacher.pk,))
        html = '<a target="_blank" href="%s">%s</a>' % (url, teacher.fullname)
        return mark_safe(html)
    teacher_fullname.short_description = _('Teacher Fullname')

    def teacher_email(self, obj):
        """
        Return related teacher's email
        so it can be used in list_display.
        """
        html = '<a href="mailto:%s">%s</a>' % (
            obj.teacher.email, obj.teacher.email)

        return mark_safe(html)
    teacher_email.short_description = _('Teacher Email')

    def teacher_phone(self, obj):
        """
        Return related teacher's phone
        so it can be used in list_display.
        """
        return obj.teacher.phone
    teacher_phone.short_description = _('Teacher phone')

    def teacher_bio(self, obj):
        """
        Return related teacher's bio
        so it can be used in list_display.
        """
        return obj.teacher.bio
    teacher_bio.short_description = _('Teacher bio')

    def teacher_website(self, obj):
        """
        Return related teacher's website
        so it can be used in list_display.
        """
        return obj.teacher.website
    teacher_website.short_description = _('Teacher website')

    def get_form(self, request, obj=None, **kwargs):
        # Proper kwargs are form, fields, exclude, formfield_callback
        if obj:                     # obj is not None, so this is a change page
            fieldsets = (
                # Translators: This is the a header in the branch admin form
                (_('Class Info'), {
                    'fields': (
                        'title',
                        'description',
                        'max_students',
                        'slug'
                    )
                }),
                # Translators: This is the a header in the branch admin form
                (_('Teacher Info'), {
                    'fields': (
                        'teacher_fullname',
                        'teacher_email',
                        'teacher_phone',
                        'teacher_bio',
                        'teacher_website'
                    )
                }),
                # Translators: This is the a header in the branch admin form
                (_('Class Schedule'), {
                    'fields': (
                        'venue',
                        'start_time',
                        'end_time',
                        'schedule_status'
                    )
                }),
            )
            kwargs['fields'] = (
                'title',
                'description',
                'max_students',
                'venue',
                'start_time',
                'end_time',
                'schedule_status',
                'color',
            )
        return super(ScheduleAdmin, self).get_form(request, obj, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj:                                 # editing an existing object
            return self.readonly_fields + (
                'teacher_fullname',
                'teacher_email',
                'teacher_bio',
                'teacher_website',
                'teacher_phone',
                'branch'
            )
        return self.readonly_fields

    list_display = (
        'title',
        'teacher_fullname',
        'teacher_email',
        'start_time',
        'end_time',
        'venue',
        'schedule_status',
        'color',
        'created'
    )
    list_editable = (
        'start_time',
        'end_time',
        'venue',
        'schedule_status',
        'color',
    )
    list_filter = (
        'schedule_status',
        'venue',
        'start_time'
    )
    readonly_fields = ()
    search_fields = (
        'title',
        'get_teacher_fullname'
    )
    inlines = ()
    actions = (
        'approve_courses',
        'populate_notifications'
    )
    #prepopulated_fields  = {'slug': ('start_time',) }


class PendingScheduleAdmin(ScheduleAdmin):
    """
    """
    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        Set the schedule_status form field to 'pending'
        Since we are adding a pending schedule.
        """
        formfield = super(PendingScheduleAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)

        if db_field.name == 'schedule_status':
                formfield.initial = 'pending'
        return formfield

    def response_change(self, request, obj):
        """
        If the schedule_status was changed to 'approved',
        redirect to the ApprovedSchedule change-view
        """
        response = super(
            PendingScheduleAdmin, self).response_change(request, obj)

        # only redirect if the schedule was saved
        # by clicking on "save and continue editing"
        if isinstance(response, HttpResponseRedirect) and '_continue' in request.POST:
            # if the status was changed to 'approved',
            # redirect to approvedschedule change view
            if obj.schedule_status == 'approved':
                url = reverse(
                    'admin:tradeschool_approvedschedule_change',
                    args=(obj.pk,)
                )
                response['location'] = url

            # if the schedule was moved to a past date
            # redirect to pastchedule change view
            if obj.end_time < timezone.now():
                url = reverse(
                    'admin:tradeschool_pastschedule_change',
                    args=(obj.pk,)
                )
                response['location'] = url

        return response


class ApprovedScheduleAdmin(ScheduleAdmin):
    """
    """
    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        Set the schedule_status form field to 'approved'
        Since we are adding an approved schedule.
        """
        formfield = super(ApprovedScheduleAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)

        if db_field.name == 'schedule_status':
                formfield.initial = 'approved'
        return formfield

    def response_change(self, request, obj):
        """
        If the schedule_status was changed from 'approved',
        redirect to the PendingSchedule change-view
        """
        response = super(
            ApprovedScheduleAdmin, self).response_change(request, obj)

        # only redirect if the schedule was saved
        # by clicking on "save and continue editing"
        if (isinstance(response, HttpResponseRedirect) and '_continue' in request.POST):

            if obj.schedule_status is not 'approved':
                url = reverse(
                    'admin:tradeschool_pendingschedule_change',
                    args=(obj.pk,)
                )
                response['location'] = url

            # if the schedule was moved to a past date
            # redirect to pastchedule change view
            if obj.end_time < timezone.now():
                url = reverse(
                    'admin:tradeschool_pastschedule_change',
                    args=(obj.pk,)
                )
                response['location'] = url

        return response


class PastScheduleAdmin(ScheduleAdmin):
    """
    """
    def response_change(self, request, obj):
        """
        If the schedule_status was changed from 'approved',
        redirect to the PendingSchedule change-view
        """
        response = super(
            PastScheduleAdmin, self).response_change(request, obj)

        # only redirect if the schedule was saved
        # by clicking on "save and continue editing"
        if (isinstance(response, HttpResponseRedirect) and '_continue' in request.POST):
            # if the schedule was moved to a past date
            # redirect to pastchedule change view
            if obj.end_time > timezone.now():
                if obj.schedule_status == 'approved':
                    url = reverse(
                        'admin:tradeschool_approvedschedule_change',
                        args=(obj.pk,)
                    )
                else:
                    url = reverse(
                        'admin:tradeschool_pendingschedule_change',
                        args=(obj.pk,)
                    )
                response['location'] = url

        return response

    list_per_page = 20


class RegistrationAdmin(BaseAdmin):
    """
    RegistrationAdmin lets you add and edit the student registrations
    as well as the items each student signed up to bring.
    """
    def queryset(self, request):
        """
        Filter queryset by the registration count,
        so only people who took at least one class are returned.
        """
        return super(RegistrationAdmin, self).queryset(
            request,
            Q(schedule__branch__in=request.user.branches_organized.all)
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'student':
            kwargs['queryset'], kwargs['initial'] = self.filter_dbfield(
                request,
                Student,
                Q(branches__in=request.user.branches_organized.all)
            )

        if db_field.name == 'schedule':
            kwargs['queryset'], kwargs['initial'] = self.filter_dbfield(
                request,
                Schedule,
                Q(branch__in=request.user.branches_organized.all)
            )

        return super(RegistrationAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'items':
            # parsing the object id from the URL.
            # ** This is very ugly!
            # ** is there a way to get the obj from the request --Or
            try:
                registration_pk = int(request.path.split('/')[4])
                registration = Registration.objects.get(pk=registration_pk)
                kwargs['queryset'] = BarterItem.objects.filter(
                    schedule=registration.schedule)
            except ValueError:
                pass
        return super(RegistrationAdmin, self).formfield_for_manytomany(
            db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj:                             # editing an existing object
            return self.readonly_fields + (
                'student',
                'schedule'
            )
        return self.readonly_fields

    fields = (
        'student',
        'schedule',
        'items',
        'registration_status'
    )
    readonly_fields = ()
    list_display = (
        'student',
        'schedule',
        'registered_items',
        'registration_status'
    )
    filter_horizontal = (
        'items',
    )


class BarterItemAdmin(BaseAdmin):
    """
    BarterItemAdmin is used mostly for introspection.
    Editing BarterItem should be done within the related Schedule.
    """

    def queryset(self, request):
        """
        Filter queryset by the registration count,
        so only people who took at least one class are returned.
        """
        return super(BarterItemAdmin, self).queryset(
            request,
            Q(schedule__branch__in=request.user.branches_organized.all)
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'schedule':
            kwargs['queryset'], kwargs['initial'] = self.filter_dbfield(
                request,
                Schedule,
                Q(
                    branch__in=request.user.branches_organized.all,
                    schedule_status='approved'
                )
            )

        return super(BarterItemAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    list_display = (
        'title',
        'schedule'
    )
    search_fields = (
        'title',
        'schedule'
    )
    fields = (
        'title',
        'schedule'
    )


class PhotoAdmin(BaseAdmin):
    """
    """
    def queryset(self, request):
        """
        Filter queryset by the registration count,
        so only people who took at least one class are returned.
        """
        return super(PhotoAdmin, self).queryset(
            request,
            Q(branch__in=request.user.branches_organized.all)
        )

    list_display = (
        'get_thumbnail',
        'filename',
        'position',
        'branch'
    )

    def get_thumbnail(self, obj):
        """
        """
        return obj.thumbnail()
    get_thumbnail.short_description = _('Thumbnail')
    get_thumbnail.allow_tags = True


class PageForm(FlatpageForm):
    class Meta:
        model = Page


class PageAdmin(BaseAdmin):
    """
    """
    def queryset(self, request):
        """
        Filter queryset by the registration count,
        so only people who took at least one class are returned.
        """
        return super(PageAdmin, self).queryset(
            request,
            Q(branch__in=request.user.branches_organized.all)
        )

    form = PageForm
    fieldsets = (
        (None, {
            'fields': (
                'url',
                'title',
                'content',
                'branch',
                'is_visible',
                'is_active'
            )
        }),
    )
    list_display = (
        'title',
        'url',
        'branch',
        'is_visible'
    )
    list_filter = (
        'branch',
    )
    list_editable = (
        'is_visible',
    )
    search_fields = (
        'url',
        'title'
    )


class FeedbackAdmin(BaseAdmin, enhanced_admin.EnhancedModelAdminMixin):
    """
    """
    def queryset(self, request):
        """
        Filter queryset by the registration count,
        so only people who took at least one class are returned.
        """
        return super(FeedbackAdmin, self).queryset(
            request,
            Q(schedule__branch__in=request.user.branches_organized.all)
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'schedule':
            kwargs['queryset'] = Schedule.objects.filter(
                branch__in=request.user.branches_organized.all)

        return super(FeedbackAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    list_display = (
        'schedule',
        'feedback_type'
    )
    fields = (
        'schedule',
        'feedback_type',
        'content',
    )


class ClusterAdmin(BaseAdmin, enhanced_admin.EnhancedModelAdminMixin):
    """
    """
    def queryset(self, request):
        return super(ClusterAdmin, self).queryset(request, Q())

    list_display = (
        'name',
        'slug',
        'branches_string'
    )
    fields = (
        'name',
        'slug',
    )
    inlines = (
        ClusteredBranchInline,
    )


# register admin models
admin.site.register(Branch, BranchAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Cluster, ClusterAdmin)

admin.site.register(PendingSchedule, PendingScheduleAdmin)
admin.site.register(ApprovedSchedule, ApprovedScheduleAdmin)
admin.site.register(PastSchedule, PastScheduleAdmin)

admin.site.register(BarterItem, BarterItemAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Feedback, FeedbackAdmin)

admin.site.register(Person, PersonAdmin)
admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)

admin.site.register(Time, TimeAdmin)
admin.site.register(TimeRange, TimeRangeAdmin)

admin.site.register(Page, PageAdmin)
admin.site.register(Photo, PhotoAdmin)

admin.site.register(DefaultEmailContainer)

admin.site.register(StudentConfirmation)
admin.site.register(StudentReminder)
admin.site.register(StudentFeedback)
admin.site.register(TeacherConfirmation)
admin.site.register(TeacherClassApproval)
admin.site.register(TeacherReminder)
admin.site.register(TeacherFeedback)
