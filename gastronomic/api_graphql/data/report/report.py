import graphene
from unidecode import unidecode
import datetime
import locale
import json
from datetime import datetime
from datetime import timedelta
from payments.models import Payment
from enterprises.models import Enterprise
from graphql_relay.node.node import from_global_id

class Report(graphene.ObjectType):   
    report_date = graphene.String()
    payment_value = graphene.Int()

class Reports(graphene.ObjectType):
    enterprise= graphene.ID()       
    start_date = graphene.DateTime()
    final_date = graphene.DateTime()
    report_list = graphene.List(Report)
    total_value = graphene.Float()


def get_query_report(enterprise,start_date,final_date):
    enterprise = from_global_id(enterprise)[1]
    query_reports=Payment.objects.filter(order__date__range=[start_date,final_date],order__details__product__enterprise=enterprise,order__status="Entregado").values('order__details__product__enterprise__name' ,'order__date','payment_value').distinct()
    return query_reports
def get_data_report(query_reports,start_date,final_date):
    
    reports_as_obj_list = [] 
    total=0
    try:
        for query_report in query_reports: 
            report = Report(query_report.get('order__date').strftime("%Y-%m-%d %H:%M:%S"),query_report.get('payment_value')) 
            reports_as_obj_list.append(report)
            total=report.payment_value+total

        object_reports = Reports(query_report.get('order__details__product__enterprise__name'),start_date, final_date, reports_as_obj_list,total)
        return object_reports
    except: 
        return None

