from django.shortcuts import render
# from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

from apps.login.models import User

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

# Metodo permitir inicio de sesión a ciertos usuarios

USER_FIELDS = ['email', 'username']

def get_whitelisted_emails():
    whitelisted_domains_emails = []
    get_whitelisted_domains_emails = User.objects.values_list('email')
    print(get_whitelisted_domains_emails)
    return [email for _, email in whitelisted_domains_emails]


def create_user(strategy, details, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    allowed_emails = get_whitelisted_emails()

    fields = dict((name, kwargs.get(name, details.get(name)))
                  for name in strategy.setting('USER_FIELDS', USER_FIELDS))
    if not fields:
        return

    if fields['email'] in allowed_emails:
        return {
            'is_new': True,
            'user': strategy.create_user(**fields)
        }
    return

# Logout no funcional
'''
def logout(request):
    auth_logout(request)
    return redirect('login')
'''


def login_success(request):
    if request.user.is_staff:
        # user es admin
        return redirect('administrador_index')
    else:
        return redirect('usuario_index')



# Redireccion tomando en cuenta rol
'''
def login_success(request):
    if request.user.rol == 'admin':
        # user es admin
        return redirect('administrador_index')
    else:
        return redirect('usuario_index')
'''

def accounterror(request):
    return redirect('login')