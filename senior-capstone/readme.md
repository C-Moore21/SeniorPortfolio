# Senior Project (project name tbd)

Senior Project for displaying BLM lease data on a readable map with pertinent information

### Prerequisites
Docker

Python 3.6+

AWS Account

Geojson stored in S3 with the following requirements:
    bucket-name: senior-project-geo-json

[Google MAP API key](https://developers.google.com/maps/documentation/javascript/get-api-key)

### Running

NOTE: YOU MUST CONFIGURE ALL AWS SESSIONS TO YOUR ACCOUNT CONFIGURATION FOLLOW THIS DOCUMENTATION FOR MORE INFORMATION:
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html

YOU ALSO MUST ADD YOUR OWN GOOGLE MAPS API KEY IN THE INDEX HTML PAGE OR THE PAGE WILL NOT RENDER

Build the docker image

```
docker build -t name-you-want-here .
```

Run the docker image

```
docker run -d name-you-want-here
```

view website in your browser: http://localhost:5000

## Built With

* Python
* Python-Flask
* Bootstrap
* Google API


## Authors

* **Camden Moore**


## License

This project is licensed under the GNU V.3
