
from aliyun.log.etl_core import *

TRANSFORM_EVENT_lookup = [
    ( NO_EMPTY('csv_field'), ('csv_field', CSV("f_v1,f_v2,f_v3")) ),
    ( NO_EMPTY('dsv_field'), ('dsv_field', CSV("f_d1,f_d2,f_d3", sep='#', quote='|')) ),
    ( ANY, ([("f1", "c1"), ("f2", "c2")], LOOKUP('./data4_lookup_csv1.txt', ["d1", "d2"]) ) ),
    ( ANY, ("f1",LOOKUP({'a': "a_new", '*': "unknown"}, "f1_new")) ),
    ( NO_EMPTY('split2'), ("split2", SPLIT))
]

KV_FIELDS_data = r'kv_data\d+'

DROP_FIELDS_origin = ["csv_field", 'dsv_field', 'data', 'f1', 'f2', r'kv_data\d+']


@condition(NO_EMPTY("split"))
def sls_en_split(event):
    return [{"split": v} for v in event['split'].split(',')]
