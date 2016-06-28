from django.conf.urls import url

from accounts.views import registro_usuario_view , gracias_view

urlpatterns = [
    url(r'^registro/$',registro_usuario_view, name='accounts.registro'),
    url(r'gracias/(?P<username>[\w]+)/$', gracias_view, name='accounts.gracias'),
]
