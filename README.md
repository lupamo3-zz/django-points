# django-points
Django Coordinates // Distance between coordinates

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
-->





<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Django Co-ordinates API</h3>
</p>



<!-- ABOUT THE PROJECT -->
## About The Project

An application that should have an API endpoint that accepts a string of comma separated
points for example “(2,3), (1,1), (5, 4), ...” and calculates the closest points. It then stores them
in a table with the following details:
* The string of points submitted
* The result of the computation: the closest points pair



Here are some of the features:
* Input Points and create closest two coordinates



### Built With

* [Django](https://www.django-rest-framework.org/)
* [Python](https://www.python.org/)
* [PostgresQl](https://www.postgresql.org/)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
  ```sh
  
  ```

### Installation

1. Access Github [https://github.com](https://github.com)
2. Clone the repo
   ```sh
   git clone https://github.com/lupamo3/django-points/tree/master
   ```
3. Change directory into the Django points directory :
   ```sh
   cd django-points
   ```
4. Create and activate your virtual environment :

   ```sh
   Virtual venv python=[Python-Version]
   Pip install auto-env
   ```
5. Install Project Requirements
```sh
pip install -r requirements.txt
```
6. Run the application
```sh
python3 manage.py runserver
```

### Test the application on Postman
## Test The API end-points
 - Run [Co-ordinates Endpoints](https://mfs-djangorf.herokuapp.com/) on your postman to test the URLs

or use:

| URL                                 | METHOD                 | MESSAGE                                |
| ------------------------------------|:----------------------:| --------------------------------------:|
|points/                              | POST                   | Input an Array and number of points.   |


---


<!-- USAGE EXAMPLES -->
## Additional Information

- **Feel free to reach me via email and to fork this project**
    - Any feedback would be appreciated.
    - The Pull requests have bit by bit application documentation


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


<!-- CONTACT -->
## Contact

Your Name - [@nlanjichi](https://twitter.com/nlanjichi)

Project Link: [https://github.com/lupamo3/flask-crud/tree/master](https://github.com/lupamo3/django-points/tree/master)


