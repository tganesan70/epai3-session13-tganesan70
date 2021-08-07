# Session 13 Readme file 
# Assignment details:

## Goal 1
Create a lazy iterator that will return a named tuple of the data in each row. 
The data types should be appropriate - i.e. if the column is a date, you should 
be storing dates in the named tuple, if the field is an integer, then it should 
be stored as an integer, etc.

## Goal 2
Calculate the number of violations by car make.

### Note:
Try to use lazy evaluation as much as possible - it may not always be possible 
though! That's OK, as long as it's kept to a minimum.

# Approach 1 - Problem 1
    * Create a read function which yields the data records one by one from the file
    * Create a list of namedtuple lazily for each record which reads from the file
      one record at a time
      
# Approach 1 - Problem 2
    * Create a read function which yields the data records one by one from the file
    * Create a list of namedtuple lazily for each record which reads from the file
      one record at a time.
        - Use proper data format conversions of fields from string format
    * Traverse through the records to obtain the statistics for the violation by
      a given car brand.
      
# Approach 2 - Problem 1
    * Create read function which yields the data records one by one and creates a 
      list of namedtuples
        - Use proper data format conversions of fields from string format
      
# Approach 2 - Problem 2
    * Create a read funtion which yields one nametuple from the list of namedtuples
      lazily
        - Use proper data format conversions of fields from string format
    * Traverse thru the records lazily to collect the staticstics for the given car brand
 
 # Approach 3 - Using Class iterator (Not completed as of now)
    * Create a class which stores only the critical information such as filename, selected
      car brand or date or license plate state, etc. 
    * The lazy reader function yields one data record at a time 
        - Use proper data format conversions of fields from string format to namedtuple fields
    * Static functions to perform each of the tasks such as statistics for violation by car 
      makes, vehicle types, registration state, etc.
      
 # Test cases
    1. Check for creation of non-empty records from file.
    2. Chech for correct number of records as in the file.
    3. Check the format for all fields in the namedtuple.
    4. Check the number of violations for the given make using method1.
    5. Check the number of violations for the given make using method2.
    6. Check the match between methods 1 and 2.
