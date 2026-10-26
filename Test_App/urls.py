from django.urls import path

from . import aviews, apis

urlpatterns = [
    path('', aviews.home_page, name='home_page'),
    path('polling_unit/<int:uniqueid>/', aviews.polling_unit, name='polling_unit'),
    path('form_page/', aviews.form_page, name='form_page'),
    path('api/create_polling_data/', apis.create_polling_data, name='create_polling_data'),
]