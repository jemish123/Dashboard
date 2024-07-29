from django.shortcuts import render
from django.http import JsonResponse
import json
import psycopg2


# Create your views here.
def index(request):
    with open('jsondata.json', 'r') as f:
        data = f.read()
        data = json.loads(data)

    # try:
    #     conn = psycopg2.connect(database="JsonData", 
    #                             user="postgres",
    #                             password="1234",
    #                             host="localhost",
    #                             port=5432)
    #     cur = conn.cursor()
        
    #     for record in data:

    #         values = (record['sector'], record['topic'], record['insight'], record['url'], record['region'], record['country'], record['title'], record['end_year'], record['intensity'],
    #                   record['start_year'], record['impact'], record['added'], record['published'], record['relevance'], record['pestle'], record['source'], record['likelihood'])
    #         sql = "ALTER TABLE jsondatatable ADD COLUMN id serial primary key;"

    #         cur.execute(sql)
    #         conn.commit()
    # except Exception as e:
    #     print(e)
    # finally:
    #     cur.close()
    #     conn.close()

    return JsonResponse({'data': data})