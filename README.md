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

## Registration/Sign-up 

Just for now , username is a required param for this ( which can be handled from the Frontend --> @atiprad by making usename and email taking same input)

```json
{
  "username": "Patient_1", << E-mail can be passed 
  "password": "password" ,
  "re_password" : "password" ,
  "email" : "patient1@gmail.com"
}
```
The react code to signup is here :

```node.js
const http = require("http");

const options = {
  "method": "POST",
  "hostname": "127.0.0.1",
  "port": "8000",
  "path": "/api/v1/signup/",
  "headers": {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Authorization": "Bearer cdf631e10658c36c4768552a351654fe163c630e ",
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
  username    : 'Patient_1',
  password    : 'password',
  re_password  : 'password',
  email        : 'patient1@gmail.com'
}));
req.end();
```

## Log-in 

The Login request in react is here >>>

```node.js
const http = require("http");

const options = {
  "method": "POST",
  "hostname": "127.0.0.1",
  "port": "8000",
  "path": "/api/v1/login/",
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

req.write(JSON.stringify({username: 'superadmin', password: 1729}));
req.end();
```

The Login output will be containing the "TOKEN" and coming like this >>>

```json
{
  "id": 1,
  "username": "superadmin",
  "token": "5421781bb6d98fb75501a715873aea9d42901a17"
}
```

## Getting Session User-detail (Authenticated user for now )

- The Token coming from login-response will be used in this format : "Token place_your_token_here"
```node.js
const http = require("http");

const options = {
  "method": "GET",
  "hostname": "127.0.0.1",
  "port": "8000",
  "path": "/api/v1/current_user/",
  "headers": {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Authorization": "Token 5421781bb6d98fb75501a715873aea9d42901a17" // TOKEN PLACEHOLDER IS HERE
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

req.end();
```

The output for this will be coming like this :

- The 'id' will be necessary we have to filer the alloted appointements for a user (Doctor).

```json
{
  "id": 1,
  "username": "superadmin",
  "email": "superadmin@gmail.com",
  "first_name": "Firstname",
  "last_name": "Lastname"
}
```
# ! TODO : WATCH-TOWER for the Admin















