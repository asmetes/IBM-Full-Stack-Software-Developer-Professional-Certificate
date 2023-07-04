# coding-project-template

## Objectives
In this assignment you will:

Use the deep_translator python package for the translation.
Create a function that translates English to French.
Create a function that translates French to English.
Run coding standards check against the functions above.
Write unit tests to test the above functions.
Run unit tests and interpret the results.
Package the above functions and tests as a standard python package.



## Task1: Write a function that translates English text to French in translator.py
Open a terminal window by using the menu in the editor: Terminal > New Terminal.


Go to the project home directory.

cd /home/project
Copied!
Run the following command to Git clone the project directory from the clone URL you had copied in the prework lab.

[ ! -d 'xzceb-flask_eng_fr' ] && git clone <paste_your_repo_name>
Copied!
Change to the final_project folder.


cd /home/project/xzceb-flask_eng_fr/final_project
Copied!
Create folder named machinetranslation and change to that directory.


mkdir machinetranslation
cd machinetranslation
Copied!
Run the following command to make sure that python3 is using version 3.8.


sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 10
Copied!
Run the following command to check the python version.

python3 --version


Note: It should be Python 3.8.0.

Install the packages that you will be using in this code, namely deep_translator and Flask.


python3 -m pip install deep_translator
python3 -m pip install Flask
Copied!
In the explorer, go to the machinetranslation directory and create a new file called translator.py. Enter the following line of code.


 from deep_translator import MyMemoryTranslator
Copied!
📷 Take a screenshot of your import statement and save it as a .jpg or .png with the filename import_translator. You will be prompted to upload the screenshot in the Peer Assignement that follows.

Add function englishToFrench which takes in the englishText as a string argument, in translator.py. Use the instance of the MyMemory Translator you imported previously, to translate the text input in English to French and return the French text.


def englishToFrench(englishText):
    #write the code here
    return frenchText
Copied!
📷 Take a screenshot of your functions and save it as a .jpg or .png with the filename e2f_translator_function. You will be prompted to upload the screenshot in the Peer Assignement that follows.

Add function frenchToEnglish which takes in the frenchText as a string argument, in translator.py. Use the instance of the MyMemory Translator you imported previously, to translate the text input in French to English and return the English text.


def frenchToEnglish(frenchText):
    #write the code here
    return englishText
Copied!
📷 Take a screenshot of your functions and save it as a .jpg or .png with the filename f2e_translator_function. You will be prompted to upload the screenshot in the Peer Assignement that follows

## Task 2: Write the unit tests for English to French translator and French to English translator function in tests.py
Create a new file called tests.py in the machinetranslation directory.
Write at least 2 tests in tests.py for each method
Test for the translation of the word ‘Hello’ and ‘Bonjour’.
Test for the translation of the word ‘Bonjour’ and ‘Hello’.
Take a screenshot of your unit tests and save it as a .jpg or .png with the filename translation_unittests.


## Task 3: Check your code against python coding standards
At the terminal run the following command to install pylint.


python3 -m pip install pylint
Copied!
Run pylint translator.py to check the coding standard compliance in your code. Refer to this exercise you did earlier, if needed.

Make sure your rating is at least 7.

📷 Take a screenshot of the output of the pylint analysis report showing your score and save it as a .jpg or .png with the filename pylint_score.

## Task 4: Run tests
At the terminal run the command

1
python3 tests.py
Copied!
📷 Take a screenshot of test results and save it as a .jpg or .png with the filename unit_test_results.


## Task 5: Package the above functions and tests as a standard python package.
Create __init__.py file in the directory machinetranslation.

Create a folder called tests under the newly created folder

Copy the unit tests into the tests folder

📷 Take a screenshot of the folder structure of the package ( From the menu go to View -> Explorer to set the explorer view) and save it as a .jpg or .png with the filename package_folder_structure


## Task 6: Import the package into server.py and create flask end points
Import the package machinetranslation in server.py.

In the server.py, for end-point /, implement a method that renders the index.html.

In the space provided in server.py for end-point /englishToFrench implement a method that uses the appropriate translation function through the package you created in the previous part. The function should take the English text as input through the request parameter and return a string.

In the space provided in server.py for end-point /frenchToEnglish implement a method that uses the appropriate translation function through the package you created in the previous part. The function should take the French text as input through the request parameter and return a string.

Push the code to GitHub.

Change to the project directory


