
## PDF_ArticleAnlyzer

Articles Anlyzer using Grobid


## Instalation

Follow these steps to get started with the project.

### Create a enviroment
Create a enviroment to run the repository

conda create -n <name_env> python=3.11.5

In case you are in python 3.11.5 you could also use python enviroments

python -m venv <virtual-environment-name>

### Clone the Repository

```bash
git clone --recursive <REPOSITORY_URL>
cd <DIRECTORY_NAME>
git submodule init
git submodule updates
```

### Install Dependencies

```bash
pip install -r requirements.txt
```


### SetUp Packages
 This repository has a setup.py using setuptools

setup install for getting the packages at site-packages
```bash
python setup install
```

Install the required dependencies for the project.



## Configuration

This project uses config files as the form of yaml files.

The main script uses the folders {base_config} and {data_main} for a correct working in case you move the main script bring those folder with it.

If you use this project as a library as the examples look at the examples folders for custom config folders with the config files.

### Configure Grobid Client

At the folder config/api, check the grovid-server-config.yaml for modiying the protocol (http,https), domain(example.com), and port (8070) before starting

### Configure Grobid Funcionalites

At the folder config/api, check the api-base-config.yaml any funcionality has those configs values in common, if you want to create a new config file dont remove those config values, any changes to the base values could end up to unexpected results.


### Configure Grobid Server

This project uses a Grobid Server for working make sure there is a online grobid server, you could use docker to run a local grobid server
 [Link on hot to setup a grobid server](https://grobid.readthedocs.io/en/latest/Grobid-docker/)



## Tutorials

### At folder examples there are some notebooks with a brief demostration of the funcionalities and how to use the class

You can run the funcionalites as a library as shown at the exmples or using the main script


## Features

### 0. Main Executable

While as shown at the examples this proyect can be use a a library also it can be execute as a script with the main.py
its paramerters are  {service} for selecting the funcionality, {--protocol} {http}  {--domain} {example.com}  {--port} {8070}

```bash
python main.py {service} --protocol http --domain example.com --port 8070
```

### 1. Generate Wordclouds from Abstracts

Using the class WordCloud we extract the abstracts of the articles and create a WordCloud png of the text

```bash
python main.py visualize.word_cloud 
```


### 2. Bar Chart with the Number of Figures per Article

Using the class CountAtritubte we can count specific elments of the articles and create bar chars comparing them, at the config folder config/api there is count-config.yaml
where we can set what atributes to find now it is set to finde <figures> elements form the xml

```bash
python main.py visualize.stadistic 
```

### 3. List Article Links

The class SearchLink will find <ref> elements and https links at the articles and list them displaying a table using the rich library

```bash
python main.py visualize.links_search
```


## Docker

In case you need to run this project as a container you will need to use the Dockerfile at the folder docker

##### Docker Server
First you need to have a running server with grobid
```
docker pull grobid/grobid:0.8.0
```
```
docker run --rm --gpus all --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.0
```

##### Grobid Client
```
docker build -t pdf-analyzer docker
```

```
docker run -it pdf-analyzer /bin/bash
```
Now you can use 
python main.py {service} and run the services
## License

This project is under the Apache 2.0 License. Refer to the [LICENSE](LICENSE) file for more details.

## Contact

- Name: Jorge Martin Izquierdo
- Email: jorge.martin.izquierdo@alumnos.upm.es


## Bibliography

As this project uses the grobid cliente api and server as base for working checkout the original author of this two programs
    GROBID (2008-2022) <https://github.com/kermitt2/grobid>
    GROBID (2008-2022) <https://github.com/kermitt2/grobid>_client_python

