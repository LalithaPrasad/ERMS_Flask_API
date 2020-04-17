This app is same in functionality as 'ERMS_Flask_Web', but implements it in api
mode using Flask framework. It uses token based authentication. To use it you 
need a HTTP client like 'postman' or 'httpie'. You can also access the api 
with a javascript frontend.

To initialise the database run the following commands:

    flask db init
    flask db migrate
    flask db upgrade

After that, run the app with:

    flask run

To access the api with say 'httpie' the commands will look like this:

    http <http verb> <machine address>:5000/<api> <data>

Here are the commands to access the api from the localhost:

    http post http://localhost:5000/create_admin username=<username> password=<password>

    http get http://localhost:5000/get_token username=<username> password=<password>

    http post http://localhost:5000/add_employee token:<token> name=<name>
                                                    age=<age> ed=<education> role=<role>

    http get http://localhost:5000/display_employees token:<token>

    http post http://localhost:5000/modify_employee token:<token> id=<id of
                                                employee> ed=<ed> or role=<role> or both

    http delete http://localhost:5000/delete_employee token:<token> id=<id of employee>

I have also implemented this app using 'flask-restful' and 'falcon', but I am
not posting them here, because their implementation is quite straightforward.
