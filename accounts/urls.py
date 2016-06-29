from django.conf.urls import url

from accounts.views import registro_usuario_view, gracias_view, index_view, login_view, logout_view

urlpatterns = [
    url(r'^registro/$', registro_usuario_view, name='accounts.registro'),
    url(r'gracias/(?P<username>[\w]+)/$', gracias_view, name='accounts.gracias'),
    url(r'^$', index_view, name='accounts.index'),
    url(r'^login/$', login_view, name='accounts.login'),
    url(r'^logout/$', logout_view, name='accounts.logout'),

]
