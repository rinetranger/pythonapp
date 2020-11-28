#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:24:43 2020

@author: rinkishi
"""

from django.conf.urls import url
from . views import DjstartView



urlpatterns = [
        url(r'',DjstartView.as_view(),name='index')
]