# 0x13-firewall

### Resources
- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_%28computing%29)
- [Configure UFW on ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04)
- [How To Configure Firewall with UFW on Ubuntu 20.04 LTS](https://www.cyberciti.biz/faq/how-to-configure-firewall-with-ufw-on-ubuntu-20-04-lts/)
- [UFW Essentials: Common Firewall Rules and Commands](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)
- [First 5 Commands When I Connect on a Linux Server](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/)


### Warning!
**if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.**

# Files & Description
| File | Description|
|------|------------|
|0-block_all_incoming_traffic_but| Let’s install the ufw firewall and setup a few rules on ``web-01``. Configure ufw so that it blocks all incoming traffic, except the following TCP ports: ``22`` (SSH), ``443`` (HTTPS SSL), and ``80`` (HTTP). Share the ``ufw`` commands that you used in your answer file (0-block_all_incoming_traffic_but).|
|100-port_forwarding | Firewalls can not only filter requests, they can also forward them. Configure ``web-01`` so that its firewall redirects port ``8080/TCP`` to port ``80/TCP``. Your answer file should be a copy of the ``ufw`` configuration file that you modified to make this happen.|

### Task One Procedure (100-port_forwarding):
- **Step 1: Edit the file /etc/ufw/before.rules:**
```
$ sudo vi /etc/ufw/before.rules
```
- **Step 2: Configure ufw to redirect http traffic to another (LAN) IP:port. by appending the below command at the top of the file **
```
$ *nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
```
- **Step 3: Open the file /etc/ufw/sysctl.conf:**
```
$ sudo vi /etc/ufw/sysctl.conf
```
- **Step 4: Edit file (/etc/ufw/sysctl.conf):** <br>
``Find where there is the following comments:``<br>
#Uncomment this to allow this host to route packets between interfaces<br>
#net/ipv4/ip_forward=1<br>
#net/ipv6/conf/default/forwarding=1<br>
#net/ipv6/conf/all/forwarding=1<br>
``Uncomment line 2, 3, 4 as below:``<br>
#Uncomment this to allow this host to route packets between interfaces<br>
net/ipv4/ip_forward=1<br>
net/ipv6/conf/default/forwarding=1<br>
net/ipv6/conf/all/forwarding=1
- **Good luck**
