project_library
==============================

![image1](https://github.com/hicham123k/project_library/assets/64266152/2a58d0a9-8aaa-49c2-9bdb-6d259f69a298)


![image4](https://github.com/hicham123k/project_library/assets/64266152/cf220b30-3c46-40bc-a52d-cffebd5be84f)

![image6](https://github.com/hicham123k/project_library/assets/64266152/3d2d7742-2838-4358-a21c-6eab4204f1db)
![image7](https://github.com/hicham123k/project_library/assets/64266152/6b8653ff-50ef-43aa-845d-d8b161d48536)
![image9](https://github.com/hicham123k/project_library/assets/64266152/21caa665-45d6-464e-b912-cc96f99618ba)
![image10](https://github.com/hicham123k/project_library/assets/64266152/78c65992-196c-46a1-beb6-06512c3bccc0)
![image12](https://github.com/hicham123k/project_library/assets/64266152/db4a8610-a54f-4d5a-b60e-93b078877527)
![image16](https://github.com/hicham123k/project_library/assets/64266152/cda0ea32-c0ef-468e-a6a1-a1cd76d49b7f)
![image19](https://github.com/hicham123k/project_library/assets/64266152/5fbd46c0-f17a-47b9-8a41-226ed907e541)
![image20](https://github.com/hicham123k/project_library/assets/64266152/13cc99c2-1dc3-4a85-bb52-72652162a4e1)

### Quick setup

> The next steps assume that conda is already installed


1 - <a name="step-1">Create a conda environment:</a>


```bash
conda create python=3.8 -n project_library
```
2 - <a name="step-2">Activate the conda environment</a>

```bash
conda activate project_library
```

3 - <a name="step-3">Install the project basic dependencies and development dependencies</a>

> Make sure you are inside the root project directory before executing the next commands.
>
> The root project directory is the directory that contains the `manage.py` file

On Linux and Mac

```bash
pip install -r requirements/local.txt
```

On Windows

```bash
pip install -r requirements\local.txt
```

4 - <a name="step-4">Configure the database connection string on the .env</a>

On Linux and Mac

```bash
cp env.sample.mac_or_linux .env
```

On Windows

```bash
copy env.sample.windows .env
```

Change the value of the variable `DATABASE_URL` inside the file` .env` with the information of the database we want to connect.

Note: Several project settings have been configured so that they can be easily manipulated using environment variables or a plain text configuration file, such as the `.env` file.
This is done with the help of a library called django-environ. We can see the formats expected by `DATABASE_URL` at https://github.com/jacobian/dj-database-url#url-schema. 

5 - <a name="step-5">Use the django-extension's `sqlcreate` management command to help to create the database</a>

On Linux:

```bash
python manage.py sqlcreate | sudo -u postgres psql -U postgres
```

On Mac:

```bash
python manage.py sqlcreate | psql
```

On Windows:

Since [there is no official support for PostgreSQL 12 on Windows 10](https://www.postgresql.org/download/windows/) (officially PostgreSQL 12 is only supported on Windows Server), we choose to use SQLite3 on Windows

6 - <a name="step-6">Run the `migrations` to finish configuring the database to able to run the project</a>


```bash
python manage.py migrate
```


### <a name="running-tests">Running the tests and coverage test</a>


```bash
coverage run -m pytest
```


## <a name="troubleshooting">Troubleshooting</a>

If for some reason you get an error similar to bellow, is because the DATABASE_URL is configured to `postgres:///project_library` and because of it the generated `DATABASES` settings are configured to connect on PostgreSQL using the socket mode.
In that case, you must create the database manually because the `sqlcreate` is not capable to correctly generate the SQL query in this case.

```sql
ERROR:  syntax error at or near "WITH"
LINE 1: CREATE USER  WITH ENCRYPTED PASSWORD '' CREATEDB;
                     ^
ERROR:  zero-length delimited identifier at or near """"
LINE 1: CREATE DATABASE project_library WITH ENCODING 'UTF-8' OWNER "";
                                                             ^
ERROR:  syntax error at or near ";"
LINE 1: GRANT ALL PRIVILEGES ON DATABASE project_library TO ;
```



```sql
ERROR:  role "myuser" already exists
ERROR:  database "project_library" already exists
GRANT
```

<a name="troubleshooting-delete-database">You can delete the database and the user with the commands below and then [perform step 5 again](#step-5).</a>

> :warning: **Be very careful here!**: The commands below erase data, and should only be executed on your local development machine and **NEVER** on a production server.


On Linux:

```bash
sudo -u postgres dropdb -U postgres --if-exists project_library
sudo -u postgres dropuser -U postgres --if-exists myuser
```

On Mac:

```bash
dropdb --if-exists project_library
dropuser --if-exists myuser
```


