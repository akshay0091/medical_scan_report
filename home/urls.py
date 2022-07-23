from django.urls import path
from . import views
from django.conf import settings
from  django.conf.urls.static import  static



urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('about', views.about, name='about'),
    path('kidney', views.kidney, name='kidney'),
    path('pnemonia', views.pnemonia, name='pnemonia'),
    path('malaria', views.malaria, name='malaria'),
    path('skin_cancer', views.skin_cancer, name='skin_cancer'),
    path('tb', views.tb, name='tb'),
    path('tb_result', views.tb_result, name='tb_result'),
    path('skin_result', views.skin_result, name='skin_result'),
    path('maleria_result', views.maleria_result, name='maleria_result'),
    path('pnemonia_result', views.pnemonia_result, name='pnemonia_result'),
    path('kidney_result', views.kidney_result, name='kidney_result'),

              ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
 #       urlpatterns += static(settings.MEDIA_URL,
  #                            document_root=settings.MEDIA_ROOT)