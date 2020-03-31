# Distribution_Algorithm 


# Server 
 it is recommended to run the below command first to get all the available updates:
```
apt-get update
```
Since the root user is the most powerful, essentially a root user can do everything on the server, so we may want to limit access to it to improve security.you can create a new user and configure it to "act like" a root user but with certain limitations, and we will log in as this user from then on. It is highly recommended to do so, but if you choose not to follow this practice and simply want to login as the root user anyway, continue the guide otherwise see the CreateUser.md guide.

## Setting up our app folder

First, we create a folder called `fairness-algorithm-rest` for our app. We create this folder using the following command

```
sudo mkdir /var/www/html/fairness-algorithm-rest
```

The folder is owned by the `root` user since we used `sudo` to create it. We need to transfer ownership to our current user:

```
sudo chown <user>:<user> /var/www/html/fairness-algorithm-rest
```

Remember that `user` is the username in our tutorial, make sure you change it to yours accordingly. The same goes for `fairness-algorithm-rest`.

Next, we get our app from `Git`:

```
cd /var/www/html/fairness-algorithm-rest/
git clone https://github.com/DanielAbergel/Distribution-Algorithm.git .
cd /server
```

Note that there's a trailing space and period (` .`) at the end, which tells `Git` the destination is the current folder. If you're not in this folder `/var/www/html/fairness-algorithm-rest/`, remember to switch to it or explicitly specify it in the `Git` command. And for the following commands in this section, we all assume that we are inside the folder `/var/www/html/fairness-algorithm-rest/server` unless specified otherwise.

Then we will install a bunch of tools we need to set up our app:
make sure your pytohn3 -version is python 3.6.9

```
sudo apt-get install python3-pip python3-dev libpq-dev
```

Next, we will install `virtualenv`, which is a python library used to create virtual environment. Since we may want to deploy several services on one server in the future, using virtual environment allows us to create independent environment for each project so that their dependencies won't affect each other. We may install `virtualenv` using the following command:

```
pip3 install virtualenv
```

After it is installed, we can create a `virtualenv`:

```
virtualenv venv --python=python3
```

To activate `virtualenv`:

```
source venv/bin/activate
```

You should see `(venv)` appears at the start of your command line now. We assume that we are in `virtualenv` for all the following commands in this section unless specified otherwise.

Next, use the command below to install the specified dependencies:

```
pip install -r requirements.txt
```

`requirement.txt` is a text file that includes all the dependencies that we created in our `Git` folder.

Note that when installing these requirements, we are inside the virtual environment `venv`, so all the libraries are installed into `venv`, and once we quit `venv`, these libraries won't take effect.

*Hint:* to quit virtual environment, use command:

```
deactivate
```
# uWSGI

