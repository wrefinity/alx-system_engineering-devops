# 0x14-mysql


## Resourses
 ** Install MYSQL 5.7.x **
- [Install MYSQL 5.7.x](https://www.vultr.com/docs/how-to-install-mysql-5-7-on-ubuntu-20-04/)
- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
```
# syntax: CREATE USER 'username'@'host' IDENTIFIED BY 'password';
CREATE USER 'holberton_user '@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
# grant replication priviledege holberton user 
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
```

## GRANTING PERMISSION 
```
GRANT SELECT ON tyrell_corp.nexus6 TO  'holberton_user'@'localhost';
```

## CREATING A REPLICA USER
```
# creating a replica user
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'replica_user'@'%';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
```
