from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.load_index_page, name='index'),
    # path('about', views.loadAboutPage, name='about_page'),
    path('admin', views.load_minerals_page, name='admin'),
    path('details/<mineral_id>', views.load_details_page),
    # path('excursions', views.loadExcursionsPage, name='excursions_page'),
    # path('excursion/<excursion_id>', views.loadExcursionPage),
    # path('excursion/delete/<excursion_id>', views.deleteExcursion),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)