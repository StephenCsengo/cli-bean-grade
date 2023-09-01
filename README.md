# BeanGrade: A Python CLI App

With specialty coffee subscription services, such as [Trade Coffee](https://www.drinktrade.com/), it can be difficult to keep track of all the different coffees you've tried. BeanGrade is a CLI application that allows multiple users, such as everyone in a household, to keep track of and rate coffees from specialty coffee roasters.

BeanGrade allows you to create users, add coffees, and rate these coffees. Additionally, coffee and ratings can be deleted or updated as needed. The app uses SQLAlchemy to persist changes to a database.

## How to Install

1. Fork and clone this repository
2. Navigate to the local directory with

   `cd cli-bean-grade`

3. Install required libraries from the Pipfile with

   `pipenv install`

4. Enter the virtual environment with

   `pipenv shell`

5. Navigate to the lib folder with

   `cd lib`

6. Optionally, seed the database with test data by running

   `python seed.py`

7. Start the application by running

   `./cli.py`

## Usage

A video walkthrough of using the app can be found below.

<a href="https://www.youtube.com/watch?v=DJPtMv0rqJ4
" target="_blank"><img src="https://img.youtube.com/vi/DJPtMv0rqJ4/0.jpg" 
alt="BeanGrade Walkthrough Video" width="240" height="180" border="10" /></a>

## Schema

<img src="https://i.imgur.com/kl86aeL.png" alt="BeanGrade Schema" width="600">

## Contributions

Contributions are welcome! Please fork the repository and create a new branch for your features or bug fixes. Submit a pull request describing your changes.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Acknowledgments

ASCII mug art courtesy of Elissa Potier at [ASCII Art Archive](https://www.asciiart.eu/food-and-drinks/coffee-and-tea)

ASCII title banner courtesy of [patorjk.com](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
