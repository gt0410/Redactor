# Gowtham Teja Kanneganti

In this project we are trying to redact the sensitive information from the .txt files. Whenever sensitive information is shared with the public, the data must go through a redaction process. That is, all sensitive names, places, and other sensitive information must be hidden. Documents such as police reports, court transcripts, and hospital records all containing sensitive information. Redacting this information is often expensive and time consuming.
## Getting Started

The following instructions will help you to run the project.

### Prerequisites

The project is done in python 3.7.2 version. Any version of python-3 will be sufficient to run the code. Also pip environment should be installed. Pyenv and pipenv can be created by using the folowong code in the project. Also a account in [github](https://github.com/) is necessary.
~~~
pyenv install python 3.7.2
pipenv --3.7.2
~~~

### Installing

After setting up the python environment and pip environment the following packages ehich are used in the code need to be installed.

~~~
pipenv install re
pipnev install numpy
pipenv install nltk
pipenv install commonregex
~~~

The above packages need not be installed in the pip environment you are working but should be available to import. Also, after installing all packages from nltk need to be downloaded. This has to be done in system only once.


## Project Description

### Directory Structure

The structure of the directory of this project is as given below.

cs5293p19-project1/ \
├── COLLABORATORS \
├── LICENSE \
├── Pipfile \
├── Pipfile.lock \
├── README.md \
├── project0 \
│   ├── __init__.py \
│   └── main.py \
├── docs \
├── setup.cfg \
├── setup.py \
└── tests \
    ├── test_names.py \
    └── test_genders.py \
    └── ...

The structure is received initially from the repository created in the git. This repository can be brought into Ubuntu by cloning that repository. This can be done by using the following code

~~~
git clone "git repository link"
~~~

After that the Pipfile and Pipfile.lock will be created when pipenv is created. All other files are created in command line.
If any changes are made in the repository then they need to be pushed into git. The status of the git can be checked using the following code.
~~~
git status
~~~

When the above command is run, it shows all the files that are modified. These files need to be added, commited and then pushed into git. The following code is followed:
~~~
git add file-name
git commit -m "Message to be displayed in git"
git push origin master
~~~
### Functions description

#### redactor.py

The main is written in redacted.py. In this file we save multiple arguments passed from the command line in  to related lists giving conditions. Next we will take each file from the input paths and redact the data from the file. Each function to redact the data is called as per the given flags and concept. The status is printed and the redacted data is written into .redacted file as per given output path.
~~~
pipenv run python redactor.py --input '*.txt' \
                    --input 'otherfiles/*.txt' \
                    --names --dates --addresses --phones \
                    --concept 'kids' \
                    --output 'files/' \
                    --stats stderr
~~~

Using argparse the url given in the command line will be passed to redacted.py. All the functions defined in main.py are imported in redactor.py.

#### Redact names

names() takes the input data from the read file. In this function the list of names of person in the data are saved into a list and redacted with a block. The names is extracted by tagging the words in data and then extracting the words tagged as 'PERSON'.
The data downloaded from the pdf is saved into a temporary file in any directory. This file should be available to read for the next method.

#### Redact dates

dates() function redacts all the dates mentioned in the data. This function is written assuming that common regex function identifies all formats of dates.
~~~
parsed_text = CommonRegex(data)
dates_list = parsed_text.dates
~~~

This function can return a list of dates in the data.

#### Redact addresses

The addresses() function redacts all the addresses in the data. The addresses list consists of 2 things. First one is the list of street addressed obtained by using commonregex. Second one is the list of all Geo- Locations tagged on named entities. In this we can also include to redact the zip codes also. But, this is not done at this point of time.

#### Redact phones

The function phones() takes in the data and makes a listy of all phone numbers in the data. Here, we can identify all the phones list by using commonregex. The function also identifies phone numbers from other countries also.

#### Redact genders

genders() function takes the data and replaces all the words with the names in genders_list with a block. The names considered in the genders_list are given below.

~~~
genders_list=['he','she','him','her','his','hers','male','female','man','woman','men','women']
~~~

#### Redact concept

The concept() function takes the data and concept word as the input. This concept word is given by the user and we need to redact the sentences containing that concept words. The similar words are found using wordnet from nltk. All the words from all synsets are lammetized and saved into list. Then the sentences with these words are redacted.
This flag, which can be repeated one or more times, takes one word or phrase that represents a concept. A concept is either an idea or theme. Any section of the input files that refer to this concept should be redacted. For example, if the given concept word is prison, a sentence (or paragraph) either containing the word or similar concepts, such as jail or incarcerated, that whole sentence should be redacted. 

#### Stats 

Stats takes either the name of a file, or special files (stderr, stdout), and writes a summary of the redaction process. Some statistics to include are the types and counts of redacted terms and the statistics of each redacted file. Be sure to describe the format of your outfile to in your README file. Stats should help you while developing your code.
The stats of all functions for all text files are printed and stderr is given when there are no words redacted in that file for that particular function.

### Running the tests

The test files test the different features of the code. This will allow us to test if the code is working as expected. There are several testing frameworks for python, for this project use the
py.test framework. For questions use the message board and see the pytest
documentation for more examples http://doc.pytest.org/en/latest/assert.html .
This tutorial give the best discussion of how to write tests
https://semaphoreci.com/community/tutorials/testing-python-applications-withpytest.

Install the pytest in your current pipfile. You can install it using the command
pipenv install pytest. To run test, you can use the command pipenv run
python -m pytest. This will run pytest using the installed version of python.
Alternatively, you can use the command pipenv run python setup.py test.

Test cases are written for all the five functions. For the purpose of testing a string is already given and the tests are written based on this string only. The test cases are written for each function.

#### Testing addresses

In this test case we are testing if the function addresses() is taking the data and extracting the addresses from it. After calling the function we are testing whether the number of addresses returned are same as in string or not. Next we also test if exactly the same number of texts are redacted in the string.

#### Testing dates

In this test case we are testing if the function dates() is taking the data and extracting the dates from it. After calling the function we are testing whether the number of dates returned are same as in string or not. Next we also test if exactly the same number of texts are redacted in the string.

#### Testing genders

In this test case we are testing if the function genders() is taking the data and replacing the genders init with block. After calling the function we are testing whether the count of genders returned is same as in string or not.

#### Testing names

In this test case we are testing if the function names() is taking the data and extracting the names from it. After calling the function we are testing whether the number of names returned are same as in string or not. Next we also test if exactly the same number of texts are redacted in the string.

#### Testing phones

In this test case we are testing if the function phones() is taking the data and extracting the phones from it. After calling the function we are testing whether the number of phones returned are same as in string or not. Next we also test if exactly the same number of texts are redacted in the string.


### Inspirations

https://oudalab.github.io/textanalytics/projects/project1
https://www.tutorialspoint.com/python/python_command_line_arguments.html, helped me in understanding passing multiple arguments from command line.

https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/ , These videos helped me in understanding the usage of nltk package.

https://stackoverflow.com/questions/20290870/improving-the-extraction-of-human-names-with-nltk , referred to this for extracting human names.

https://likegeeks.com/nlp-tutorial-using-python-nltk/ , helped in understanding the basic nltk concepts.

https://github.com/madisonmay/CommonRegex , I have used commonregex function after checking the documentation from the above link.

http://www.nltk.org/howto/wordnet.html , Used this to write the concept function.

https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python , helped me in using glob function to take imput files.

### People Contacted

Dr. Christan Grant, cgrant@ou.edu, Professor, Discussed what should be included in the stats function and also about the warning message while running tests.

Chanukya Lakamsani, chanukyalakamsani@ou.edu, Teaching Assistant, Mailed to him and discussed about the stats function.

Sai Teja Kanneganti, kannegantisaiteja@ou.edu, Co- student, Discussed about named entities (watched the same tourtorial), passing multiple arguments from command line. 
