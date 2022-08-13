# Flask REST API
[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) [API](https://en.wikipedia.org/wiki/API)s are commonly used to expose Machine Learning (ML)  models to other services.
This folder contains an example REST API created using Flask to expose the linear regression model from scikit-learn.

## Requirements

The "requirements file" is the file that lists the items to be installed ([Flask](https://palletsprojects.com/p/flask/) and [Scikit-learn](https://scikit-learn.org/stable/install.html)). Install with:

```shell
$ pip install -r requirements.txt
```

## Run
Run the REST API using commands:

```shell
$ python restapi.py
```

## REST API
- method: `POST`
- endpoint: `/predict`
- body request:
```JSON
{
  "age":20,
  "bmi":30,
  "smoker":"yes",
  "gender":"male"
}
```
- body response:
```JSON
{
  "prediction": 26273.42
}
```

An example python script to perform inference using requests is given in `example_request.py` or you can demo in `POSTMAN`
