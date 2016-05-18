# isy-dashboard
This Python application runs a Flask web server and provides a RESTful service to control ISY-managed light switches.

# Dependencies
isy-dashboard depends on the following packages:
* flask
* requests

Each of these packages is accessible in the pip package manager. For help on installation, please see the authors' instructions for [flask](http://flask.pocoo.org/docs/0.10/installation/) and [requests](http://docs.python-requests.org/en/master/user/install/#install).

# Initial Configuration

Configuring isy-dashboard is a four step process:

1. Define your environment
2. Configure definitions.py
3. Update isy-dashboard.py
4. Configure your html files

## 1. Define your environment

isy-dashboard uses the term 'group' to combine switches on a single page in the dashboard. As of this version, groups may not be nested, but that is coming in the future.

**Come up with a list of groups you want have in your dashboard.**

* In my home deployment, I define my groups as floors of my house as seen in this screenshot.

![Root Webpage](http://i.imgur.com/tNdclnI.png "Root Webpage")

## 2. Configure definitions.py

The definitions.py file is essentially your settings file, but it is written in python for quick, easy importing into the isy-dashboard application. If you are not comfortable writing Python code, do not worry. All you have to do is follow formatting instructions closely and you will be fine.

1. Completely ignore the first section of code - the one that starts with "class Switch:" - you do not need to touch that and, if you do, you will likely break the application. :) It does have to be at the top or I would bury it at the bottom so you aren't tempted to touch it.
2. Define all of your switches using the instructions below and the screenshot reference.
  1. Enter a python name for the switch to be used later in definitions.py
  2. Enter the name to be used by .html files
  3. Enter the address of the switch from ISY - remember to exclude leading 0s
  4. If the switch has a slave, repeat these instructions as in the "livingroom" example below
  5. Though not pictured here, you may nest as many slaves as you would like.
![Switch Object](http://i.imgur.com/D4wHJwo.png "Switch Object Reference")

3. In the line that starts with "ISYADDRESS", change "10.0.0.1" to the IP address of your ISY and do not change any other text in that line
4. In the line that starts with "ISYADMIN", update the quoted word to your admin username. Remember to leave the single quotes around it!
5. In the line that starts with "ISYPASSWORD', update the quoted word to your admin password. Remember to leave the single quotes around it!
6. Define each group you decided on earlier using the following format:
   * Enter an ALL_CAPS name without spaces (use an underscore _ if you want a space)
   * Enter each switch's python name (defined in step 2 above) separated by a comma with brackets [ ] surrounding the whole group

![Group Definitions](http://i.imgur.com/ZynItzc.png "Group Definition Reference")

## 3. Update isy-dashboard.py
This part is quick - you don't need to touch much here. This is the actual web server that will be running and displaying the isy-dashboard.

1. Do a search for the text "UPDATE ME" or scroll to the very bottom of the file
  1. Directly beneath the line "UPDATE ME", these instructions are included
2. For each group you defined in Step 2 above, you will have a line that begins with either "if" or "elif"
  1. The first group will always start with "if"
  2. Any other groups will start with "elif"
3. Enter a short, lower case name without spaces for your group between the single quotes
  1. This will be used in your .html templates to view each group
4. Enter the ALL_CAPS name from the definitions.py file for the associated group
5. If you have more than two groups, copy the two lines starting with "elif group" and insert them above the line starting with "else". 
  1. You should always include the "else" line
![isy-dashboard Update](http://i.imgur.com/7fRDA6x.png "isy-dashboard.py Update")

## 4. Update your .html files
I will add these instructions as soon as possible. I hope nobody actually sees this message and I'm able to finish before anyone needs them.
