# SqlAlchemy-Challenge

~~ ~~Love the name of this challenge.~~ ~~ In this challenge I will use Python and SQLAlchemy to analyze and explore some climate data. It will be divided into two parts.

---

## Part 1: Analyze and Explore the Climate Data

In this section, I’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. Specifically, I’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, I will complete the following steps:

1. Use the SQLAlchemy create_engine() function to connect to your SQLite database.

2. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

3. Link Python to the database by creating a SQLAlchemy session.

> [!IMPORTANT]
> Remember to close your session at the end of your notebook.

4. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

---

## Part 2: Design Your Climate App

Now that I’ve completed my initial analysis, I’ll design a Flask API based on the queries that I just developed. To do so, I'll use Flask to create a route as follows:

1. /

    Start at the homepage.

    List all the available routes.

2. /api/v1.0/precipitation

    Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

    Return the JSON representation of your dictionary.

3. /api/v1.0/stations

    Return a JSON list of stations from the dataset.

4. /api/v1.0/tobs

    Query the dates and temperature observations of the most-active station for the previous year of data.

    Return a JSON list of temperature observations for the previous year.

5. /api/v1.0/<start> and /api/v1.0/<start>/<end>

    Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

    For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

    For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


> [!NOTE]
> This code was written by DAVID RUVALCABA, starter code was given by edX Boot Camps LLC. The dataset was given by Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and #T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, (https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml)
