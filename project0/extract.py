import pypdf
import re

def process_incident_line(line,incidents_data):
    date_pattern = r'\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{2}'
    # Get the starting positions of each match
    datesFound = re.finditer(date_pattern, line)
    # If there are matches, split the line at each match
    parts=[]
    if datesFound:
        split_positions = [date.start() for date in datesFound]
        # print(split_positions)
        
        parts=[line[start:end].strip() for start, end in zip(split_positions, split_positions[1:] + [len(line)])]
        # print(parts)
        # process each parts obtained
        cleaned_parts = [part for part in parts if part]
        for segment in cleaned_parts:
            split_segment = re.split(r"\s{4,}", segment)
            valid_fields = [value for value in split_segment if value] # remove empty fields
            extract_fields(valid_fields, incidents_data)
    else:
        # In case of no matches, split the line directly
        parts =  [line.strip()]
        split_line = re.split(r"\s{4,}", line)
        valid_fields = [value for value in split_line if value] # remove empty fields
        extract_fields(valid_fields, incidents_data)

    return incidents_data

# Clean and extract data from the pdf file
def extract_incidents(pdf_path):
    """
    Extracts incidents from the PDF data.
    Returns a list of incidents with the following fields:
    Date / Time, Incident Number, Location, Nature, Incident ORI
    """
    with open(pdf_path, 'rb'):
        reader = pypdf.PdfReader(pdf_path)
        content = ""
        for page in reader.pages:
            content += page.extract_text(extraction_mode="layout")
   
    lines = content.splitlines("")[3:-1] # removing headers/footers from the pdf file
    incidents_data = []
    lines = [line for line in lines if line.strip()]
    for line in lines:
       if line:
            process_incident_line(line,incidents_data)

    return incidents_data

# Extract the fields from cleaned and processed data
def extract_fields(valid_fields, incidents_data):
    """
    Splits the line into relevant fields: Date / Time, Incident Number, Location, Nature, and Incident ORI.
    """
    if(len(valid_fields) == 5):
        extracted_data = {
        "DateTime": valid_fields[0].strip(),
        "IncidentNumber": valid_fields[1].strip(),
        "Location": valid_fields[2].strip(),
        "Nature": valid_fields[3].strip() if valid_fields[3].strip() else "",
        "IncidentType": valid_fields[4].strip()
        }
        
        # Append the data to the list
        incidents_data.append(extracted_data)