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
            "email": "johnsong@gmail.com",
            "firstName": "Andrew",
            "id": 1,
            "lastName": "Travolra"
          },
          {
            "dateOfBirth": "1987-01-08",
            "email": "example@gmail.com",
            "firstName": "Jason",
            "id": 2,
            "lastName": "Born"
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
            "firstName": "Don",
            "lastName": "Jackson",
            "phoneNumber": "+3337451226",
            "email": "don@gmail.com",
            "postalCode": "23214",
            "city": "Kiev",
            "street": "Exanple avenue",
            "houseNumber": "23"
          },
          {
            "id": 2,
            "firstName": "Joe",
            "lastName": "Vernon",
            "phoneNumber": "+29374515336",
            "email": "a.g@gmail.com",
            "postalCode": "02311",
            "city": "Kiev",
            "street": "Big street",
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
 
