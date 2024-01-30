# MediManager-Backend

The DB Design based on which initial-commit is done is hereby :
https://dbdocs.io/buddhirajsahu/Medi-Managerv1?view=relationships

Password will be shared in the group.


## Getting this repo

Create a file first in your pc by 

```
mkdir medimanager && cd medimanager
```


Copy and paste the following in your termianl while inside the "medimamnger" file

```
git clone git@github.com:ehr66777/Medi-Manager-Backend.git
```

## Activating the virtual environment
The virtual environment in created as .env
activate that by running the following command :
```
source .env/bin/activate
```

or delete the .env file and recreate again

```
python3 -m venv .env
```
Ad then activate it again

## Installing dependencies

The requiremnets.txt file is added to this repo 
run it by running this :

```
pip install -r requirements.txt
```
## Adding Sample Data for Test Purposes

Adding the Specialization, required to create appointments
```
python3 manage.py specialization_load
```

For adding symptoms use this :

```
python3 manage.py symptom_load
```

For adding some commonly used Medicines -- use this :

```
python3 manage.py medicine_load
```
# Login and Toekn Authentication from React Side :

## Registration/Sign-up Using Djoser

Just for now , email and password are required params for this SignUp process
(First Name and LastName , you can skip and empty string will be paseed as default value.) <<NOT RECOMMENDED>>

```json
{
  email: 'patient1@email.com',
  'first_name': 'Patient1',
  'last_name': 'Last1',
  'password': 'PASSWORD_PLACEHOLDER'
}
```
The react code to signup is here :

```node.js
const http = require("http");

const options = {
  "method": "POST",
  "hostname": "127.0.0.1",
  "port": "8000",
  "path": "/auth/users/",
  "headers": {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Content-Type": "application/json"
  }
};

const req = http.request(options, function (res) {
  const chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
  });
});

req.write(JSON.stringify({
                          email: 'patient1@email.com',
                          first_name: 'Patient1',
                          last_name: 'Last1',
                          password: 'bigbang13'
                        }));
req.end();

```

## Log-in 

The Login request in react is here >>> 
PATH : auth/jwt/create

```node.js

const http = require("http");

const options = {
  "method": "POST",
  "hostname": "127.0.0.1",
  "port": "8000",
  "path": "/auth/jwt/create/",
  "headers": {
    "Accept": "*/*",
    "Content-Type": "application/json"
  }
};

const req = http.request(options, function (res) {
  const chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
  });
});

req.write(JSON.stringify({email: 'patient1@email.com', password: 'bigbang13'}));
req.end();

```

The Login output will be containing the "JWT-TOKEN" and coming like this >>>

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjY5NTUwNiwiaWF0IjoxNzA2NjA5MTA2LCJqdGkiOiJiOTAwNWUxNTg5ZTY0NmJjOWMyYmE1NTIxYTgyYTEyMiIsInVzZXJfaWQiOjZ9.h8DgGCTjgNkuZWAjrLekSv9gyBsNdKZ3Um2d6uT5K4M",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NjEyNzA2LCJpYXQiOjE3MDY2MDkxMDYsImp0aSI6ImY3YWVjNDdlZWJhODRjZTA5OGNjMjQwZGRlZWM1OGZkIiwidXNlcl9pZCI6Nn0._av7Umn3pJbtHIY1Usj7ujyh4EiLnHJKXHSVVZV-yao"
}
```

## Verifying JWT Token

- The Token coming from login-response will be used in the Payload now : "Token place_your_token_here"
```node.js
const http = require("http");

const options = {
  "method": "POST",
  "hostname": "127.0.0.1",
  "port": "8000",
  "path": "/auth/jwt/verify/",
  "headers": {
    "Accept": "*/*",
    "Content-Type": "application/json"
  }
};

const req = http.request(options, function (res) {
  const chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
  });
});

req.write(JSON.stringify({
  token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NjEyNzA2LCJpYXQiOjE3MDY2MDkxMDYsImp0aSI6ImY3YWVjNDdlZWJhODRjZTA5OGNjMjQwZGRlZWM1OGZkIiwidXNlcl9pZCI6Nn0._av7Umn3pJbtHIY1Usj7ujyh4EiLnHJKXHSVVZV-yao'
}));
req.end();
```

The output for this will be coming like this 200 RESPONSE

- The 'id' will be necessary we have to filer the alloted appointements for a user (Doctor).

```json
{ }
```

## Refreshing JWT Token

- The Refresh Token coming from login-response will be used in the Payload now : "place_your_token_here"
```node.js
const http = require("http");

const options = {
  "method": "POST",
  "hostname": "127.0.0.1",
  "port": "8000",
  "path": "/auth/jwt/refresh/",
  "headers": {
    "Accept": "*/*",
    "Content-Type": "application/json"
  }
};

const req = http.request(options, function (res) {
  const chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
  });
});

req.write(JSON.stringify({
  refresh: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjY5NTUwNiwiaWF0IjoxNzA2NjA5MTA2LCJqdGkiOiJiOTAwNWUxNTg5ZTY0NmJjOWMyYmE1NTIxYTgyYTEyMiIsInVzZXJfaWQiOjZ9.h8DgGCTjgNkuZWAjrLekSv9gyBsNdKZ3Um2d6uT5K4M'
}));
req.end();

```

The output for this will be coming like this 200 RESPONSE

- The 'id' will be necessary we have to filer the alloted appointements for a user (Doctor).

```json

{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NjEzNDcyLCJpYXQiOjE3MDY2MDkxMDYsImp0aSI6ImUzYjI0MGM3YzgyMjRkNDViMjNjY2NjMThhMmFiYWE4IiwidXNlcl9pZCI6Nn0.Wd4erYmUnzTBbrrp6qM-2K2rlsCR-tAaBuop8ik9chs"
}

```
##Fetching Medicine Data using JWT token as auth-object

The format is over here :
> Authorization: JWT <token>

```node.js
const http = require("http");

const options = {
  "method": "GET",
  "hostname": "127.0.0.1",
  "port": "8000",
  "path": "/api/v1/medicine-master/",
  "headers": {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Authorization": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NjEzNDcyLCJpYXQiOjE3MDY2MDkxMDYsImp0aSI6ImUzYjI0MGM3YzgyMjRkNDViMjNjY2NjMThhMmFiYWE4IiwidXNlcl9pZCI6Nn0.Wd4erYmUnzTBbrrp6qM-2K2rlsCR-tAaBuop8ik9chs",
    "Content-Type": "application/json"
  }
};

const req = http.request(options, function (res) {
  const chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
  });
});

req.write(JSON.stringify({
  token: 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NjEzNDcyLCJpYXQiOjE3MDY2MDkxMDYsImp0aSI6ImUzYjI0MGM3YzgyMjRkNDViMjNjY2NjMThhMmFiYWE4IiwidXNlcl9pZCI6Nn0.Wd4erYmUnzTBbrrp6qM-2K2rlsCR-tAaBuop8ik9chs'
}));
req.end();
```

















