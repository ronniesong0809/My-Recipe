# My Recipe

Copyright (c) 2018-2019 Ronnie Song

An incremental construction of a scalable recipe website that utilizes Machine Learning APIs.

## Tech Stack and Tools

Python, Flask, Bootstrap Framework, Google Vision API, Google Translate API, Nutritionix API, and Yelp API

## Installation Option 1:

**1. Go to the GCP, open Cloud Shell.**
```shell
$ gcloud services enable translate.googleapis.com
$ gcloud services enable vision.googleapis.com
$ gcloud iam service-accounts create myrecipemlapis
$ gcloud iam service-accounts keys create myrecipemlapis.json --ian-account myrecipemlapis@
$ $DEVSHELL_PROJECT_ID.iam.gserviceaccount.com
```

**2. In cloud shell, build the project.**
```shell
$ git clone https://github.com/ronniesong0809/my-recipe.git && cd my-recipe
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

**3. Run the project.**
```shell
$ python main.py
```
**4. Deploy the project.**
``` shell
$ gcloud app deploy
```
## Installation Option 2:

**1. Go to the GCP Console, then go to the [Create service account key](https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.33111806.-1379095962.1564736461) page:**
- From the Service account list, select New service account.
- In the Service account name field, enter a name.
- From the Role list, select Project > Owner.
- Click Create. A JSON file that contains your key downloads to your computer.
- Open your favourite terminal. For example Git Bash or Cmder.

**2. Build the project.**
```shell
$ git clone https://github.com/ronniesong0809/my-recipe.git && cd my-recipe
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

**3. Setting the environment variable GOOGLE_APPLICATION_CREDENTIALS.**
```shell
$ set GOOGLE_APPLICATION_CREDENTIALS=[PATH]

For example:
$ $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\[FILE_NAME].json"
```

**4. Run the project.**
```shell
$ python main.py
```

## Reference
- [Cloud Translation Quickstart: Using Client Libraries](https://cloud.google.com/translate/docs/quickstart-client-libraries#client-libraries-install-python)
- [Cloud Vision Quickstart: Using Client Libraries](https://cloud.google.com/vision/docs/quickstart-client-libraries#client-libraries-install-python)

## License

This program is licensed under the "MIT License". Please see the file LICENSE in the source distribution of this software for license terms.
