E-Commerce Flask Application Documentation
This document explains the purpose and execution of three core tests implemented in the E-Commerce Flask Application, as well as their integration into the Continuous Integration/Continuous Deployment (CI/CD) pipeline.

Test 1: Route Handling Test
Objective:
The purpose of this test is to ensure that the application properly handles invalid HTTP method requests for specific routes. In particular, we want to verify that the server responds with the correct HTTP status code (e.g., 405 for Method Not Allowed) when an unsupported HTTP method is used.

Implementation:
The /products endpoint is designed to accept GET requests.
The test simulates a POST request, which is an invalid method for this endpoint.
The expected outcome is that the server responds with a 405 Method Not Allowed error.
Test 2: MongoDB Connectivity and Read Test
Objective:
This test checks the application’s ability to establish a connection with the MongoDB database and to perform read operations without issues. It uses MongoDB’s ping command to verify the database's connectivity.

Implementation:
The connection to the MongoDB database is established using credentials stored in environment variables.
The admin.command("ping") method is executed to confirm that the database is accessible.
A successful ping response indicates that the connection to the database is working correctly.
Test 3: MongoDB Write Operation Test
Objective:
The goal of this test is to ensure that the application can perform write operations to MongoDB, such as inserting a new document, and that the inserted data is accurately retrieved.

Implementation:
A test document is inserted into the products collection in the MongoDB database.
The test queries the database to confirm the document’s successful insertion.
Assertions are used to verify that the document exists and that the data is correct.
CI/CD Pipeline Integration
Step 1: Install Dependencies
The pipeline is configured to install all necessary dependencies using the following command:
bash
Copy code
pip install -r requirements.txt
Step 2: Set Up Environment Variables
Sensitive environment variables (such as database credentials) should be securely loaded in the pipeline. For GitHub Actions, this is typically done by adding the necessary variables to the GitHub Secrets.
Step 3: Execute Tests
All the implemented tests are run automatically in the CI/CD pipeline during each code push or pull request.
Conclusion
The implemented tests cover three important areas:

Handling of invalid HTTP methods and proper route responses.
Successful connection to the MongoDB database and the ability to read data.
Writing data to MongoDB and verifying that the data is correctly inserted and accessible.
By integrating these tests into the CI/CD pipeline, the application ensures reliability and stability throughout its development and deployment stages.

