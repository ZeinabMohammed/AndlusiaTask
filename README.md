# AndlusiaTask


Company API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
### Download this app to your local machine
```
git clone https://github.com/zeinabmohammed/AndlusiaTask.git
```
### Prerequisites

you need to install apps in requirements.txt file ,open terminal and move to project directory then type:

```
pip install requirements
```

### usage

after installing requirements on terminal or cmd

```
cd companysystem
```


then
```
python manage.py runserver
```
After running local server
Go to Browser 

## Versions usage
```
http://127.0.0.1:8000/v0/ (First version of API)
http://127.0.0.1:8000/v1/ (seconed version of API)
```

## Description
This is simple API for company has several departments each department have one manager with multiple employees ,
This api has 2 versions each version lists all departments with its managers and employees,
In datastructuring used hirarical structure means department is ForeignKey for managers then every manager is ForeignKey for its employees,
that helped me in seriaizing and use nested relationship in serializers structure,
-endpoints in V0 used viewsets for departments and managers then generics for profiles
-endpoints in V1 used APIVIew.
then structuring urls patterns and testing with postman




## License

This project is freelicensed 

## Acknowledgments

* This is simple API which could be imporoved with more features


