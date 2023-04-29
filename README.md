# Simple CSO service

It is a simple service to call CSO classifier.


IT MUST BE RUN ON PYTHON 3.8 ONLY. Using more modern version will break it.


It is because `cso-classifier` used an outdated library at the time of writing.


# Setup
1. Create a virtual environment using `virtualenv`  and activate it.
2. Install every dependencies by `pip install -r requirements.txt`
3. Run `cso_setup.py` to download the ontology.
4. To run server, use `uvicorn main:app --reload` for development purpose.


For the production build, please consult FastAPI documentation. It is pretty much work in progress.


# How to use

Send a POST request to `/extract` using this schema.

```json
{
  "title": "title of the paper",
  "abstract": "English abstract of the paper"
}
```

The response type is same as `CSOClassifier.run(paper)`. So, consult the CSO classifier for detailed doucmentation.