# oneomeapi

![example workflow](https://github.com/geethasohita/oneomeapi/actions/workflows/github-actions.yml/badge.svg)


This is a `Flask-SqlAlchemy` application which is deployed on [Heroku](https://oneomeapi.herokuapp.com/).
Below are some details regarding this project.

This app has REST endpoints to Create, Read, Update and Delete `Vaccine` resource in a postgres database.

Since this app is deployed on heroku, all these REST endpoints are available for you to hit. Below are the endpoints and the git repo has [postman collection](https://github.com/geethasohita/oneomeapi/blob/master/oneomeapi.postman_collection.json) checked in that you can use.

```
GET https://oneomeapi.herokuapp.com/vaccine
GET https://oneomeapi.herokuapp.com/vaccine?name=Moderna
POST https://oneomeapi.herokuapp.com/vaccine
PUT https://oneomeapi.herokuapp.com/vaccine/<vaccine_id>
DELETE https://oneomeapi.herokuapp.com/vaccine/<vaccine_id>
```
`CI` for this app is done through [github actions](https://github.com/geethasohita/oneomeapi/actions) 
and Heroku-Github integration for `CD`.


