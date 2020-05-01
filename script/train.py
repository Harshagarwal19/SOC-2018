#Depricated file not used anymore
#Relevent for local testing

import cognitive_face as CF
from camapp.keys import api_key, base_url   
KEY = api_key                           # Replace with a valid Subscription Key here
CF.Key.set(KEY)
BASE_URL = base_url                     # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)
group_id = "1"

x=CF.person.lists(group_id,0,100)
print(x)