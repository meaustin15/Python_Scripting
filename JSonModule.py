import json

js = {"office":
     {"employees":[
        { "name": "Matt",
           "age":22,
           "email":"x@gmail.com"
           },
        { "name": "Mick",
           "age":28,
           "email":"y@gmail.com"
           }
     ],
         "parking":{
             "location": "Lot X",
             "style": "covered",
             "price": 0
         }
     }
 }

y = json.dumps(js)

datastore = json.loads(y)

print(datastore["office"]["employees"])