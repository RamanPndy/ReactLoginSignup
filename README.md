# ReactLoginSignup
Login And SignUp CRUD operations using React and Bottle

Back-end: Python 2.7, Bottle Framework <br />
Front-end: React, Material-UI <br />
DB: PostgreSql<br />

<b>DB Setup:</b>
<ol>
<li>Install and configure PostgreSQL with DB Name react User postgres and password <password you like></li>
<li>inside public schema execute migration <b>users.sql.</b> </li>
<li>This will create users table in DB with columns username, email and password.</li>
</ol>

For custom DB credentials such as dbname, username, password, you need to update the same in <b>config.py</b> file.

<b>Backend Setup:</b>
<ol>
<li>clone the repo</li>
<li>navigate to <b>requirements.txt</b> folder in command line and execute </li>
<code>pip install -r requirements.txt</code><br />
<li>navigate to <b>main_app.py</b> and execute </li>
<code>python main_app.py</code><br />
</ol>

This will start the backend server.

Note: Any third party library that needs to be added should be added in <b>requirements.txt</b> file and any new SQL migration file that needs to be added should be added in <b>migrations</b> directory.
