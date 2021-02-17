from funcbaseview.views import *
from django.urls import path

urlpatterns = [
    path('welcome/', welcome_page_emp),
    path('save/', add_update_emp),
    path('edit/<int:eid>', edit_emp),
    path('delete/<int:eid>',delete_emp),

    path('adr/welcome/', welcome_page_adr),
    path('adr/save/', add_update_adr),
    path('adr/edit/<int:aid>',edit_adr),
    path('adr/delete/<int:aid>',delete_adr)
]