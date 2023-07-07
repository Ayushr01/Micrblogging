# Micrblogging
A micro blogging api project

Hi please Follow the below steps to setup the django project:
1. clone this repository (advised to do it in a seperate virtual environment)
2. In the main project app run the following command to install all dependencies pip install -r requirements.txt
3. setup a local Postgres database and user grant with all priviledges on that database to the user
   (**assuming** postgres is installed in your local else run **sudo apt install postgresql postgresql-contrib** to istall)
4. once postgres is setup and db and user are created run the following commands in the main project app the following command:
   > **python manage.py migrate**
5. create a super user for you django admin by python manage.py createsuperuser and follow the instructions.

   Now your repository is setup

Use postman to hit apis and check them

Breif Api documentation :
PLease Note that for authentication Tokens are used so please add Authorization token token_id for apis which requres them.
**App -> USER**
1. Registering a user:
  http://127.0.0.1:8000/api/users/ Method name Post -> required username, email and password
2. Login user:
     http://127.0.0.1:8000/api/users/login Method name Post -> required email and password **note you will get token in response use it for authentication.**
3. Get/update users details:
   http://127.0.0.1:8000/api/users/id/  Method Get -> to fetch users data Patch to update users data ( **Note only a user himself can update his data none others**)
4. http://127.0.0.1:8000/api/users/timeline/ Method name Get -> gives all posts details

**App -> POST**
1. creating a post:
  http://127.0.0.1:8000/api/posts/ Method name Post -> body {"created_by":1,"content": "some content"}
2. Get/update posts details:
   http://127.0.0.1:8000/api/posts/id/  Method Get -> to fetch posts data Patch to update users data ( **Note only a user himself can update his posts none others**)


