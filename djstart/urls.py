#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:24:43 2020

@author: rinkishi
"""

from django.urls import path
from . import views



urlpatterns = [
        path('my_name_is_<nickname>.I_am_<int:age>_years_old.',views.index,name='index'),
]