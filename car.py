# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 23:25:02 2023

@author: tcran
"""

from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
