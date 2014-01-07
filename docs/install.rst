Install
=======

To get this running on your local machine:

1. Set up a virtualenv (using Python >=3.2 binary)
2. Install all dependencies into your virtualenv:

    pip install -r requirements/local.txt

3. Set your database setting as an environment variable named DATABASE_URL:

    export DATABASE_URL=postgis://<username>:<password>@<hostname>/<database name>