from django.contrib import messages

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext
from django.views.generic.edit import FormView

from esef_auth.forms.user_object_permission_bulk_create_form import UserObjectPermissionBulkCreateForm


class UserObjectPermissionBulkCreateView(FormView):
    form_class = UserObjectPermissionBulkCreateForm
    template_name = 'user_object_permission_bulk_create.html'


    def __init__(self, *args, **kwargs):
        from guardian.models import UserObjectPermission

        self.success_url = reverse('admin:%s_%s_changelist' % (UserObjectPermission._meta.app_label, UserObjectPermission._meta.module_name))
        super(UserObjectPermissionBulkCreateView, self).__init__(*args, **kwargs)


    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            count = form.save()
            messages.info(request, ugettext('%s user object permission is added.' % count))
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
