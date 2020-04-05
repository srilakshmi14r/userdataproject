from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from . models import *

# Create your views here.

def get_data(request):
    file_path = "/C/users/Sri/Downloads/Test JSON.json"

    with open(file_path, 'r') as f:
        json_data = f.read()

    converted_data = json.loads(json_data, encoding='utf-8')
    save_data = converted_data['members']
    for data in save_data:
        save_to_db = UserData(
            userid = data['id'],
            name = data['real_name'],
            timezone = data['tz']
        )
        save_to_db.save()
        for act_per in data['activity_periods']:
            save_act_period = ActivePeriod(
                start_time = act_per['start_time'],
                end_time = act_per['end_time'],
                user_id = data['id']
            )
            save_act_period.save()
    return JsonResponse(save_data, safe=False)
