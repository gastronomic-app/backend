import graphene

import datetime
import locale
import json
from datetime import datetime
from datetime import timedelta
from payments.models import Payment
from enterprises.models import Enterprise

class Report(graphene.ObjectType):   
    report_date = graphene.String()
    payment_value = graphene.Int()

class Reports(graphene.ObjectType):
    enterprise= graphene.String()       
    start_date = graphene.DateTime()
    final_date = graphene.DateTime()
    report_list = graphene.List(Report)
    total_value = graphene.Float()


def get_query_report(enterprise,start_date,final_date):

        enterprise=Enterprise.objects.get(pk=enterprise)
        business_hours = json.loads(enterprise.business_hours)
        locale.setlocale(locale.LC_TIME, '')
        current_day=datetime.today().strftime('%A')
        #fecha de cierre del establecimiento obtenida de la bd
        close_date=(business_hours[current_day])['horaF']
        hour_final = "{:d}:{:02d}".format(final_date.hour, final_date.minute)
        if(hour_final>close_date):
            final_date=final_date-timedelta(days=1)
        query_reports=Payment.objects.filter(delivery__delivery_time__range=[start_date,final_date],delivery__order__details__product__enterprise=enterprise,delivery__status="1").values('delivery__order__details__product__enterprise__name' ,'delivery__delivery_time','payment_value').distinct()
        return query_reports

def get_data_report(query_reports,start_date,final_date):
    
    reports_as_obj_list = [] 
    total=0
    try:
        for query_report in query_reports: 
            report = Report(query_report.get('delivery__delivery_time').strftime("%Y-%m-%d %H:%M:%S"),query_report.get('payment_value')) 
            reports_as_obj_list.append(report)
            total=report.payment_value+total

        object_reports = Reports(query_report.get('delivery__order__details__product__enterprise__name'),start_date, final_date, reports_as_obj_list,total)
        return object_reports
    except: 
        return None

