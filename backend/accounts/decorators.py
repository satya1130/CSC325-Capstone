from functools import wraps

from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseForbidden


def admin_required(view_func):
    """US-08: only signed-in staff/admin users may reach administrative views.

    Anonymous visitors are sent to the login page; signed-in members who are
    not admins receive 403. Enforced on the server, never by hiding buttons.
    """

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        if not request.user.is_staff:
            return HttpResponseForbidden("Administrator access required.")
        return view_func(request, *args, **kwargs)

    return wrapper
