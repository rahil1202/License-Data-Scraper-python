# License Data Scraper

🚗 Scrapes Driving License data from government websites

## How to Run

### 1. Install Required Packages

```bash
pip install -r requirements.txt
```

### 2. Run the Python CLI Application

For example, with a License number "DL0420110149646" and DOB "09-02-1976":

```bash
python main.py -dl DL-0420110149646 -dob 09-02-1976
```

It takes 2 arguments `-dl` and `-dob`. Run `python main.py --help` for more information.

### 3. Output

The output is displayed on the screen and saved as `driver_data.json` in the project root directory.

## Sample Output

```bash
random data
$ python main.py -dl DL-0420110149646 -dob 09-02-1976
```

```json
Data received ->

{
  "Class Of Vehicle": [
    {
      "COV Category": "NT",
      "COV Issue Date": "01-Mar-2011",
      "Class Of Vehicle": "ADPVEH"
    }
  ],
  "Driver Details": {
    "Current Status": "ACTIVE",
    "Date Of Issue": "01-Mar-2011",
    "Holder's Name": "ANURAG BREJA",
    "Last Transaction At": "ZONAL OFFICE, WEST DELHI, JANAKPURI",
    "Old / New DL No.": "DL-0420110149646"
  },
  "Validity": {
    "Hazardous Valid Till": "NA",
    "Hill Valid Till": "NA",
    "Non-Transport": {
      "from": "01-Mar-2011",
      "to": "08-Feb-2026"
    },
    "Transport": {
      "from": "NA",
      "to": "NA"
    }
  }
}

Driver Details Successfully stored in driver_data.json
```

## Project File Structure

```
- License-Data-Scraper/
  - main.py
  - scraper/
    - __init__.py
    - getDetails.py
    - getTableData.py
  - requirements.txt
  - README.md
```