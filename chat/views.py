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

@require_http_methods(['GET'])
def index_view(request):
    return render(request, 'home.html')

def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)

    return data



@require_http_methods(['POST'])
def chat_view(request):
    # gcp authentication and project variables
    GOOGLE_AUTHENTICATION_FILE_NAME = "django-dialogflow-307207-a6ca460023ff.json"
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path

    GOOGLE_PROJECT_ID = "django-dialogflow-307207"
    session_id = "12345"
    context_short_name = "no_name"

    # handle input value depending on text or file input
    if request.content_type == 'application/json':

        input_dict = convert(request.body)
        input_text = json.loads(input_dict)['text']
        print('input_text is: ', input_text)
        input_value = input_text
    
    else:
        file_input = request.FILES['file']
        print('file is', file_input)
        file_name = upload_blob('as-testing-bucket', request.FILES['file'], request.FILES['file'].name)
        input_value = 'file is '+ file_name
        print('text is: ', input_value)

    context_name = "projects/" + GOOGLE_PROJECT_ID + "/agent/sessions/" + session_id + "/contexts/" + \
               context_short_name.lower()

    #set up parameters and request to call dialogflow detectintent endpoint
    parameters = dialogflow.types.struct_pb2.Struct()
    context_1 = dialogflow.types.context_pb2.Context(
        name=context_name,
        lifespan_count=2,
        parameters=parameters
    )
    query_params_1 = {"contexts": [context_1]}
    language_code = 'en'

    # call dialogflow detectintent endpoint and save result in response 
    response = detect_intent_with_parameters(
        project_id=GOOGLE_PROJECT_ID,
        session_id=session_id,
        query_params=query_params_1,
        language_code=language_code,
        user_input=input_value
        )
    print('response is: ',response.query_result.fulfillment_text)

    #return httpresponse received from the detectintent API
    return HttpResponse(response.query_result.fulfillment_text, status=200)
