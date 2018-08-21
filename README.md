repository to hold the exercises from the UCSF NLP group

# overview of pipeline
- input data: __data_export.json
- get keys from file: **json_parse.py**
- this outputs a file called clinical_items.txt
- copy this file into a new file called tmp_clinical_items.txt
- update the tmp file
  - append ", y" to fields of interest
- run **ref_update.py** to add "n" to all other fields
- run **filter.py** to create a new file (filtered_data.txt), which contains only the fields of interest
- to determine whether the selected fields are useful:
  - run **column_analyze.py**
  - this outputs a text file for each field (in a subdirectory)
