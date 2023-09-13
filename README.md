# HNG-Stage-Two

The Documentation for this API can be found below but it looks better on https://documenter.getpostman.com/view/29497397/2s9YC4TXmh 



GO TO https://documenter.getpostman.com/view/29497397/2s9YC4TXmh for a much better look at the documentation








STAGE-TWO
This API offers the basic CRUD operations.

﻿

﻿

GET
USERS
https://stage2hng-8d2g.onrender.com/users
The /users route will list every information we have in our database.

Example:
Python
import requests
response = requests.get("https://stage2hng-8d2g.onrender.com/users")
print(response.json())
JSON
{
    "users": [
        {
            "id": 1,
            "name": "example",
        }
    ]
}
﻿

POST
ADD USERS
https://stage2hng-8d2g.onrender.com//api?name=example8
The /api route creates a new user and adds the user to a database. It includes the following parameters:

name - A string that contains the name of the user [required]
Example:
Python
import requests
﻿
params = {
    'name': 'example2',
}
﻿
response = requests.get("https://stage2hng-8d2g.onrender.com/api", params=params)
print(response.json())
﻿
﻿

Response:                                                                                                                  Status: 200

﻿

JSON
{
    "status": {
        "success": "successfully added the new user to the database"
    }
}
﻿

﻿

Query Params
name
example8
GET
GET A USER
https://stage2hng-8d2g.onrender.com/api/{{user_id}}
The /{user_id} gets a user with the ID entered and returns a json with every information about it. It requires no parameters just the user ID in the endpoint.

﻿

EXAMPLE: 
Python
import requests


response = requests.get(url="https://stage2hng-8d2g.onrender.com/api/3")
print(response.json())

﻿

﻿

Response:

JSON
{
    "user": {
        "id": 1,
        "name": "example2",

    }
}
﻿

DELETE
DELETE USER
https://stage2hng-8d2g.onrender.com/api/delete/4
The /delete/{{user_id}} routes deletes a user from the database. 

EXAMPLE:
Python
import requests


response = requests.get(url="https://stage2hng-8d2g.onrender.com/api/delete/3")
print(response.json())

﻿

Response:

JSON
{
    "status": {
        "success": "successfully deleted the user"
    }
}
﻿

PUT
UPDATE USER
https://stage2hng-8d2g.onrender.com/api/update-user/{user_id}
Updates a user's name in the database. The user_id is required in the endpoint.

name — A string value that contains the user's name. 
Example:
﻿

Python
import requests

params = {
    "name": "example6"
}
response = requests.get(url="https://stage2hng-8d2g.onrender.com/api/update-user/3", params=params)
print(response.json())
﻿

﻿

Response:

JSON
{
    "status": {
        "success": "successfully updated the user info."
    }
}
﻿

﻿

﻿

Query Params
name
example5
