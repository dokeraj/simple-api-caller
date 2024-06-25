import requests

import configInit


def runRequests(config):
    for req in config:
        try:
            response = requests.request(
                url=req.url,
                method=req.http_method,
                headers=req.converted_headers,
                json=req.payload
            )

            if 200 <= response.status_code <= 299:
                print(f"Successfully called: ${response.json()}")
            else:
                print(f"API call failed with status code {response.status_code} and error: ${response.json()}")

        except requests.exceptions.Timeout:
            strErr = f"ERROR: Timeout has occurred while calling scanning folder(s)! Please run the scan manually!"
            print(strErr)
            return None
        except Exception as e:
            strErr = f"ERROR: {str(e)} has occurred while calling the API: ${req.url}!"
            print(strErr)
            return None


def main():
    print("STARTING SCRIPT!")

    config = configInit.initConfig()
    runRequests(config)


main()
