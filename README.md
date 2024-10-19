
# Rule Engine with AST

A 3-tier rule engine application designed to determine user eligibility based on attributes such as age, department, income, and spending. The system utilizes an Abstract Syntax Tree (AST) to represent conditional rules, enabling dynamic creation, combination, and modification of rules through a simple UI, API, and backend database.


## Installation

1.Install Python 3.10.0,
Download from link:
https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

2.Install Flask

```bash
pip install Flask==3.0.0
```

3.Install Sqlconnect:

```bash
pip install mysql-connector-python==9.1.0
```
4.Install Xampp:

Link : https://www.apachefriends.org/
    
## Download 

Method 1: Download as zip File

Link:https://github.com/Jaisuntbiji/Rule-Engine-with-AST

Method 2:  Clone the Repository Using Git

1.Open a terminal or command prompt and run the following command:
```bash
git clone https://github.com/Jaisuntbiji/Rule-Engine-with-AST.git
```

2.After the repository is cloned, navigate into the project directory:
```bash
cd Rule-Engine-with-AST
```

## Setup Database

Step 1 : (only Install system does not conation sql)

Install Mysql,Before you can use the MySQL command line, ensure that MySQL Server is installed on your system. 

download Link:https://dev.mysql.com/downloads/mysql/8.0.html

step 2:Open Mysql command line and login to it.

step 3:create a Database and use 

```bash
CREATE DATABASE rule_engine_db;
USE rule_engine_db;
```
step 4 :create Table named rules

```bash
CREATE TABLE rules (
  	id INT AUTO_INCREMENT PRIMARY KEY,
  	rule_string VARCHAR(255) NOT NULL,
  	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

step 5 :Insert Data Into Table 

```bash
INSERT INTO rules (rule_string) VALUES 
('((age > 30 AND department = \'Sales\') OR (age < 25 AND department = \'Marketing\')) AND (salary > 50000 OR experience > 5)'),
('((age > 30 AND department =\'Marketing\')) AND (salary > 20000 OR experience > 5)'),
('(age > 30 AND department = \'Sales\')');
```





## Run Locally

Step 1: navigate into the project directory.
```bash
cd Rule-Engine-with-AST
```

Step 2: Select the interpreter as python 3.10.0(64-bit)in VScode/other Code editor, In Vscode download the python package.

Step 3: Open xampp and start mysql and Apache by clicking the start button. To see the table in the database , click the admin button.

Step 4: Use Run code button Or Open terminal run command:
```bash
Python app.py
```
Step 4: Click on the localhost link and the application will be open.The Application was run on port 3066.



