# React

Create a react component called MessageBox that has an input field
and a button that when the button is clicked,if the input field
is not empty, it creates an HTTP POST request to 
https://admin.remote.besic.org/api/statusmessage
with a JSON body containing the contents of the input in a field
called 'msg'

***Hint**: code will be in `/myapp/src/Components/MessageBox.js`*

# Containerize

***Wait until after you're done with the React part of this task***

Write a Dockerfile that will containerize the React project 
you just modified and run the development server exposing the 
appropriate port

***Hint**: blank Dockerfile is provided in  `/myapp/Dockerfile`*
