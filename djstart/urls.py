#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:24:43 2020

@author: rinkishi
"""

from django.urls import path
from  . import views



urlpatterns = [
        path('',views.index,name='index'),
        path('create',views.create,name='create'),
        path('edit/<int:num>',views.edit,name='edit'),
        path('delete/<int:num>',views.delete,name='delete'),
]