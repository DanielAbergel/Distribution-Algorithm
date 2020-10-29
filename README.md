<p align="center">
  <img src="https://user-images.githubusercontent.com/44754325/78273213-36a98b80-7517-11ea-8f8e-fb9b8e569988.png">
</p>

# Distribution Algorithm

A web application for fairly dividing goods among people with different valuations.

The [front-end](demoWeb/) allows each person to specify how much he/she values each of the goods.
The data is then sent to the [server](server/).
It runs an [algorithm](server/algorithm) that computes an allocation of the goods among the people.
The algorithm guarantees the following properties:

1. **Fairness**: each agent receives goods with a value of at least 1/n of his/her valuation of all goods.

2. **Pareto Efficiency**: there is no other allocation that is at least as good for all agents and better for at least one agent.

3. **Minimal sharing**: subject to fairness and efficiency, the allocation minimizes the number of sharings of goods between two or more people.
I.e., if there is a fair and efficient allocation with no sharing at all - it will be returned.
Otherwise, if there is a fair and efficient allocation with only one sharing (one good is shared between two people) - it will be returned. And so on.


# Server Installation

**NOTE: in our development process we are using python 3.6.9**

Since the root user is the most powerful, essentially a root user can do everything on the server, so we may want to limit access to it to improve security.You can create a new user and configure it to "act like" a root user but with certain limitations, and we will log in as this user from then on. It is highly recommended to do so, but if you choose not to follow this practice and simply want to login as the root user, continue the guide, otherwise see the CreateUser.md guide.


## Debug Server  

First, we need to set a virtual environment and install the server dependencies.                            
Go into **server/** folder.
Run the following command and replace the parameter `` <password> ``  with your user password.

```
./app.sh build <password>
```

Go into **server/** folder 
and run the following command.

```
./app.sh
```
Now that the server deployed using Flask and Flask-RESTful, access the default Server landing page to confirm that the software is running properly through this URL:

```
  http://127.0.0.1:5000
```
## Production Server 

Creating a Heroku account

First thing we need to do is to sign up for a Heroku account. If you haven't done so, here is the [link](https://signup.heroku.com).

The page will also ask for your primary programming language, choose python (not necessary).

After creating and logging into your account, you will be ask to select a Dyno , which is essential a server in Heroku . Other platforms will have different names for their servers. Remember to select the free tier Dyno unless you choose to pay.

The free tier Dyno is powerful enough to our website (there is also the unix Deployment via master branch , for more information please see master branch README.md), and the limitation is that it will go to sleep if no requests come in 30 minutes. 
It will wake up in a few seconds after receiving a request when it's sleeping. The performance of free Dyno is also limited. Still, it's a good way for our project.

After selecting the Dyno , you will be navigated to the Dashboard, where you can create a new app. Click the New button on the upper-right of your Dashboard, and select create new app from the dropdown menu.
Then enter the app name and select a region for your app. Selecting a region which is closest to your users can make your service much faster.

After creating a new app, you will be navigated to the app page.
Select the ```Settings``` tab and go to the ```buildpack``` option. Use the ```Add buildpack``` button and add the following lines , ```by that order``` :

```https://github.com/timanovsky/subdir-heroku-buildpack.git```

```heroku/python```

Then add the Following key-value to the ```Config Vars``` :
```buildoutcfg

 KEY              VALUE
 EMAIL          : <Email>
 EMAIL_PASSWORD : <Email password>
 PROJECT_PATH   : server
```
```PROJECT_PATH``` is mandatory parameter!

```EMAIL``` + ```EMAIL_PASSWORD``` used for sending emails with the algorithm results.

Next, select the Deploy tab in the app page.

Then click the GitHub option in Deployment method section and enter your credentials to connect Heroku with your GitHub. Next, select the repository and branch where your project is ```Distribution-Algorithm``` and branch is ```heroku-depoloyment```. Once it is done, you can directly deploy your app from GitHub onto Heroku by clicking the button Deploy Branch . Heroku will take care of the rest for you from now on. After a few seconds, Heroku will finish deploying for you.

by Clicking on ```View``` you can go to your website URL , have fun . 

It is highly recommended to choose ```Enable Automatic Deploys``` for the ```heroku-deployment``` branch , this will automatic build the website on each commit on the branch.

NOTE : Most of the documentation is taken from another repository

Our server is a generic production server that can be used by many algorithms. 
The server usage is simple, to deliver any content to the clients, place the content as described here:
* HTML content - web/```<any HTML format>```.
* CSS content - web/css/```<any CSS format>```.
* DOM content (JavaScript files) - web/DOM/```<any DOM format>```. 
    
# Server data format
our server recives the Algorithm input via ``<server URL>/calculator`` URL. (need to send a POST request with JSON as described here)
```json
    "num_of_agents" : 4,
    "num_of_items" : 4 ,
    "problem" : "Proportional",
    "agents" : ["Netanel", "Daniel", "Holo","Matanel"],
    "items" : ["Miami Beach House", "Old Piano", "AirPods Pro"],
    "values" : [[12,63,25], [49,13,38], [39,15,47],[44,9,47]],
    "email" : "fairnessalgorithm.io@gmail.com"
```
### Explanation
  * num_of_agents - participants  number.
  * num_of_items - the items that that will be divided.
  * problem - the algorithm [Proportional\EnvyFree] .
  * agents - participants  names.
  * items - items names
  * values - return value / input values.
  * email : a valid email that the server will send the result to 
# For developers

The algorithm can be run without the server, e.g. for experiments.
To do this, download the repository, and 
add the [Distribution-Algorithm/server/](Distribution-Algorithm/server/) path to your Python include path.
An example of a Python code for running the algorithm can be found 
[here](server/algorithm/Version3/Example.py).

# Algorithm Run Times.

this table represents the Algorithm times for each case Agents/Items please note that on 4 Agents the time may be a long time.
in our client-side (website) on in each 4 Agent case, an email will be sent with the Algorithm results.

## Proprotional
![Screen Shot 2020-10-02 at 10 20 40](https://user-images.githubusercontent.com/44754325/94897836-1bedaa80-0499-11eb-89f5-f0d8fb571966.png)

## Envy-Free
![Screen Shot 2020-10-02 at 10 21 01](https://user-images.githubusercontent.com/44754325/94897909-40498700-0499-11eb-819b-5effe4985b2b.png)

# Contributors

* [Algorithm Programming](server/algorithm/): Eliyahu Satat and Nachshon Satat.
* [Server Programming](server/): Daniel Abergel and Elyashiv Deri.
* [Front-End Programming](demoWeb/): Netanel Ben Issahar.
