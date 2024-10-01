# -*- coding: utf-8 -*-
import argparse

from download import fetch_incidents
from extract import extract_incidents
from database import deletedb, createdb, populatedb, status


def main(url):
    # Download data
    fetch_incidents(url)

    # Extract data
    incidents = extract_incidents('resources/incidents.pdf')
    # print(len(incidents))
    # print(incidents)
    
    # delete existing database if any
    deletedb()

    # Create new database
    createdb()
    
    # Insert data
    populatedb(incidents)
    
    #Print incident counts
    status()

    # printAllRecords()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
