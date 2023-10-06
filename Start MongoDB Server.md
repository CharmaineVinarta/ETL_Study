# Practice

- **Start Mongo**
  ```bash
  start_mongo
  ```
- **After recieving a command similar to the one given below, copy paste to Connect to mongodb server**
  ```bash
  mongo -u root -p NTc0My1yc2FubmFy --authenticationDatabase admin local
  ```
- **Find the version of the server**
  ```bash
  db.version()
  ```
-This will show the version of the mongodb server.
- **Lists database**
  ```bash
  show dbs
  ```
- This will print a list of the databases present on the server.
- **Create database**
  ```bash
  use training
  ```
- This will create a new database named training. If a database named training already exists, it will start using it.
- **Create collection**
  ```bash
  db.createCollection("mycollection")
  ```
- This will create a collection name mycollection inside the training database.
- **Lists collections**
  ```bash
  show collections
  ```
- This will print the list of collections in your current database.

- **Insert documents into a collection**
  ```bash
  db.mycollection.insert({"color":"white","example":"milk"})
  ```
  ```bash
  db.mycollection.insert({"color":"blue","example":"sky"})
  ```
  ```bash
  b.mycollection.insert({"color":"green","example":"grass"})
  ```
  ```bash
  db.mycollection.insert({"color":"pink","example":"barbie"})
  ```
  ```bash
  db.mycollection.insert({"color":"yellow","example":"biscuit"})
  ```
- **Count the number of documents in a collection**
  ```bash
  db.mycollection.count()
  ```
  -This command gives you the number of documents in the collection.
- **List all documents in a collection**
  ```bash
  db.mycollection.find()
  ```
- This command lists all the documents in the collection mycollection
- Notice that mongodb automatically adds an ‘_id’ field to every document in order to uniquely identify the document.
- **Disconnect from mongodb server**
  ```bash
  exit
  ```

# Exercise
### Connect to mongodb server.
- mongo -u root -p NTc0My1yc2FubmFy --authenticationDatabase admin local

### List databases.
- show dbs

### Create a database named mydatabase.
- use mydatabase 

### Create a collection named landmarks in the database mydatabase.
- db.createcollection("landmarks")

### Lists collections
- show collections

### Insert details of five landmarks including name, city, and country. Example: Eiffel Tower, Paris, France.
- db.landmarks.insert({"name":"Tokyo Tower","city":"Tokyo","country":"Japan"})

### Count the number of documents you have inserted.
- db.landmarks.count()

### List the documents
- db.landmarks.find()

### Disconnect from the server.
- exit



