from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
import dialogflow
import os
import json
from google.cloud import storage

