# Creating another user

Since the `root` user is the most powerful, essentially a root user can do everything on the server, so we may want to limit access to it to improve security. So in this section, we will create a new user and configure it to "act like" a `root` user but with certain limitations, and we will login as this user from then on. It is highly recommended to do so, but if you choose not to follow this practice and simply want to login as the `root` user anyway, you can skip this section

## Hello fairness-algorithm

In this section, we will create a user named `fairness-algorithm`. You may choose any name you want, just remember to swap `fairness-algorithm` with your username for each command and configuration. We can create a new user `fairness-algorithm` with the following command:

```
adduser fairness-algorithm
```

You will be asked to enter and confirm the password for this user, and then provide some info about this user. Notice that you can leave the info sections blank if you want to. And if you entered unmatching passwords, just complete the info section and we can change the password later by using the command:

```
passwd fairness-algorithm
```

## Providing user with additional privilege

Since we will be logging in as `fairness-algorithm` for most of the time in the future, we will want it to have some "extra power", that is, temporarily acting as a super user. To do this, we need to run the command:

```
visudo
```

first, and we will see a text file popping up. Then we navigate to the lines containing:

```
# User privilege specification
root ALL=(ALL:ALL) ALL
```

You can do this with the arrow keys. We need to add a new line for our user in this section:

```
# User privilege specification
root ALL=(ALL:ALL) ALL
fairness-algorithm ALL=(ALL:ALL) ALL
```

Remember that the `ALL` has to be **all uppercase**, otherwise it will raise syntax error.

After adding this line, use `ctrl + o` to save and press `ENTER` to overwrite, then press `ctrl + x` to quit.

## Enable SSH for our new user

Next, we want to allow us to login as `fairness-algorithm` using SSH, and we may also want to disable login as `root` from SSH to make our server more secure. To do this, use the command:

```
vi /etc/ssh/sshd_config
```

And we will be prompted with another text file. Navigate to the section which contains:

```
# Authentication
PermitRootLogin yes
```

Press `i` on your keyboard to enter insert mode and change the `yes` to `no` to disallow login as root.

Next, look for a configuration called `PasswordAuthentication`:

```
# Change to no to disable tunnelled clear text passwords
PasswordAuthentication yes
```

 **Important:** make sure to set it as `yes` so that you can use your password to login in the future. It should be set to `yes` already, however, there are some platforms that enforces SSH key authentication and set it to `no` instead.

Then go to the bottom of the file and add the following lines:

```
AllowUsers fairness-algorithm
```


Next, press `Esc` to quit insert mode, press `:` (colon) to enable the command function and enter `wq` to write and quit (after hitting `ENTER` to confirm).

Some other useful vi commands are: `:q` to quit without modification and `:q!` to force quit and discard changes.

Finally, we use the command:

```
service sshd reload
```

to enable our modifications.

Now we've created a new user `fairness-algorithm` and enabled both its super user privilege and SSH access. 
