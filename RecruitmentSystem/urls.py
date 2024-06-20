from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("studentapplication/", views.studentapplication, name='studentapplication'),
    path('create_ocpresident/', views.create_ocpresident, name='create_ocpresident'),
    path("login/", views.login, name="login"),
    path("oc_page/", views.oc_page, name="oc_page"),
    path("oc_bureau_leader_page/", views.oc_bureau_leader_page, name="oc_bureau_leader_page"),
    path("oc_president_page/", views.oc_president_page, name="oc_president_page"),

    #OC President
    #Add new event
    path("oc_president_page/add_event/", views.add_event, name="add_event"),

    #Update (Add user & Update User & Delete User)
    path("oc_president_page/update_page", views.update_page, name='update_page'),

    #Add user
    path('oc_president_page/update_page/create_oc/', views.create_oc, name='create_oc'),
    path('oc_president_page/update_page/create_ocbureauleader/', views.create_ocbureauleader, name='create_ocbureauleader'),

    #Add user no.2
    path('oc_president_page/update_page/applications/', views.application_list, name='application_list'),
    path('oc_president_page/update_page/applications/<int:pk>/update/', views.update_application_status, name='update_application_status'),

    #Update user
    path("oc_president_page/update_page/update_oc_list/", views.update_oc_list, name="update_oc_list"),
    path("oc_president_page/update_page/update_oc_list/update_oc/<int:pk>/", views.update_oc, name="update_oc"),
    path("oc_president_page/update_page/update_ocbureauleader_list/", views.update_ocbureauleader_list, name="update_ocbureauleader_list"),
    path("oc_president_page/update_page/update_ocbureauleader_list/update_ocbureauleader/<int:pk>/", views.update_ocbureauleader, name="update_ocbureauleader"),

    #Delete user
    path("oc_president_page/update_page/delete_oc_list/", views.delete_oc_list, name="delete_oc_list"),
    path("oc_president_page/update_page/delete_oc_list/delete_oc/<int:pk>/", views.delete_oc, name="delete_oc"),
    path("oc_president_page/update_page/delete_ocbureauleader_list/", views.delete_ocbureauleader_list, name="delete_ocbureauleader_list"),
    path("oc_president_page/update_page/delete_ocbureauleader_list/delete_ocbureauleader/<int:pk>/", views.delete_ocbureauleader, name="delete_ocbureauleader"),

    #OC Bureau Leader
    #Add OC to join Event
    path("oc_bureau_leader_page/select_oc_for_event/", views.select_oc_for_event, name="select_oc_for_event"),
]