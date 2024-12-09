# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


#################################################
# Database Setup
#################################################
# Create engine and reflect database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# reflect an existing database into a new model

# reflect the tables


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)




#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available routes."""
    return (
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the last 12 months of precipitation data."""
    # Find the most recent date in the dataset
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = pd.to_datetime(most_recent_date) - pd.DateOffset(years=1)

    # Query precipitation data for the last 12 months
    results = (
        session.query(Measurement.date, Measurement.prcp)
        .filter(Measurement.date >= one_year_ago.strftime('%Y-%m-%d'))
        .all()
    )

    # Convert query results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

# Stations Route
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    # Query all station data
    results = session.query(Station.station).all()

    # Convert list of tuples into a normal list
    stations_list = [station[0] for station in results]
    return jsonify(stations_list)

# TOBS Route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return temperature observations (TOBS) for the previous year for the most active station."""
    # Find the most active station
    most_active_station = (
        session.query(Measurement.station, func.count(Measurement.station))
        .group_by(Measurement.station)
        .order_by(func.count(Measurement.station).desc())
        .first()[0]
    )

    # Find the most recent date and calculate one year back
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = pd.to_datetime(most_recent_date) - pd.DateOffset(years=1)

    # Query temperature observations for the most active station
    results = (
        session.query(Measurement.date, Measurement.tobs)
        .filter(Measurement.station == most_active_station)
        .filter(Measurement.date >= one_year_ago.strftime('%Y-%m-%d'))
        .all()
    )

    # Convert query results to a list of temperature observations
    tobs_list = [{"date": date, "tobs": tobs} for date, tobs in results]
    return jsonify(tobs_list)

# Start and Start-End Routes
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start, end=None):
    """Return TMIN, TAVG, TMAX for a specified date range."""
    # Query for the min, avg, and max temperatures
    if end:
        results = (
            session.query(
                func.min(Measurement.tobs),
                func.avg(Measurement.tobs),
                func.max(Measurement.tobs)
            )
            .filter(Measurement.date >= start)
            .filter(Measurement.date <= end)
            .all()
        )
    else:
        results = (
            session.query(
                func.min(Measurement.tobs),
                func.avg(Measurement.tobs),
                func.max(Measurement.tobs)
            )
            .filter(Measurement.date >= start)
            .all()
        )

    # Convert query results to a dictionary
    stats_data = {
        "Start Date": start,
        "End Date": end if end else "Latest Available",
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2],
    }
    return jsonify(stats_data)
# Main behavior to run the app
if __name__ == "__main__":
    app.run(debug=True)