
# PDF_ArticleAnlyzer

Articles Anlyzer using Grobid


## Quick Start

Follow these steps to get started with the project.

### Clone the Repository

```bash
git clone --recursive <REPOSITORY_URL>
cd <DIRECTORY_NAME>
git submodule init
git submodule updates
```

This repository uses libraries, so make sure to clone recursively to get all necessary files.

### Install Dependencies

```bash
pip install -r requirements.txt
```


### SetUp Packages
 This repository has a setup.py using setuptools

setup install para intalar el paquete localmente
```bash
python setup install
```

Install the required dependencies for the project.

### Configure Grobid Client

At the folder config/api, check the grovid-server-config.yaml for modiying the protocol (http,https), domain(example.com), and port (8070) before starting


# At folder examples there are some notebooks with a brief demostration of the funcionalities and how to use the class

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

## License

This project is under the Apache 2.0 License. Refer to the [LICENSE](LICENSE) file for more details.

## Contact

- Name: Jorge Martin Izquierdo
- Email: jorge.martin.izquierdo@alumnos.upm.es