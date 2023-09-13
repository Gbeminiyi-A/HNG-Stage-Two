# HNG-Stage-Two

The Documentation for this API can be found below but it looks better on [https://documenter.getpostman.com/view/29497397/2s9YC4TXmh ](https://documenter.getpostman.com/view/29497397/2s9YC4TXmh)



GO TO [https://documenter.getpostman.com/view/29497397/2s9YC4TXmh](https://documenter.getpostman.com/view/29497397/2s9YC4TXmh) for a much better look at the documentation





STAGE-TWO
This API offers the basic CRUD operations.

﻿

GET
USERS
https://stage2hng-8d2g.onrender.com/api
The /api route will list every information we have in our database.

Example:
Python
import requests
response = requests.get("https://stage2hng-8d2g.onrender.com/api")
print(response.json())
JSON
{
    "users": [
        {
            "id": 1,
            "name": "example",
            "value": "value"
        }
    ]
}
﻿

POST
ADD USERS
https://stage2hng-8d2g.onrender.com/api?name=John Doe&value=Artist
The /api route creates a new user and adds the user to a database. It includes the following parameters:

name - A string that contains the name of the user [required]
value- A string that contains anything about the user
Example:
Python
import requests
params = {
    'name': 'example2',
    "value": 'example_value'
}
response = requests.get("https://stage2hng-8d2g.onrender.com/api", params=params)
print(response.json())
Response: Status: 200

JSON
{
    "status": {
        "success": "successfully added the new user to the database"
    }
}
﻿

Query Params
name
John Doe
value
Artist
GET
GET A USER
https://stage2hng-8d2g.onrender.com/api/3
The /{user_id} gets a user with the ID entered and returns a json with every information about it. It requires no parameters just the user ID in the endpoint.

EXAMPLE:
Python
import requests
﻿
﻿
response = requests.get(url="https://stage2hng-8d2g.onrender.com/api/3")
print(response.json())
﻿
Response:

JSON
{
    "user": {
        "id": 1,
        "name": "example2",
        "value": "example_value"
﻿
    }
}
﻿

DELETE
DELETE USER
https://stage2hng-8d2g.onrender.com/api/5
The /delete/{{user_id}} routes deletes a user from the database.

EXAMPLE:
Python
import requests
﻿
﻿
response = requests.get(url="https://stage2hng-8d2g.onrender.com/api/3")
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
https://stage2hng-8d2g.onrender.com/api/4?value=artist
Updates a user's name in the database. The user_id is required in the endpoint.

name — A string value that contains the user's name. [optional]
value - A string value that contains anything about the user [optional]
Example:
Python
import requests
params = {
    "name": "example6",
    "value": "example_value"
}
response = requests.get(url="https://stage2hng-8d2g.onrender.com/api/update-user/3", params=params)
print(response.json())
Response:

JSON
{
    "status": {
        "success": "successfully updated the user info."
    }
}
﻿

﻿

Note:
You can edit one or both values of the users. Just use the right key for whichever value you want to update.

Query Params
name
example5
value
artist
