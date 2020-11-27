#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:24:43 2020

@author: rinkishi
"""

from django.urls import path
from . import views



urlpatterns = [
        path('<int:id>/<nickname>/',views.index,name='index'),
]