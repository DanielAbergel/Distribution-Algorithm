

# Server 

**Very Important: in our development process we using python 3.6.9**

Since the root user is the most powerful, essentially a root user can do everything on the server, so we may want to limit access to it to improve security.you can create a new user and configure it to "act like" a root user but with certain limitations, and we will log in as this user from then on. It is highly recommended to do so, but if you choose not to follow this practice and simply want to login as the root user anyway, continue the guide otherwise see the CreateUser.md guide.


## Debug Server  

First, we need to set a virtual environment and install the server dependencies                            
go into **server/** folder in our project.  
Run the following command and replace the parameter `` <password> ``  with your user password.

```
./app.sh build <password>
```

go into **server/** folder 
and run the following command

```
./app.sh
```
Now the server deployed using Flask and Flask-RESTful, Access the default Server landing page to confirm that the software is running properly through this URL:

```
  http://127.0.0.1:5000
```
## Production Server 

It is highly recommended to run the Debug server, and check whether everything works before installing the Production Server . 

go into the **server/** folder.                                             
Run the following command and replace the `` <password> `` parameter with your user password and the  ``` <user> ```  parameter with your ubuntu username .  
(TIP: to find your ubuntu user name run the command  ``whoami``  )

```
./deployServer <password> <user>
```
Now the server deployed using Nginx and uWSGI  , 
Access the default Server landing page to confirm that the software is running properly through your IP address:

```
  http://your_ip
```
.
