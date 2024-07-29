from django.shortcuts import render
from django.http import HttpResponse
from app.models import Jsondatatable

# Create your views here.
def index(request):
    queryset = Jsondatatable.objects.all()
    
    # Data filtering for filter fields
    filter_fields = Jsondatatable.objects.values_list('end_year', 'topic', 'sector', 'region', 'source', 'country', 'pestle')
    filter_dict = {'end_years': set(), 'topics': set(), 'sectors': set(), 'regions': set(), 'sources': set(), 'countries': set(), 'pestles': set()}
    
    for record in filter_fields:
        (end_year_filter, topic_filter, sector_filter, region_filter, source_filter, country_filter, pestle_filter) = \
            (record[0], record[1], record[2], record[3], record[4], record[5], record[6])
            
        if end_year_filter:
            filter_dict['end_years'].add(end_year_filter)
        if topic_filter:
            filter_dict['topics'].add(topic_filter)
        if sector_filter:
            filter_dict['sectors'].add(sector_filter)
        if region_filter:
            filter_dict['regions'].add(region_filter)
        if source_filter:
            filter_dict['sources'].add(source_filter)
        if country_filter:
            filter_dict['countries'].add(country_filter)
        if pestle_filter:
            filter_dict['pestles'].add(pestle_filter)
            
            
    filter_dict['end_years'] = sorted(filter_dict['end_years'])
    filter_dict['topics'] = sorted(filter_dict['topics'])
    filter_dict['sectors'] = sorted(filter_dict['sectors'])
    filter_dict['regions'] = sorted(filter_dict['regions'])
    filter_dict['sources'] = sorted(filter_dict['sources'])
    filter_dict['countries'] = sorted(filter_dict['countries'])
    filter_dict['pestles'] = sorted(filter_dict['pestles'])
    
    print(type(filter_dict['end_years']))
    
        
    return render(request, 'index.html', context={"records": queryset, "filters": filter_dict, "numbers": {'a': filter_dict['topics']}, 'b': [50, 50, 50, 55]})
