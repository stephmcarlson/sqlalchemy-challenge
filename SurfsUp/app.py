# Import the dependencies.
from sys import _enablelegacywindowsfsencoding
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# create engine 
# automap base to import

# # app=flask()
# session = sessign _engine 
# session query 

# return jsonify varaible

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement

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
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    results = session.query(measurement.station, measurement.date, measurement.prcp, measurement.tobs).all()
    start_date = session.query(measurement.date).order_by(measurement.date.desc()).first()

    start_object = dt.datetime.strptime(start_date.date, "%Y-%m-%d")
    end_object = start_object - dt.timedelta(days=365)

    final_results = session.query(measurement.station, measurement.date, measurement.prcp, measurement.tobs).\
        filter(measurement.date > end_object)

    session.close()

    all_results = []
    for station, date, prcp in final_results:
        results_dict = {}
        results_dict["station"] = station
        results_dict["date"] = date
        results_dict["prcp"] = prcp
        all_results.append(results_dict)

    return jsonify(all_results)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    station_results = session.query(station.station).all()

    session.close()

    station_list = []
    for station in station_results
        if station not in station_list:
        station_list.append(station)
        
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    results = session.query(measurement.station, measurement.date, measurement.prcp, measurement.tobs).all()
    start_date = session.query(measurement.date).order_by(measurement.date.desc()).first()

    start_object = dt.datetime.strptime(start_date.date, "%Y-%m-%d")
    end_object = start_object - dt.timedelta(days=365)

    final_results = session.query(measurement.station, measurement.date, measurement.prcp, measurement.tobs).\
        filter(measurement.date > end_object)

    session.close()

    tobs_results = []
    for station, date, tobs in final_results:
        results_dict = {}
        results_dict["station"] = station
        results_dict["date"] = date
        results_dict['tobs'] = tobs
        tobs_results.append(results_dict)

    return jsonify(tobs_results)

if __name__ == '__main__':
    app.run(debug=True)
