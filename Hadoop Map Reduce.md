# Practice

- **1. Download hadoop-3.2.3.tar.gz to your theia environment by running the following command.:**
  ```bash
  curl https://dlcdn.apache.org/hadoop/common/hadoop-3.2.3/hadoop-3.2.3.tar.gz --output hadoop-3.2.3.tar.gz
  ```
- **2. Extract the tar file in the currently directory.:**
  ```bash
  tar -xvf hadoop-3.2.3.tar.gz
  ```
- **3. Extract the tar file in the currently directory.:**
  ```bash
  tar -xvf hadoop-3.2.3.tar.gz
  ```
- **4. Navigate to the hadoop-3.2.3 directory.:**
  ```bash
  cd hadoop-3.2.3
  ```
- **5. Check the hadoop command to see if it is setup. This will display the usage documentation for the hadoop script.:**
  ```bash
  bin/hadoop
  ```
- **6. Run the following command to download data.txt to your current directory.:**
  ```bash
  curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/data.txt --output data.txt
  ```
- **7. Run the Map reduce application for wordcount on data.txt and store the output in /user/root/output.:**
  ```bash
  bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.3.jar wordcount data.txt output
  ```
- **8. Once the word count runs successfully, you can run the following command to see the output file it has generated.:**
  ```bash
  ls output
  ```
- **After completing the practice part-r-00000 with _SUCCESS indicating that the wordcount has been done.:**
 
- **The following command is to see the word count output.:**
  ```bash
  cat  output/part-r-00000
  ```



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
