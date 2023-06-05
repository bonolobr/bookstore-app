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
  - Once the book has been entered successfully, a message will notify you of that along with the display of the updated database that includes the new book added.
  
  <img width="1010" alt="Screenshot 2023-06-02 at 20 31 39" src="https://github.com/bonolobr/bookstore-app/assets/127111801/3c2323cf-ad32-43b9-ac53-ec4c0de3ad99">

 3. To update a book in the database, enter "2" in the menu.
  
  - This will display the books in the database that can be updated.
  
  <img width="1010" alt="Screenshot 2023-06-02 at 20 48 45" src="https://github.com/bonolobr/bookstore-app/assets/127111801/f42d4042-f810-4b79-8b6a-bbf87cc46162">

  - Enter the id of the book you would like to update. After you do so, the selected book will display on the screen to confirm the selection.
  
  <img width="1010" alt="Screenshot 2023-06-05 at 11 33 33" src="https://github.com/bonolobr/bookstore-app/assets/127111801/9f2dc313-7e17-4d67-814e-9097283bd439">

  - Select whether you would like to update the book title.
  - Select whether you would like to update the author.
  - Select whether you would like to update the quantity of books.
  - Once the relevant details selected have been updated, the final updated details of the book will display on the screen.
  
<img width="1010" alt="Screenshot 2023-06-05 at 11 41 18" src="https://github.com/bonolobr/bookstore-app/assets/127111801/e7913f0e-3dc5-4e82-a143-f4b41bfc977d">

  4. To delete a book from the database, enter "3" in the menu.
  
  - This will display the books in the database from which you can select to delete.
  
<img width="1010" alt="Screenshot 2023-06-05 at 11 49 33" src="https://github.com/bonolobr/bookstore-app/assets/127111801/26ff3d4c-ee0f-4950-82c5-7d8396a063e7">
  
  - Enter the id of the book you would like to delete. After you do so, the selected book will display on the screen to confirm the selection.
  
<img width="1010" alt="Screenshot 2023-06-05 at 11 51 30" src="https://github.com/bonolobr/bookstore-app/assets/127111801/843365bb-af72-4beb-a431-582828e146e3">

  -  When requested to confirm deletion, if you enter a value that is not "yes", a message will notify you that the deletion has not been confirmed.
  
<img width="1010" alt="Screenshot 2023-06-05 at 11 55 06" src="https://github.com/bonolobr/bookstore-app/assets/127111801/89395023-1ec8-44a4-8fb3-3ca117e4d44d">
  
<img width="1010" alt="Screenshot 2023-06-05 at 11 54 50" src="https://github.com/bonolobr/bookstore-app/assets/127111801/99e9a95c-8281-409d-9027-37294f6634bf">

  - If you enter "yes" to confirm deletion, a message confirming deletion will display along with the final updated database.
  
  <img width="1010" alt="Screenshot 2023-06-05 at 11 57 14" src="https://github.com/bonolobr/bookstore-app/assets/127111801/49f166e2-1504-43a9-9dc2-6e708e936f41">

  5. To search for a book, enter the "4" in the menu.
  
  - Select whether you would like to search for a book based on the id, title or author.
  - Depending on which selection you've made, the book for which you have searched will display on the screen.
  
  <img width="1010" alt="Screenshot 2023-06-05 at 12 18 57" src="https://github.com/bonolobr/bookstore-app/assets/127111801/2eddcc01-9c1b-4449-b155-e16387af28ff">

  <img width="1010" alt="Screenshot 2023-06-05 at 12 19 09" src="https://github.com/bonolobr/bookstore-app/assets/127111801/6cff8650-651c-4578-b9d8-b5388a49a48d">
  
  <img width="1010" alt="Screenshot 2023-06-05 at 12 19 22" src="https://github.com/bonolobr/bookstore-app/assets/127111801/9cb7c9cc-399c-4be5-a237-f9d007ebc377">
  
  6. To exit the program, enter "0" in the menu.
  
  <img width="1010" alt="Screenshot 2023-06-05 at 12 29 36" src="https://github.com/bonolobr/bookstore-app/assets/127111801/dccaf240-db95-4cd1-826f-d0f5d7e128ae">
  
 ### Error Handling for Bookstore App
  
The program will notify if there are errors with the inputs entered that make the inputs invalid. In these instances, follow the prompts provided and try again to re-enter valid inputs.
  
 The following is the list of invalid input situations with the associated images of the prompts that you will see: 
  
 1. If you enter any value that is not one of the menu option numbers available.
  
  <img width="1010" alt="Screenshot 2023-06-02 at 20 39 37" src="https://github.com/bonolobr/bookstore-app/assets/127111801/8f4d03e0-e3e3-49fd-bbf3-b0d92d86c9d5">

 2. If you enter an negative number or a value that is not a number when adding a new book and entering the quantity you would like to add.
  
  <img width="1010" alt="Screenshot 2023-06-02 at 20 40 58" src="https://github.com/bonolobr/bookstore-app/assets/127111801/2fdeed9c-8427-4820-bc69-113482ee9625">
  
  3. After selecting to update a book from the menu, if you enter a book id that is not in the system.
  
<img width="1010" alt="Screenshot 2023-06-05 at 11 44 24" src="https://github.com/bonolobr/bookstore-app/assets/127111801/92a3f237-5a1f-4874-913d-9504e6150368">

  4. After selecting to update the quantity of books, if you enter a value that is not an number or is a negative value for the quantity.
  
  <img width="1010" alt="Screenshot 2023-06-05 at 11 46 29" src="https://github.com/bonolobr/bookstore-app/assets/127111801/c2714af5-f70e-4f7f-9b0e-17e760319796">
  
  5.  After you select to search for a book, if you enter a value that is not one of the options provided for the method of searching for a book (i.e. by id, title or author).
  
  <img width="1010" alt="Screenshot 2023-06-05 at 12 05 46" src="https://github.com/bonolobr/bookstore-app/assets/127111801/3bcebd5a-b7ac-4e55-84f0-f418c74a2b12">

  6. When you've selected to search for a book based on the id, if you enter a value that is not a number, an error message will appear. If you enter an id number that is not in the database, a message will display to notify you of that.
  
  <img width="1010" alt="Screenshot 2023-06-05 at 12 22 13" src="https://github.com/bonolobr/bookstore-app/assets/127111801/861cae35-603c-4504-94c5-91fe19137073">

  7. When you've selected to search for a book based on the title, if you enter a title that is not in the database.
  
  <img width="1010" alt="Screenshot 2023-06-05 at 12 23 47" src="https://github.com/bonolobr/bookstore-app/assets/127111801/47aec482-2d25-402f-9ec1-a9984ee390ae">

  8. When you've selected to search for a book based on the author, if you enter an author that is not in the bookstore database.
  
  <img width="1010" alt="Screenshot 2023-06-05 at 12 26 16" src="https://github.com/bonolobr/bookstore-app/assets/127111801/00f20e48-165b-4f80-99b9-437405a9c1e2">
  
## Credit and Contribution <a name="credit_and_contribution"><a> 

This program has been developed by Bonolo Ramasedi.

## License <a name="license"><a> 
  
This project is not licensed and is intended for display purposes only. All rights reserved. No usage, distribution, or modification rights are granted.

  
