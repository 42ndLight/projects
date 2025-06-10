#!/bin/bash

#Python BackEnd quick setup

python3 -m venv virt
source virt/bin/activate

pip install django
pip install djangorestframework
pip install pyscopg2-binary
pip install django-cors-headers

