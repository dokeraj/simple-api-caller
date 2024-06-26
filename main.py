import os
import sys

import requests

import configInit

API_TIMEOUT = int(os.environ.get('API_TIMEOUT', 3))


def runRequests(config):
    for req in config:
        try:
            response = requests.request(
                url=req.url,
                method=req.http_method,
                headers=req.converted_headers,
                json=req.payload
                , timeout=(3, API_TIMEOUT))

            if 200 <= response.status_code <= 299:
                print(f"Successfully called: ${response.json()}")
            else:
                print(f"API call failed with status code {response.status_code} and error: ${response.json()}")

            sys.exit()

        except requests.exceptions.Timeout:
            strErr = f"ERROR: Timeout has occurred after {API_TIMEOUT} seconds, while making request: {req.url}! Exiting app!"
            print(strErr)
            sys.exit()
        except Exception as e:
            strErr = f"ERROR: {str(e)} has occurred while calling the API: ${req.url}! Exiting app!"
            print(strErr)
            sys.exit()


def main():
    print("STARTING SCRIPT!")

    config = configInit.initConfig()
    runRequests(config)


main()
