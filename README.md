# StopOver

## Team members

**Project Leader:** Ana Teo  
**Team Leader:** Jono Sun  
**Business Analyst:** Jeffrey Tan  
**Scrum Master:** Nicky Le  

## GitHub URL

**https://github.com/Envying/StopOver**

## Heroku Application

**https://stopover-rmit.herokuapp.com/**

## Release Versions

| Release Version | type | Features |
| --------------- | -------- | ------- |
| v1.0 | new feature | The first version of the car share scheme app, Stopover. This is developed within the scope of the group's capstone project course at RMIT University under the supervision of Mr. Homy Ashrafzadeh. This version includes the following features: Map, Current location of user, Current location of cars available , Booking function |
| v2.0 | new feature | The second version of Stopover now includes a payment function, which allows the users to pay for their chosen vehicle through Paypal. This version also includes the following features: Full screen homepage map, Retractable list of available vehicles in the homepage, List of available vehicles is sorted by distance from the user's current location, Payment, summary and confirmation page, Payment page redirects to Paypal's payment system, Payment session timer |
| v2.1 | bug fixes | Version 2.1 of Stopover now contains updated static files. |
| v2.12 | bug fixes | Another fix to Stopover's static files that improves the app's performance after deployment. |
| v2.13 | bug fixes | This version contains a quick hotfix for the static files. |
| v3.0 | new features | Stopover v3.0 now lets its users see how to navigate to their car during their booking confirmation! This makes it easier for the users to gauge how far the car is from their current location and how exactly to get there. The admin side of the web app lets the administrators track down the company's cars through a simulation created using the MapBox API. The new version of Stopover introduces a fresh look that favours user-friendliness through a clean and organised interface. Users can now log-in and access their dashboard, which allows them to update their account details, to view current booking and to read through their booking history. The current booking tab of the dashboard includes a "Return Car" button that notifies the system when the car has been returned. This version also includes an updated payment method, so that users can enter their credit card details and confirm their booking securely through Stripe. Users are charged for their use of the service without the hassle of repeatedly entering their details. |
| v4.0 Beta | new features | **Select and book a car on-the-go.** StopOver's latest version features a mobile-friendly web application which makes it easier for the users to view and utilise the interface on their phones or tablets. A few tweaks were also done to the UI for a more straightforward application use. |
| v4.1 | bug fixes | Version 4.1 contains a fix for the images that were previously not showing in version 4.0. |

## Installation

### Install Python:
The project is done in Python 3.7, so it is recommended to install Python 3.7.X.

#### Linux:
- Open up the Terminal and type the following command:
```
$ sudo apt-get update && sudo apt-get -y upgrade
```
```
$ sudo apt install python python-dev python3.7 python3-dev
```
- To verify the success installation of Python 3.7, run the following command:
```
$ python3 -V
```
You should see an output like this:
```
python 3.7.X
```

#### Windows:
- Download the python 3 installer at https://www.python.org/downloads/release/python-373/. Scroll down to the bottom and select either Windows x86-64 executable installer for 64-bits or Windows x86 executable installer for 32-bits.
- Run the installer.
- Make sure to tick “Add Python 3.7 to PATH”. Continue to by clicking “Install Now” or customize your installation by clicking “Customize Installation”
- Open up the Command Prompt and run the following command:
```
pip3 --version
```
-The output should look like this:
```
C:\users\[USERNAME]\appdata\local\programs\python\python36-32\lib\site-packages (Python 3.6).
```

#### MacOS:
- To install Python, we need to use homebrew. Open up the Terminal and type the following command:
```
brew install python3
```
- To verify the installation of python 3.7, run the following code:
```
$ python3 --version
```

### Installing Pip
We require pip to install the virtual environment and modules that are needed to run the project.
#### Linux:
- Open up the Terminal and type the following command:
```
$ sudo apt-get install -y python3-pip
```
- To verify the installation of pip3, run the following command:
```
$ pip3 -V
```

#### Windows:
- Pip should have been installed with installing Python, to verify the installation, run the following command:
```
pip --version
```

#### MacOS:
- Pip should have been installed with Python, to verify the installation, run the following command:
```
pip3 --version
```

### Installing Virtual Environment
We will be installing Django in a virtual environment that will we setup in this instruction. We want to isolate one project’s dependencies from dependencies of other projects. So that is why we are installing a virtual environment.
#### Linux:
- Open up the Terminal and type the following command:
```
$ pip3 install virtualenv
```
- Once it is installed, to verify the installation, run the following command:
```
$ virtualenv --version
```
- You should see an output similar to the following:
```
16.4.3
```

#### Windows:
- Open up the Command Prompt to enter into the PowerShell and run the following command in the stopover directory:
```
virtualenv --python "c:\python36\python.exe" env
```

#### MacOS:
- Open up the Terminal and type the following command:
```
pip3 install --upgrade virtualenv
```

### Download Stopover

- We are going to create a directory called Stopover, or you can choose a name of your choice.
```
$ mkdir Stopover
```
```
$ cd Stopover
```
- Initialise a git repository with the following command:
```
$ git --init
```
- To download the project, run the following command in the terminal or command prompt:
```
$ git clone https://github.com/Envying/StopOver.git
```

### Installing the requirements
Requirements.txt contains the necessary modules needed to run this project including Django.
#### Linux:
- To run the virtual environment, make sure you are inside the project directory and run the following code:
```
$ . /env/bin/activate
```
- Now once you are in the virtual environment, to install the requirements, run the following code:
```
(env) user: $ pip3 install -r requirements.txt
```
- To verify that you have installed the required modules, run the following command:
```
(env) user: $ pip3 list
```

#### Windows:
- To run the virtual environment, make sure you are inside the project directory and run the following code:
```
.\env\Scripts\activate
```
- Now once you are in the virtual environment, to install the requirements, run the following code:
```
pip install -r requirements.txt
```

#### MacOS:
- To run the virtual environment, make sure you are inside the project directory and run the following code:
```
source env/bin/activate
```
- Now once you are in the virtual environment, to install the requirements, run the following code:
```
pip install -r requirements.txt
```

## Deployment

### Local Deployment
- In command prompt/terminal in your project file, enter your virtual environment (read information above)
- Run the following command for local deployment:
```
python manage.py runserver
```
- To access the website: http://127.0.0.1:8000

### Heroku Deployment
- In requirements.txt add whitenoise module and then run
```
pip install -r requirements.txt
```
- In settings.py file add:
```
whitenoise.middleware.WhiteNoiseMiddleware
```
into middleware and add:
```
whitenoise.runserver_nostatic
```
into installed apps
- Create a collectstatic that collects all the static (CSS, JS, IMGS) to be used in deployment
```
python manage.py collectstatic
```
**More detailed deployment in development guide on how to update your settings.py files**
