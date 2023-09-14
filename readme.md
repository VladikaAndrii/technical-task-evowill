# Bored API Wrapper
This program uses a Bored API to get random activity with parameters and save it in the database.

## Installation
1. Make sure you have Python 3.10.12 installed on your computer. You can try any another version of Python, but this can cause unexpected errors.

2. Clone this repository to your computer.

3. Open a command prompt and navigate to the directory where the cloned repository is located.


## Usage:

###### The program has two commands: `new` and `list`.

#### The `new` command gets a random activity from the Bored API using the provided filters and saves it in the database. For example:

    python app.py new --type education --participants 1 --price_min 0.1 --price_max 30 --accessibility_min 0.1 --accessibility_max 0.5

This command will run the program and get a new random activity with type education, 1 participant, price 0.1, and accessibility 0.1, then save it in the database.

### But you can also run: 
    python app.py new

This command will run the program and get a new random activity without any parameters.


### The `list` command lists the latest activities saved in the database. For example:

    python app.py list

This command will run the program and list the last 5 activities saved in the database.

#### As additional you can run:
    python app.py --help
This command will show you list with commands and options of program.

    python app.py new --help
This command will show you some description about command, all parameters and allowed data types for parameters.

    python app.py list --help 

This command will show you some description of command list.

# Below you can view original task for this program:

## Technical Challenge for Juniors

For this challenge, you are going to use the API of [bored API](https://www.boredapi.com/). This API gives us a random activity to do every time you call it, for example, if you make the following call:

```
GET https://www.boredapi.com/api/activity
```
You will get a response like this:

```json
{
    "activity": "Learn Express.js",
    "type": "education",
    "participants": 1,
    "price": 0.1,
    "link": "https://expressjs.com/",
    "key": "3943509",
    "accessibility": 0.1
}
```
For more details, check the [documentation](https://www.boredapi.com/documentation).

 We will use this API to create a simple program that will give us a random activity to do.

## Instructions
Clone this repository and create a new one on your own GitHub account. When you are done, please send us the link to your repository.

## Tasks

### API Calls
1. Create an API wrapper for bored API, This wrapper should have a method that returns a random activity, and should accept parameters to filter the activities by type, number of participants, price range, and accessibility range.

### Database
2. Write a class that will save the activities in a database, this class should have a method that will accept the activity as a parameter

3. Add another method that will return the latest activities saved in the database. The database can be any database you want (e.g. SQLite), but it should be a relational database.

### Command line program
3. Create a simple command line program that will use the API wrapper and the database class to get a random activity and save it in the database. The program should accept parameters to filter the activities by type, number of participants, price range, and accessibility range. The command should look like this:
    
    ```bash
    my_program new --type education --participants 1 --price_min 0.1 --price_max 30 --accessibility_min 0.1 --accessibility_max 0.5
    ```
This command should get a random activity with the type education, 1 participant, a price of 0.1, and an accessibility of 0.1 and save it in the database.


4. Add another command to the program that will return the last activities saved in the database. The command should look like this:
    
    ```bash
    my_program list
    ```
This command should return the last 5 activities saved in the database.


## Extra points
 - Make sure that you include a dependencies file (requirements.txt, gemfile, package.json, etc.). But don't include any virtual environment or packages installed in your repository.
 - Add unit tests for your work.

