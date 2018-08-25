# Lukkien Django app

## Tech stack
- Django 2.1
- Python 3.6


## Description
 - Web page with form to create a new customer
 - Web page with form to create a new shipping
 - settings for test and production
      - `ENVIRONMENT` var needs to be PRODUCTION for production settings
 
### Bonuses
 - forms validation: by Django `forms.ModelForm` and by additional custom validation
 - DRY: models inheritance
 - API (GraphQL): handle request strings (that looks almost like JSON strings) and 
 return response as string that may be easily parsed. In `debug` mode has web interface 
 that may be vieved by `/api` link. The same url handles all GraphQL requests.
 
GraphQL examples:
 - Get all customers:
   - request

    ```
        query{
          customers{
            id
            firstName
            lastName
            email
            dateOfBirth
          }
        }
    ```

   - response

    ```
    {
      "data": {
        "customers": [
          {
            "dateOfBirth": "1987-01-08",
            "email": "voronov.a.g@gmail.com",
            "firstName": "Andrey",
            "id": 1,
            "lastName": "Voronov"
          },
          {
            "dateOfBirth": "1987-01-08",
            "email": "a.g@gmail.com",
            "firstName": "Andrey",
            "id": 2,
            "lastName": "Voronov"
          }
        ]
      }
    }
    ```
- Get all shippings:
   - request

    ```
    query{
      shippings{
        id
        firstName
        lastName
        phoneNumber
        email
        postalCode
        city
        street
        houseNumber
      }
    }
    ```

   - response

    ```
    {
      "data": {
        "shippings": [
          {
            "id": 1,
            "firstName": "Andrey",
            "lastName": "Voronov",
            "phoneNumber": "+3937451596",
            "email": "voronov.a.g@gmail.com",
            "postalCode": "04214",
            "city": "Kyiv",
            "street": "Obolonskiy avenue 34-A, app. 89",
            "houseNumber": "23"
          },
          {
            "id": 2,
            "firstName": "Andrey",
            "lastName": "Voronov",
            "phoneNumber": "+2937451596",
            "email": "a.g@gmail.com",
            "postalCode": "04211",
            "city": "Kyiv",
            "street": "Obolonskiy avenue",
            "houseNumber": "23"
          }
        ]
      }
    }
    ```

## Deploy
- install and activate virtual environment(virtualenv example)
    - `virtualenv -p python3.6 venv`
    - `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py runserver`
- `python manage.py migrate`
 
