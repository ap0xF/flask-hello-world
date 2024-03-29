This is follow along code from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Background:- I have six months of professional experience in java working at Hamro Patro Inc, and currently I am learning py and flask to get better
opportunities for a stable career as a backend developer. This readme containes some key points which 
helps me understand the flask way and it's internals.

1. Controllers --> view functions <br>
2. flaskInstance = Flask(\_\_main__) -> we need to get an instance of Flask class
3. @flaskInstance.route('\\') -> route is defiend under scaffold.py file
4. we need to create a runner script inside the main scope of flask project and import the 
<br> instnce of Flask into this script.
5. Then we need to set FLASK_APP env to the script created in step 4, better import python-dotenv and define the FLASK_APP env inside .flaskenv file
6. Now we're ready to run our flask app using flask run command.<br>

Note:- detailed explaination is in the comments itself.