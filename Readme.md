### Data Modeling - Music app 

Data Modeling and ETL pipelines using python 

- Application purpose - future data analysis for a music streaming app

### Data Schema 
Fact table

- songplays - records in log data associated with song plays

      songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
    
Dimension tables:

- users - users in the app 
   
      user_id, first_name, last_name, gender, level
        
- songs - songs in the music database
        
      song_id, title, artist_id, year, duration
        
- artists - artists in the music dataset
        
      artist_id, name, location, latitude, longitude
        
- time - timestamp of records 
       
      start_time, hour, day, week, month, year, weekday
        
### Project files

queries.py - contains sql queries for dropping,creating and inserting data.

create_tables.py - contains code for setting up the database.

etl.py - reads and processes the data.

main.py - Initializes the above mentioned files
