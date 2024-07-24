import time
import jwt
import json

# Чтение закрытого ключа из JSON-файла
with open('configs/env/authorized_key.json', 'r') as f: 
  obj = f.read() 
  obj = json.loads(obj)
  private_key = obj['private_key']
  key_id = obj['id']
  service_account_id = obj['service_account_id']

now = int(time.time())
payload = {
        'aud': 'https://iam.api.cloud.yandex.net/iam/v1/tokens',
        'iss': service_account_id,
        'iat': now,
        'exp': now + 3600
      }

# Формирование JWT.
encoded_token = jwt.encode(
    payload,
    private_key,
    algorithm='PS256',
    headers={'kid': key_id}
  )

#Запись ключа в файл
with open('jwt_token.txt', 'w') as j:
   j.write(encoded_token) 
   
# Вывод в консоль
print(encoded_token)

