#! /bin/bash

# Current working directory
cwd=$(pwd)

# Customized Settings:
# Install dir for MonogoDB
path="/usr/local/mongodb/bin"

# Export program
import_prog="./mongoimport "

# csv file type
file_format="--type=csv "

# Specify the data fields for each entry 
field="-f sepal_length,sepal_width,petal_length,petal_width,label " 

# Specify the target database
database="-d "$1          

# Specify the target collection
collection=" -c "$2

# Specify the output file name
output=" --file="${cwd}"/"$3

# Omit the 1st line
# omit_header="--headerline"


# Run the export program:
# Change to the install dir for MonogoDB
cd ${path}

# Run the export command to generate ".csv" files
${import_prog}${file_format}${field}${database}${collection}${output}