cd /home/projects/xzceb-flask_eng_fr
Copied!
Run these following commands replacing your github username and the email you use for loggin into github as appropriate.

git config --global user.email youremail@domain.com
git config --global user.name your_github_username


git add .

git commit -m"Final changes"
Copied!
Task - Generate Personal Access Token

Verify your email address if it hasn’t been verified on Github.
Copied!

In the upper-right corner of any page, click your profile photo, then click Settings.


In the left sidebar, click Developer settings.



In the left sidebar, click drop-down menu `Personal access tokens`.


Click on `Token (classic)` and then click drop-down menu `Generate new token` and click `Generate new token (classic)`.


Give your token a descriptive name. To give your token an expiration, select the Expiration drop-down menu, then click a default or use the calendar picker. Select the scopes, or permissions, you'd like to grant this token. To use your token to access repositories from the command line, select repo.
Copied!



Click `Generate token` and make a note of it.


Make sure you copy the token and keep it safe. It is not visible to you again.

Treat your tokens like passwords and keep them a secret.

Once you have a token, you can enter the Personal Access Token as password when performing Git operations.

The git push command will enable you to sync all the changes made locally to the GitHub web repository.

Run the following command with your actual HTTPS link:


git push [HTTPS link]
Copied!
You will be prompted by git for your username and password.

Type your GitHub username and for the password, enter the personal access token you generated in the previous task. When you are authenticated, all committed changes are synced with your GitHub repository.

You can now visit the GitHub repository page and check to ensure that the revised and newly added files are in place.




## Task 7: Run the server
Change to the project directory and run the server from your terminal.

cd /home/project/xzceb-flask_eng_fr/final_project && python3 server.py
Copied!
You will see that the server starts up in port 8080.

Click on the Skills Network button on the left, it will open the Skills Network Toolbox. Then click the Other then Launch Application.
From there you should be able to enter the port.


Connect to port 8080and click Launch button.


A new browser window opens up with the index page.
📷 Take a screen shot of the translation from English to French
📷 Take a screen shot of the translation from French to English
Previous


## Task 8: Deploy the application on Code Engine.
Change to the final_project directory.

cd /home/project/xzceb-flask_eng_fr/final_project
Copied!
Note:
Make sure Task 7: Run the servers runs successfully.
In requirements.txt file, delete the package versions and it should look as shown below:

Let’s create a Dockerfile in your project directory. Dockerfile is the blueprint for building a container image for our app.


Create Dockerfile and add the following lines to your file:

FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]
Copied!
On the first line we are importing the Docker image python:alpine3.7 which comes with support for Python 3. This image allows us to create Flask web applications in Python that run in a single container. We are interested in the latest version of this image available, which supports Python 3.

On the next 2 lines, we copy the contents of the final_project directory we just created, into an app directory in the container image. Pretty easy, right!

Finally, we are opening port 8080 to usage in the docker container. This will allow us to access our application later once it’s deployed to the cloud.

You should have a directory structure like this:


On the menu in your lab environment, click Skills network tools; Click Cloud dropdown and choose Code Engine. The code engine set up panel comes up. Click Create Project.


The code engine environment takes a while to prepare. You will see the progress status being indicated in the set up panel.

Once the code engine set up is complete, you can see that it is active. Click on Code Engine CLI to begin the pre-configured CLI in the terminal below.



You will now use the CLI to deploy the application.

Change to the app directory where the Dockerfile was created.


cd /home/project/xzceb-flask_eng_fr/final_project
Copied!
Now run docker build in the app directory and tag the image. Note that in the below command we are naming the app flask-docker-demo-translator.


docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/flask-docker-demo-translator



Now push the image to the namespace so that you can run it.

docker push us.icr.io/${SN_ICR_NAMESPACE}/flask-docker-demo-translator:latest


Deploy the application.

ibmcloud ce application create --name flask-docker-demo-translator --image us.icr.io/${SN_ICR_NAMESPACE}/flask-docker-demo-translator --registry-secret icr-secret



Please note this command will run only in a Code Engine CLI. If you didn’t follow the steps 4 to 7 to start the Code Engine CLI, you may get errors.

Press ctrl(Windows)/cmd(Mac) and the link that is created. Alternatively copy the link and paste it in a browser page and press enter. The flask-docker-demo-translator application page renders as given below.

Congratulations!
You have completed the tasks for this project. In the peer assignement that follows, you will be required to upload the screenshots you saved in this lab.

Authors
Lavanya