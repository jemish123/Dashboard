from django.shortcuts import render
from django.http import HttpResponse
from app.models import Jsondatatable

# Create your views here.
def index(request):
    queryset = Jsondatatable.objects.all()
    
    filter_set = Jsondatatable.objects.values_list('end_year', 'topic', 'sector', 
                                              'region', 'country', 'source',
                                              'pestle')
    
    filter_dict = {
        'end_years': set(), 'topics': set(), 'sectors': set(), 'regions': set(),
        'countries': set(), 'sources': set(), 'pestles': set()
    }
    
    for record in filter_set:
        if record[0]:
            filter_dict['end_years'].add(record[0])
        if record[1]:
            filter_dict['topics'].add(record[1])
        if record[2]:
            filter_dict['sectors'].add(record[2])
        if record[3]:
            filter_dict['regions'].add(record[3])
        if record[4]:
            filter_dict['countries'].add(record[4])
        if record[5]:
            filter_dict['sources'].add(record[5])
        if record[6]:
            filter_dict['pestles'].add(record[6])
        # if record[0]:
        #     filter_dict['end_years'] = record[0]
        
    for key in filter_dict.keys():
        filter_dict[key] = sorted(filter_dict[key])
        
    return render(request, 'index.html', context={"records": queryset, "filters": filter_dict})
