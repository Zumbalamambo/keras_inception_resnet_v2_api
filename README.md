# keras_inception_resnet_v2_api

[![Docker Automated build](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg)](https://hub.docker.com/r/charlesgreen/keras_inception_resnet_v2_api/) [![Updates](https://pyup.io/repos/github/charlesgreen/keras_inception_resnet_v2_api/shield.svg)](https://pyup.io/repos/github/charlesgreen/keras_inception_resnet_v2_api/) [![Python 3](https://pyup.io/repos/github/charlesgreen/keras_inception_resnet_v2_api/python-3-shield.svg)](https://pyup.io/repos/github/charlesgreen/keras_inception_resnet_v2_api/) [![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/charlesgreen/keras_inception_resnet_v2_api/blob/master/LICENSE) [![Read the Docs](https://img.shields.io/readthedocs/pip.svg)](http://charlesgreentensorflow.readthedocs.io/en/latest/) [![Travis branch](https://img.shields.io/travis/rust-lang/rust/master.svg)](https://travis-ci.org/charlesgreen/keras_inception_resnet_v2_api)

# WIP - ACTIVE DEVELOPMENT - DO NOT USE!!!

Implement an image classification web api using keras_inception_resnet_v2 model and keras-rest-server.

This repository is based on the [ansrivas/Keras-rest-server](https://github.com/ansrivas/keras-rest-server) for loading and serving keras models as an API using flask.


## Getting started:
---
1. Install Anaconda:
```
https://docs.continuum.io/anaconda/install
```

2. Clone this repository
```
git clone https://github.com/charlesgreen/keras_inception_resnet_v2_api.git
cd keras_inception_resnet_v2_api
```

3. Create a new python 3.x environment and activate it:
```
conda create --name keras-server -y python=3
source activate keras_inception_resnet_v2_api
```

4. Install all the dependencies:
```
conda env update -n keras_inception_resnet_v2_api  --file requirements.txt
```

5. To remove the environment run:
```
conda remove -n keras_inception_resnet_v2_api --all -y
```

### Usage
------------------

### Run to generate pickle files:
```
python createpickles.py
```

### Run the server (defaults to http://localhost:7171)
```
python server.py
```

### Send a post request to this server to test your model
```
python client.py
```
