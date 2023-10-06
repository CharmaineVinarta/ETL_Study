# Exercise

- **1. Do a word count on a file with the following content.:**
  ```bash
  Italy Venice
  Italy Pizza
  Pizza Pasta Gelato
  ```
- **2. How to get started:**
- Delete the data.txt file and output folder
  ```bash
  rm data.txt
  ```
  ```bash
  rm -rf output
  ```

- **3. How to create a file to wordcount:**
  ```bash
  bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.3.jar wordcount data.txt output
  ```
