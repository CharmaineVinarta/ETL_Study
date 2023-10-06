- Create documents in MongoDB with the insert method
- Read documents by listing them, counting them and matching them to a query
- Update and delete documents in MongoDB based on specific criteria

# Exercise 1 Getting the environment ready
### Getting the environment ready
- Start the mongodb server.
  start_mongo
### Connect to the mongodb server.
- Connect to the mongodb server.
  #mongo -u root -p NTc0My1yc2FubmFy --authenticationDatabase admin local
## Connect to the mongodb server.
- Select the training database.
  use training
### Create a collection named languages.
- db.createCollection("languages")

# Exercise 2 Insert Documents

### Let us insert five documents into the collection languages
- db.languages.insert({"name":"java","type":"object oriented"})
- db.languages.insert({"name":"python","type":"general purpose"})
- db.languages.insert({"name":"scala","type":"functional"})
- db.languages.insert({"name":"c","type":"procedural"})
- db.languages.insert({"name":"c++","type":"object oriented"})

# Exercise 3 - Read documents
### Find the count of documents.
- db.languages.count()
Copied!
### List the first document in the collection.
- db.languages.findOne()
### List all documents in the collection.
- db.languages.find()
### List first 3 documents in the collection.
= db.languages.find().limit(3)
### Query for “python” language.
- db.languages.find({"name":"python"})
### Query for “object oriented” languages.
- db.languages.find({"type":"object oriented"})

## List only specific fields, Using a projection document you can specify what fields we wish to see or skip in the output.
### This command lists all the documents with only name field in the output.
- db.languages.find({},{"name":1})

### This command lists all the documents without the name field in the output.
- db.languages.find({},{"name":0})

### This command lists all the “object oriented” languages with only “name” field in the output.
- db.languages.find({"type":"object oriented"},{"name":1})

# Exercise 4 - Update documents
### The ‘updateMany’ command is used to update documents in a mongodb collection, and it has the following generic syntax.
db.collection.updateMany({what documents to find},{$set:{what fields to set}})

### Here we are adding a field description with value programming language to all the documents.
- db.languages.updateMany({},{$set:{"description":"programming language"}})

### Set the creater for python language.
- db.languages.updateMany({"name":"python"},{$set:{"creator":"Guido van Rossum"}})

### Set a field named compiled with a value true for all the object oriented languages.
- db.languages.updateMany({"type":"object oriented"},{$set:{"compiled":true}})

# Exercise 5 - Delete documents
### Delete the scala language document.
- db.languages.remove({"name":"scala"})

### Delete the object oriented languages.
- db.languages.remove({"type":"object oriented"})

### Delete all the documents in a collection.
- db.languages.remove({})


