# Simple Pokemon API
A simple RESTful API for a Pokemon database implemented using Python and Flask. All pokemon data is from GitHub user fanzeyi - https://github.com/fanzeyi/pokemon.json

## How to run
1. Either fork or download the repository
2. Install flask dependency using `npm i` command
3. Run the program

## Requests
Below you can find a list a list of all requests inside the API.

* ### Get all Pokemons
`GET /pokemons/`
#### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 197652
    Server: Werkzeug/1.0.1 Python/3.7.4
    Date: Mon, 08 Mar 2021 19:37:27 GMT
    
    [A list of all pokemons]
    
* ### Get Pokemon by ID
`GET /pokemons/:id`
#### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 251
    Server: Werkzeug/1.0.1 Python/3.7.4
    Date: Mon, 08 Mar 2021 19:38:41 GMT
    
    {"Pokemon":{"base":{"Attack":55,"Defense":40,"HP":35,"Sp. Attack":50,"Sp. Defense":50,"Speed":90},"id":25,"name":{"chinese":"\u76ae\u5361\u4e18","english":"Pikachu","french":"Pikachu","japanese":"\u30d4\u30ab\u30c1\u30e5\u30a6"},"type":["Electric"]}}
    
* ### Get Pokemon by Name
`GET /pokemons/:name`
#### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 251
    Server: Werkzeug/1.0.1 Python/3.7.4
    Date: Mon, 08 Mar 2021 19:40:49 GMT
    
    {"Pokemon":{"base":{"Attack":55,"Defense":40,"HP":35,"Sp. Attack":50,"Sp. Defense":50,"Speed":90},"id":25,"name":{"chinese":"\u76ae\u5361\u4e18","english":"Pikachu","french":"Pikachu","japanese":"\u30d4\u30ab\u30c1\u30e5\u30a6"},"type":["Electric"]}}
    
* ### Get all Pokemon Types
`GET /types/`
#### Response 

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 1350
    Server: Werkzeug/1.0.1 Python/3.7.4
    Date: Mon, 08 Mar 2021 19:41:45 GMT
    
    [A list of all pokemon types]
    
* ### Get all Pokemon of a type
`GET /types/:type`

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 15626
    Server: Werkzeug/1.0.1 Python/3.7.4
    Date: Mon, 08 Mar 2021 19:42:54 GMT
    
    [A list of all Pokemon of a type]

* ### Get all Pokemon sorted by a property
`GET /pokemons/sorted/:property`

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 197652
    Server: Werkzeug/1.0.1 Python/3.7.4
    Date: Mon, 08 Mar 2021 19:44:09 GMT
    
    [A list of all Pokemon sorted by a property]

* ### Get all Pokemon reverse sorted by a property
`GET /pokemons/sorted/:property/Reversed`

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 197652
    Server: Werkzeug/1.0.1 Python/3.7.4
    Date: Mon, 08 Mar 2021 19:44:29 GMT
    
    [A list of all Pokemon reverse sorted by a property]
