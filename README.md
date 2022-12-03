Penless

< br/>

A Content managment system for the telecom world to ditch the use of pens for paperwork...


< br/>
```bash

*** All templates are under www and then stored in there own seperate folders


Code base structure

< PROJECT ROOT >
  |
  |-- core/                               # Implements app logic and serve the static assets                          
  |     |-- settings.py                    
  |     |-- wsgi.py                       
  |     |-- urls.py                        # Define URLs served by all apps
  |   |-- www/
  |     |-- templates/                    # Templates 
  |       |-- www/                      
            |--index.html 
  |     |-- admin.py
  |     |-- apps.py
  |     |-- models.py
  |     |-- views.py 
  |-- requirements.txt                    
  |-- runtime.txt                          # Django version
  |-- manage.py                            # Start the app - Django default start script
|
|-- ************************************************************************
```
