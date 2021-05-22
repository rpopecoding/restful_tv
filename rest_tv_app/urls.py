from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('new', views.new),
    path('create', views.create),
    path('shows/<int:render_id>', views.show_data),
    path('shows/edit/<int:render_id>', views.edit),
    path('make_edit', views.make_edit),
    path('shows/delete/<int:render_id>', views.delete_confirm),
    path('make_delete', views.make_delete)
    ]