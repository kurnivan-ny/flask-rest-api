# Flask REST API
[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) [API](https://en.wikipedia.org/wiki/API)s are commonly used to expose Machine Learning (ML) models to other services.
This folder contains an example REST API created using Flask to expose the logistic regression model from scikit-learn.

## Requirements
 
The "requirements file" is the file that lists the items to be installed ([Flask](https://palletsprojects.com/p/flask/) and [Scikit-learn](https://scikit-learn.org/stable/install.html)). Install with:

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
  "age":20,
  "avg_glucose_level":100,
  "bmi":30,
  "gender":"male",
  "hypertension":"no",
  "heart_disease":"yes",
  "ever_married":"no",
  "work_type":"Govt_job",
  "Residence_type":"Rural",
  "smoking_status":"Smokes"
}
```
- body response:
```JSON
{
  "prediction": "no"
}
```

An example python script to perform inference using requests is given in `example_request.py` or you can demo in `POSTMAN`
