Created following the tutorial at
https://www.django-rest-framework.org/tutorial/quickstart/

to troubleshoot the bug
https://github.com/tfranzel/drf-spectacular/issues/422

If you deploy with `python manage.py runserver`, you can test by running
```
curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/
```
