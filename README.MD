# GeoMe Powered by React

## Technologies

- Flask v1.1.1
- Python v3.7.3
- unittest

## API Usage

    - (GET) /vessel - it should return all vessels code or []
    - (GET) /vessel/<vessel_code> - it should return the vessel code or a "not found" message

    - (POST) /vessel - it should register the vessel code sent by body request in JSON format
    Exemple:
    `
        {"code":"AB127"}
    `

## Installation

1. Modules Installation
    - You must to run the `pip3 install` to install all dependencies.

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.