import mal

_mal = mal.MAL(client_id='8fc58b161cb116994064500386b5c9ef', client_secret='0ab895ae043cf873c0d1bb313fb14f482d8d1ce2542dd397761f17780c036e60')

print(_mal.new_authorization_url())

token = input("Code verifier = ")