In this section, we will be using `uWSGI` to run the app for us, in this way, we can run our app in multiple threads within multiple processes. It also allow us to log more easily. More details on `uWSGI` can be found [here](https://uwsgi-docs.readthedocs.io/en/latest/).

First, we define a `uWSGI` service in the system by:

```
sudo vi /etc/systemd/system/uwsgi_fairness_algorithm_rest.service
```

And the content we are going to input is shown below:

```
[Unit]
Description=uWSGI fairness algorithm

[Service]
ExecStart=/var/www/html/fairness-algorithm-rest/server/venv/bin/uwsgi --master --emperor /var/www/html/fairness-algorithm-rest/server/uwsgi.ini --die-on-term --uid fairness-server --gid fairness-algorithm --logto /var/www/html/fairness-algorithm-rest/server/log/emperor.log
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

We will explain the basic idea of these configs. Each pair of square brackets `[]` defines a `section` which can contain some properties.

The `Unit` section simply provides some basic description and can be helpful when looking at the logs.


If we want to add multiple environment variables, we just need to add multiple lines of the `Environment` entry following the syntax:

```
Environment=key=value
Environment=key=value
Environment=key=value
...
```

The `ExecStart` property informs `uWSGI` on how to run our app as well as log it.

At last, the `WantedBy` property in `Install` section allows the service to run as soon as the server boots up.

*Hint:* after editing the above file, press `ESC` to quit insert mode and use `:wq` to write and quit.

## Configuring uWSGI

Our next step is to configure `uWSGI` to run our app. To do so, we need to create a file named `uwsgi.ini` with the following content: **(already in the project under /server folder)**

```
[uwsgi]
base = /var/www/html/fairness-algorithm-rest/server
app = app
module = %(app)

home = %(base)/venv
pythonpath = %(base)

socket = %(base)/socket.sock

chmod-socket = 777

processes = 8

threads = 8

harakiri = 15

callable = app

logto = /var/www/html/fairness-algorithm-rest/server/log/%n.log
```

Note that you should change the `base` folder accordingly in your own app. For the second entry, `app` is referred to the `app.py` , which serves as the entry point of our app, so you may need to change it accordingly in your own project as well. We defined the `socket.sock` file here which will be required by the `nginx` later. The socket file will serve as the connection point between `nginx` and our `uWSGI` service.

We asked for 8 processes with 8 threads each for no particular reason, you may adjust them according to your server capacity and data volume. The `harakiri` is a Japanese word for suicide, so in here it means for how long (in seconds) will the `emperor` kill the thread if it has failed. This is also an advantage we have with `uWSGI`, it allows our service to be resilient to minor failures. And it also specifies the log location.

And at last, after saving the above file, we use the command below to run the `uWSGI` service we defined earlier:

```
sudo systemctl start uwsgi_fairness_algorithm_rest
```

And we should be able to check the `uWSGI` logs immediately to make sure it's running by using the command:

```
vi /var/www/html/fairness-algorthm-rest/server/log/uwsgi.log
```
# Nginx

`Nginx` (engine x) is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server. In this tutorial, we use `nginx` to direct traffic to our application. `Nginx` can be really helpful in scenarios like running our app on multiple threads, and it performs very well so we don't need to worry about it slowing down our app. More details about `nginx` can be found [here](https://nginx.org/en/).

## Installing nginx

```
sudo apt-get install nginx
```

## Configure firewall to grant access to nginx

First, check if the firewall is active:

```
sudo ufw status
```

If not, we will enable it later. Before that, let's add some new rules:

```
sudo ufw allow 'Nginx HTTP'
sudo ufw allow ssh
```

**Important:** the second line, adding SSH rules, is not related to `nginx` configuration, but since we're activating the firewall, we don't want to get blocked out of the server!

If the UFW (Ubuntu Firewall) is inactive, use the command below to activate it:

```
sudo ufw enable
```

To check if `nginx` is running, use the command:

```
systemctl status nginx
```

Some other helpful command options for system controller are:

```
systemctl start <service_name>
systemctl restart <service_name>
systemctl reload <service_name>
systemctl stop <service_name>
```

## Configure nginx for our app

Before deploying our app onto the server, we need to configure `nginx` for our app. Use the below command to create a config file for our app:

```
sudo vi /etc/nginx/sites-available/fairness-algorithm-rest.conf
```

Note that `fairness-algorithm-rest` is what we named our service, you may change it accordingly, but remember to remain consistent throughout the configurations.

Next, we input the below text into `fairness-algorithm-rest.conf` file. **Remember to change your service name accordingly in this file as well**.

```nginx
server {
  listen 80;
  real_ip_header X-Forwarded-For;
  set_real_ip_from 127.0.0.1;
  server_name localhost;

  location / {
    include uwsgi_params;
    uwsgi_pass unix:/var/www/html/fairness-algorithm-rest/server/socket.sock;
    uwsgi_modifier1 30;
  }

  error_page 404 /404.html;
  location = /404.html {
    root /usr/share/nginx/html;
  }

  error_page 500 502 503 504 /50x.html;
  location = /50x.html {
    root /usr/share/nginx/html;
  }
}
```

The above config allows `nginx` to send the request coming from our user's browser to our app. It also sets up some error pages for our service using `nginx` predefined pages.

And at last, in order to enable our configuration, we need to do something like this:

```
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/fairness-algorithm-rest.conf /etc/nginx/sites-enabled/
```

We need to remove the default file since `nginx` will look at this file by default. We want `nginx` to look at our config file instead, thus we added a soft link between our config file and the `site-enabled` folder.

## Running our app

Finally, we can launch our app! We can do so by starting the `nginx` and `uWSGI` services we defined (we already started the `uWSGI` service in the previous section).

```
sudo systemctl start nginx
```

If any of these services is already running, you may use the below commands (taking `nginx` for example) to reload and restart it so that it has the latest changes:

```
sudo systemctl reload nginx
sudo systemctl restart nginx
```
.
