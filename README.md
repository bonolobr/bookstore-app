# Bookstore App

## Table of Contents

1. [Project Description](#project_description)
2. [Installation](#installation) 
3. [Usage](#usage)
4. [Credit and Contribution](#credit_and_contribution)
5. [License](#license)

## Project Description <a name="project_description"><a>

  This program is a bookstore application that enables users, particularly bookstore clerks, to search for books in the database and make relevant updates. In particular, users can: add new books to the database, update book information, delete books from the database and search the database to find a specific book.
  
## Installation <a name="installation"><a> 
  
There are two different ways to run the program: using Docker or a virtual environment.

### Docker

You can either use docker on your desktop or by using Docker Playground. Descriptions for using both options are included.

**Run container using Desktop**

1. If you don't already have Docker installed on your desktop, install Docker on your desktop.

2. Once installed, enter the following command in the terminal:

```
docker run -i bonolor/bookstore
```

**Run container using Docker Playground**

1. Go to Docker Playground at the following link and enter "Start": https://labs.play-with-docker.com/.

2. Add a new instance.
  
3. Enter the following command in the terminal:

```
docker run -i bonolor/bookstore
```

### Virtual Environment

1. Download the followiing files in the repository.

2. Create a project folder named "bookstore".
 
3. Move and save the downloaded files to the bookstore folder.
  
4. Open your local Integrated Development Environment (IDE) such as VSCode.
 
5. Add the watch_next folder to your IDE.
 
6. In the same parent directory, create a virtual environment named .venv by entering the following command in the terminal (use relevant python version):
   
  ```
  python3.11 -m venv .venv
  ```
  
7. Activate the virtual environment using the following command (for macOS):
  
  ```
  source .venv/bin/activate
  ```
  
8. Once the virtual environment is created and activated, enter the following command to move into the garden_ai directory (if you are not already in the directory):
  
  ```
  cd bookstore
  ```
 
9. Run the requirements.txt file to install all the relevant packages:
  
  ```
  pip install -r requirements.txt
  ```
  
10. If prompted to upgrade pip, enter:

  ```
  pip install --upgrade pip
  ```
  
11. Select bookstore_task.py and run the program.
  
## Usage <a name="usage"><a>
  
1. When you run the proprgam, the the menu provides various options from which you can select.
  
  <img width="1010" alt="Screenshot 2023-06-02 at 20 18 45" src="https://github.com/bonolobr/bookstore-app/assets/127111801/fa4c25af-5bd3-4306-8763-c6638b9b2d07">

2. Add a new book to the database by entering "1" from the menu options.
  
  - Enter the book title.
  - Enter the name of the author.
  - Enter the quanity of books you would like to add.
  - Once the book has been entered successfully, a message will notify you of that and the updated database, which includes the new book added, will display on the screen.
  
  <img width="1010" alt="Screenshot 2023-06-02 at 20 31 39" src="https://github.com/bonolobr/bookstore-app/assets/127111801/3c2323cf-ad32-43b9-ac53-ec4c0de3ad99">

 3. To update a book in the database, enter "2" in the menu.
  
  - This will display
  
  <img width="1010" alt="Screenshot 2023-06-02 at 20 48 45" src="https://github.com/bonolobr/bookstore-app/assets/127111801/f42d4042-f810-4b79-8b6a-bbf87cc46162">

  
 ### Error Handling for Bookstore App
  
The program will notify if there are errors with the inputs entered that make the inputs invalid. In these instances, follow the prompts provided and try again to re-enter valid inputs.
  
 The following is the list of invalid input situations with the associated images of the prompts that you will see: 
  
 1. If you enter any value that is not one of the menu option numbers available.
  
  <img width="1010" alt="Screenshot 2023-06-02 at 20 39 37" src="https://github.com/bonolobr/bookstore-app/assets/127111801/8f4d03e0-e3e3-49fd-bbf3-b0d92d86c9d5">

 2. If you enter an negative number or a value that is not a number when adding a new book and entering the quantity you would like to add.
  
  <img width="1010" alt="Screenshot 2023-06-02 at 20 40 58" src="https://github.com/bonolobr/bookstore-app/assets/127111801/2fdeed9c-8427-4820-bc69-113482ee9625">

  
  
## Credit and Contribution <a name="credit_and_contribution"><a> 

This program has been developed by Bonolo Ramasedi.

## License <a name="license"><a> 
  
This project is not licensed and is intended for display purposes only. All rights reserved. No usage, distribution, or modification rights are granted.

  
