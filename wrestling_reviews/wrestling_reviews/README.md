# Wrestling Reviews Project

This project is a Django-based web app where wrestling fans can:
- Add reviews for matches and events.
- View wrestlers, events, and match details.
- Interact with reviews (comments, likes, ratings).
- Freely provide their opinions or POVs

Apps included:
- users
- wrestlers
- events
- reviews

### POSTMAN tests
### User Endpoints

*Post* /api/users/ 
*request body*:
json
{
    "username":"salem5",
    "email":"salemmahmoud6@gmail.com",
    "password": "*********"
}

*Put* /api/users/(id number)/

*request body*:
json
{
    "username":"salem55",
    "email":"salemmahmoud56@gmail.com,
    "password":"**********"
}

*Patch* /api/user/(id number)/

*request body*:
json
{
    "email":"salemmahmoud5@gmail.com"
}

*Delete* /api/user/(id number)/

### Wrestlers Endpoints

*Post* /api/wrestlers/

*request body*:

json{
"name":"John Cena",
"country":"Massachusetts - USA",
"debut_year":1999,
"birth_date":"1977-04-23",
"debut_date":"1999-11-05"
}

*Put* /api/wrestlers/(id number)/

*request body*:
json
{
    "name":"John Cena",
    "country":"Massachusetts - USA",
    "debut_year":2005,
    "birth_date":"1977-04-23",
    "debut_date":"1999-11-05"
}

*Patch* /api/wrestlers/(id number)/

*request body*:
json
{
    "debut_year":1999
}

*Delete* /api/wrestlers/(id number)/

### Events Endpoints

*Post* /api/events/

*request body*:
json
{
    "name":"All In: London (2024)",
    "date":"2024-08-25",
    "location":"London - England",
    "promotion":"AEW",
    "description":"test description",
    "is_ppv":true
}

*Put* /api/events/(id number)/

*request body*:
json
{
    "name":"All In: London (2025)",
    "date":"2024-08-25",
    "location":"London - England",
    "promotion":"AEW",
    "description":"test description",
    "is_ppv":true
    }

*Patch* /api/events/(id number)/

*request body*:
json
{
    "name":"All In: London (2024)"
}

*Delete* /api/events/(id number)/


### Reviews Endpoints

*Post* /api/reviews/

*request body*:
json
{
"wrestlers":[3,4],
"match_title":"Test Match",
"review_content":"Nice!",
"rating":4.55,
"event":1,
"user":1
}

*Put* /api/reviews/(id number)/

*request body*:
json
{
"wrestlers":[3,5],
"match_title":"Test Match",
"review_content":"Nice!",
"rating":4.55,
"event":1,
"user":1
}

*Patch* /api/reviews/(id number)/

*request body*:
json
{
"wrestlers":[3,4]
}

*Delete* /api/reviews/(id number)/