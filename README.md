# Billing system using Machine Learning
## Image Classification using tensorflow and UI using django
- model - MobilenetV2
- db - SQLite3
- other libraries -
## Features

- Detect products from image
- Calculate rate and total bill for every customer
- Save invoices in db
- Generate timely sale reports 
- Responsive UI

# How to run
- navigate to `server` folder
- install required libraries from `requirements.txt` (virtual env preferred)
```sh
pip install -r requirements.txt
```
### Required libraries
>Tensorflow
>Django
>Numpy
>Pandas
>Keras
>Joblib

Navigate to the folder with manage.py in it and run this command

```sh
python manage.py runserver
```

> Note: database stored in db.sqlite

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT


