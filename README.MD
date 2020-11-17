# Vessel Registry

## Technologies

- Flask v1.1.1
- Python v3.7.3
- unittest

## API Usage
- **Vessel Registry**
    - (GET) /vessel - it should return all vessels code or []
    - (GET) /vessel/:vessel_code: - it should return the vessel information or a "not found" message

    - (POST) /vessel - it should register the vessel code sent by body request in JSON format
        Exemple:
        ```
            {"code":"AB127"}
        ```
    - (DELETE) /vessel/:vessel_code: - it should delete the vessel of db or a "not found" message

- **Vessel Item Registry**
    - (GET) /vessel/:code:/items - it should return all items of the specified vessel
    - (GET) /vessel/:code:/items/:code_item: - it should return the item with the specified code item and the specified vessel
    - (POST) /vessel/:code:/items - it should create a new item in the specified vessel
        Exemple:
        ```
            [
                {"code":"1234B1C8","location":"Brasil", "name": "Motor"},
                {"code":"1234B1C7","location":"Brasil", "name": "Motor"}
            ]
        ```
    - (POST) /vessel/:code:/items/deactivate - it should deactivate in the specified vessel the items set on the body
        Exemple:
        ```
            [
                {
                    "code":"1234B1C8"
                },
                {
                    "code":"1234B1C7"
                }
            ]
        ```


## Installation

1. Modules Installation
    - You must to run the `pip3 install` to install all dependencies.

## Available Scripts

In the project directory, you can run:

### `python3 app.py`

Runs the app in the development mode.\
Use [http://localhost:5000](http://localhost:5000) to use the APIs

### `python3 -m unittest`

It runs the unittest module using the scripts at tests directory
