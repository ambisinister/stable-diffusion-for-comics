# Stable Diffusion - Image Generation for Artists

This project aims to implement the "stable diffusion" algorithm for image generation in order to assist artists in iterating upon concepts more quickly.

This project was built leveraging the Huggingface Diffusers library, which provides a flexible and easy-to-use implementation of the stable diffusion algorithm. This allowed us to quickly and efficiently implement the algorithm, and focus on developing features and improvements specifically tailored to the needs of artists.

This readme was partially generated using [chatGPT](chat.openai.com/chat). You have no excuse to provide code without documentation! The future is now.

## Requirements
In order to run this project, you will need:

Python 3.6 or later
TensorFlow 2.0 or later
NumPy
Installation
To install the project, clone this repository and install the required packages:

```
$ git clone https://github.com/USERNAME/stable-diffusion.git
$ cd stable-diffusion
$ pip install -r requirements.txt
```

## Usage
To use the stable diffusion algorithm, simply run the following command:

```
$ python stable_diffusion.py --input_image path/to/input_image.png --output_image path/to/output_image.png
```

This will generate a new image based on the input image using the stable diffusion algorithm, and save it to the specified output path.

## Docker Usage
This project includes a Dockerfile which can be used to build a Docker image containing all of the required dependencies. To build the Docker image, run the following command from the root of the project directory:

```
$ docker build -t stable-diffusion .
```

This will create a Docker image with the tag "stable-diffusion". You can then run the image as a container with the following command:

```
$ docker run -it --rm stable-diffusion
```

This will start a new container based on the "stable-diffusion" image, and run the stable_diffusion.py script inside of it. You can pass any command line arguments to the script by appending them to the docker run command. For example, to run the algorithm on a specific input image and save the output to a specific path, you can use the following command:

```
$ docker run -it --rm stable-diffusion python stable_diffusion.py --input_image path/to/input_image.png --output_image path/to/output_image.png
```

Note that the input_image and output_image paths should be specified with respect to the root of the project directory inside of the container.

If you would like to access files on your host system from inside of the container, you can mount a volume using the -v flag. For example, to mount the current working directory on your host system to the /app directory inside of the container, you can use the following command:

```
$ docker run -it --rm -v "$(pwd)":/app stable-diffusion
```

This will allow you to access files in the current working directory on your host system from the /app directory inside of the container. You can then specify file paths with respect to this directory when running the stable_diffusion.py script.

## Contribution
If you would like to contribute to this project, please fork this repository and make any desired changes. Then, submit a pull request for review.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
