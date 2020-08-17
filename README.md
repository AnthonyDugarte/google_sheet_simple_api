# google sheet simple api

Simple google sheet API communication class for python based on official google api

## Installation

Currently, you can install google sheet simple api by its github's CVS url:

```bash
pip install git+https://github.com/AnthonyDugarte/google_sheet_simple_api.git@0.0.1#google_sheet_simple_api
```

Or, by appending it at your *requirements.txt*:

```bash
echo -e "\ngit+https://github.com/AnthonyDugarte/google_sheet_simple_api.git@0.0.1#google_sheet_simple_api" >> requirements.txt
```


## Usage

### Authorization

#### Default google Service Account

[Google Ref](https://google-auth.readthedocs.io/en/latest/reference/google.auth.html#google.auth.default)

- Make your google service account credentials file is available at the environment variable **GOOGLE_APPLICATION_CREDENTIALS**

```bash
export GOOGLE_APPLICATION_CREDENTIALS=~/credentials.json
```

Then in your script simply:

```python
import google.auth

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials, project = google.auth.default(scopes=SCOPES)

```

### For different alternatives

[Docs](https://google-auth.readthedocs.io/en/latest/reference/google.auth.html#module-google.auth)

### Initialization

After having gotten your google credentials file, you can instanciate your authorized client with:

```python
from google_sheet_simple_api import Sheet

# ...

sheet = Sheet(
    spreadsheet_id=YOUR_SPREADSHEET_ID,
    credentials=credentials,
)
```

### Methods available

#### Get values from sheet

```python
sheet.get(
    sheet_range="A1:C",
)
```

#### append values to sheet

```python
sheet.append(
    values=[[1, 2, 3]],
    sheet_range="A1:C",
)
```

#### Update values to sheet

```python
sheet.update(
    values=[[2, 4, 16]],
    sheet_range="A1:C",
)
```
