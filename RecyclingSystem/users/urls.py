from django.conf.urls import url
from . import views as userViews


urlpatterns = [
    url(r'^login$', userViews.signin, name='login'),
    url(r'^logout$', userViews.signout, name='logout'),
    url(r'^signup$', userViews.signup, name='signup'),
    url(r'^profile$', userViews.profile, name='profile'),
    url(r'^about$', userViews.about, name='about'),
]
