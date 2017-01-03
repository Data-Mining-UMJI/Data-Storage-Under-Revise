#! /bin/bash

# Customized Settings:
# Install dir for MonogoDB
path="/usr/local/mongodb/bin"

# Export program
export_prog="./mongoexport "

# csv file type
file_format="--type=csv "

# Specify the data fields for each entry 
field="-f _id,title,likes " 

# Specify the target database
database="-d test "             

# Specify the target collection
collection="-c col "

# Specify the output file name
output="-o ./test.csv "



# Run the export program:
# Change to the install dir for MonogoDB
cd ${path}

# Run the export command to generate ".csv" files
${export_prog}${file_format}${field}${database}${collection}${output}