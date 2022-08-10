# Flask REST API
[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) [API](https://en.wikipedia.org/wiki/API)s are commonly used to expose Machine Learning (ML)  models to other services.
This folder contains an example REST API created using Flask to expose the linear regression model from pickle.

## Requirements

- [Flask](https://palletsprojects.com/p/flask/) is required. Install with:

  ```shell
  $ pip install Flask
  ```
  
- [Scikit-learn](https://scikit-learn.org/stable/install.html) is required. Install with:

  ```shell
  $ pip install scikit-learn
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
