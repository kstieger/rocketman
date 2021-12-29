#!/usr/bin/env python3

import requests

REST_API_BASE_URL = "https://api.spacexdata.com/v4"


def all_launches():
    """
    Get all launches and print a list of the names
    """
    
    response = requests.request(
        method="GET",
        url=f"{REST_API_BASE_URL}/launches"
    )
    
    launches = []
    if response.ok:
        launches = response.json()
    print(f"{'-' * 20}0. all launches{'-' * 20}")
    for launch in launches:
        print(f" * {launch['name']}")
    print(f"{'-' * 60}\n")
        
def all_successful_launches():
    """
    Challenge 1:
    Create (and print) a list of all successful launches
    """

    print(f"{'-' * 20}1. all successful launches{'-' * 20}")
    print("*** TODO: successful launches")
    print(f"{'-' * 60}\n")

def all_failed_launches():
    """
    Challenge 1:
    Create (and print) a list of all failed launches
    """
    
    print(f"{'-' * 20}2. all failed launches{'-' * 20}")
    print("*** TODO: failed launches")
    print(f"{'-' * 60}\n")

def main():
    all_launches()
    all_successful_launches()
    all_failed_launches()
    

if __name__ == "__main__":
    main()