from lazop_sdk import LazopClient, LazopRequest

# Konfigurasi API
url = 'https://auth.lazada.com/rest'
app_key = '130375'
app_secret = '1Ja8KbVhJtfXV7eC8mFB5lpORt6Jvyc7'
auth_code = '0_130375_4cZKaUmlmWVbJf220LYYOVtG13110'

# Membuat client dan request
client = LazopClient(url, app_key, app_secret)
request = LazopRequest('/auth/token/create')

# Menambahkan parameter API
request.add_api_param('code', auth_code)
#request.add_api_param('uuid', 'This field is currently invalid, do not use this field please')

# Mengeksekusi permintaan dan mendapatkan respon
response = client.execute(request)

# Menampilkan tipe dan isi respon
print(response.type)
print(response.body)


client = LazopClient('https://api.lazada.co.id/rest', app_key ,app_secret)
request = LazopRequest('/orders/get','GET')
#request.add_api_param('update_before', '2024-08-30T16:00:00+08:00')
request.add_api_param('sort_direction', 'ASC')
#request.add_api_param('offset', '0')
#request.add_api_param('limit', '50')
#request.add_api_param('update_after', '2024-07-01T09:00:00+08:00')
#request.add_api_param('sort_by', 'updated_at')
request.add_api_param('created_before', '2024-08-15T16:00:00+08:00')
request.add_api_param('created_after', '2024-08-01T09:00:00+08:00')
request.add_api_param('status', 'returned')
response = client.execute(request, '50000601123y5WdZ0f0gjREVwE8hDx7nyvf16f9092akDQIZeQulczjsPRXlR1wr')
#print(response.type)

for order in response.body['data']['orders']:
  print(order)
  print()