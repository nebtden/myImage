import requests
import hashlib



data = '{"add_time":"1521525121","asn_no":"asn_no_1006","asn_items_list":[{"goods_num":1,"id":"10001","lineNo":0,"user_define1":"1","user_define2":"2"}],"asn_no2":"ASN0001_01","asn_type":"CC","carrier_id":"1","carrier_name":"SAISHI","customer_id":"1","supplier_name":"ssss","user_define1":"11","user_define2":"22","warehouse_id":"KE01"}'
app_key = 'huanqiu'
method = 'nos.outbound.create'

m = hashlib.md5()
before_md5 = '9fo5xxxda1sY9fo55mUo59fo55mUo'+data+'9fo5xxxda1sY9fo55mUo59fo55mUo'
m.update(before_md5.encode("utf8"))
encodeStr = m.hexdigest()

sign =encodeStr
post_data = {}
payload = {'data':data, 'app_key': app_key,"method":method,'sign':sign}

r = requests.post("http://kiliboss.kili.co/api/client/v2", data=payload)
print(r.text)