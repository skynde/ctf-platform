# CTF-Platform
I created this project as a study.

This project uses [DashGum](http://blacktie.co/2014/07/dashgum-free-dashboard/).
Thanks to Carlos.

## Usage 
1. Build a container
```docker-compose up```
Please wait until you see
```
db_1   | LOG:  database system is ready to accept connections
db_1   | LOG:  autovacuum launcher started
```

1. Migrate
Entering the container
```
docker exec -it ctfplatform_web_1 /bin/bash
```
and migrate.
```
./manage.py makemigrations
./manage.py migrate
```

1. Create SuperUser
```
./manage.py createsuperuser
```

1. Run test server
```
./manage.py runserver 0.0.0.0:8000
```
If you want to use this server to listen from Internet, 
prepare some web servers like nginx.

1. Access admin site
   - http://localhost:8000
1. Create Affiliates
1. Create Problems
1. Add users with the command below
```./manage.py addUsers userList.csv problemList.csv```


