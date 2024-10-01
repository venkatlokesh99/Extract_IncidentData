# cis6930fa24 -- Project0 -- Incident Data Extraction Project

Name: Venkat Lokesh Vejendla

## Assignment Description

This project is designed to extract incident data from the Norman, Oklahoma police department's publicly available PDF files. The data includes information such as the date/time of the incident, the incident number, location, nature of the incident, and an incident ORI. The extracted data is then stored in a SQLite database for easy querying and analysis. The project demonstrates the use of Python 3, SQL, regular expressions, and PDF data extraction techniques to process and manage real-world data.

## How to Install

To install and set up the project environment, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python 3 and `pipenv` installed.
3. Run the following command to install the required dependencies:
```bash
pipenv install
```
## How to Run

You can run the project with the following command:
```bash
pipenv run python main.py --incidents <url>
```
#### Example
```bash
pipenv run python project0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2024-08/2024-08-01_daily_incident_summary.pdf
```
![video](https://drive.google.com/file/d/1NtvLcKPgxst7AbpRyslSX1_9drzm6_pC/view?usp=drive_link)
## Functions

### main.py
- `main(url)`:
  - This function coordinates the workflow of downloading the incident PDF file, extracting the relevant incident data, and inserting it into a SQLite database. Finally, it prints a summary of incidents by their nature.

### download.py
- `fetch_incidents(url)`:
  - Downloads the PDF file from the provided URL using HTTP requests and saves it locally as `resources/incident.pdf`.

### extract.py
- `extract_incidents(pdf_path)`:
  - Extracts text from the provided PDF file and processes it to capture relevant incident fields. Returns a list of incidents with fields such as date/time, incident number, location, nature, and incident ORI.
  
- `process_incident_line(line, incidents_data)`:
  - Processes each line of extracted text, applying regex to identify the start of incidents and split them into relevant fields. Cleans and stores them in the `incidents_data` list.

- `extract_fields(valid_fields, incidents_data)`:
  - Extracts and validates the five fields (Date/Time, Incident Number, Location, Nature, and Incident ORI) from each processed line and appends them to the `incidents_data` list.

### database.py
- `connectdb()`:
  - Establishes and returns a connection to the SQLite database `resources/normanpd.db`.
  
- `createdb()`:
  - Creates the `incidents` table in the SQLite database if it does not already exist.
  
- `populatedb(incidents)`:
  - Inserts the extracted incident data into the `incidents` table in the SQLite database.
  
- `status()`:
  - Queries the database and prints the number of occurrences for each incident nature.
  
- `deletedb()`:
  - Deletes the existing `incidents` table to prevent data duplication when re-running the script.

## Database Development

The SQLite database `normanpd.db` is used to store the extracted incident data. It contains one table named `incidents`, which holds the following fields:

- `incident_time` (TEXT): Date and time of the incident
- `incident_number` (TEXT): Unique identifier for the incident
- `incident_location` (TEXT): Location of the incident
- `nature` (TEXT): Nature or type of the incident
- `incident_ori` (TEXT): ORI code related to the incident

Each time the program runs, the existing table is dropped, and a new table is created to store the latest data.

## Sample Output
```
911 Call Nature Unknown|6
Abdominal Pains/Problems|5
Alarm|13
Alarm Holdup/Panic|1
Animal Complaint|4
Animal Dead|5
Animal Injured|2
Animal Trapped|2
Animal at Large|2
Assault EMS Needed|3
Breathing Problems|6
Burglary|1
```
## Test Cases Overview

### test_download.py
- **Test Name**: `test_download`
  - Verifies the functionality of downloading incident data from the specified URL. It checks that the downloaded PDF matches the expected content by comparing the actual downloaded file against a predefined test file.

### test_extract.py
- **Test Name**: `test_extract`
  - Tests the extraction process from the downloaded PDF. It validates that the extracted data is in the expected format, ensuring that the resulting data is a list, contains the correct keys (DateTime, IncidentNumber, Location, Nature, IncidentType), and matches the length of the expected dataset.

### test_database.py
- **Test Name**: `test_connectdb`
  - Confirms the database connection works properly by checking the types of the cursor and database connection. It ensures that the database file exists and can execute a simple query.

- **Test Name**: `test_createdb`
  - Tests the creation of the database and its tables. It checks that the incidents table is successfully created after deleting any existing tables.

- **Test Name**: `test_populatedb`
  - Validates that the data insertion process works as expected by inserting mock incident data into the database and confirming that the correct number of records is present.

- **Test Name**: `test_status`
  - Assesses the functionality of the status function to ensure it prints the correct summary of incidents. It checks that the printed output includes specific incident types that were added to the database.

- **Test Name**: `test_deletedb`
  - Tests the deletion of the incidents table in the database. It verifies that the table is no longer present after the deletion operation.


## Bugs and Assumptions

### Bugs:
- The extraction of text from PDF files might not perform accurately on all PDFs, especially when formatting or layout variations occur in the source documents.
- Certain edge cases where the structure of incident data diverges from the expected format could lead to errors in extraction or incomplete data being captured.

### Assumptions:
- It is assumed that the input PDF files maintain a consistent format, particularly in terms of the patterns used for date/time, incident number, location, nature, and ORI.
- Only complete lines with all five required fields are processed; lines missing one or more fields are ignored.
- The PDF files are expected to have headers and footers, which are removed during the extraction process.

