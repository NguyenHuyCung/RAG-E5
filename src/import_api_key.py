import os

# Thiết lập biến môi trường
os.environ['GOOGLE_API_KEY'] = 'AIzaSyAG1n6P9uXqmNs8ghbPKu2QDZvgsm_7pzs'

# Kiểm tra xem biến môi trường đã được thiết lập chưa
print(os.environ.get('GOOGLE_API_KEY'))
