# Flask REST API
[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) [API](https://en.wikipedia.org/wiki/API)s are commonly used to expose Machine Learning (ML) models to other services.
This folder contains an example REST API created using Flask to expose the logistic regression model from scikit-learn.

## Requirements
 
The "requirements file" is the file that lists the items to be installed. Install with:

```shell
$ pip install -r requirements.txt
```

## Run

After Flask installation run:

```shell
$ python restapi.py
```

## API
- method: `POST`
- endpoint: `/predict`
- body request:
```JSON
{
    "image":"square face.jpg"
}
```
- body response:
```JSON
{
    "prediction face": "Square"
}
```

An example python script to perform inference using requests is given in `example_request.py` or you can demo in `POSTMAN`