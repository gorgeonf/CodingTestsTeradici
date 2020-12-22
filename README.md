## Making the docker image
To make the docker image open a terminal at the root of the directory and run the following command:
`docker build -t <image_name> .`

## Running the application
Once the image is built you can run the application with the following command:
`docker run -it <image_name>`

## Executing the tests
With the image built you can launch the tests with the command:
`docker run -it <image_name> pytest -v` 
