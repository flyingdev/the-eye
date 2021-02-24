<div align="center">
<h1>The Eye</h1>
</div>

<div align="center">
<strong>Assumptions</strong>
<p>
There is Application generating part especially for generating session id. <br />
Also I assume that can get allowed hosts address and set as environment
</p>
</div>

<div align="center">
<strong>Constraints</strong>
</div>

 - Event should be unique for session_id and timestamp
 - Event has index for session_id, category, timestamp for quick search

<div align="center">
<strong>Configure</strong>
</div>

 - Python 3.8
 - Run ``virtualenv venv --python python3``
 - Run ``source venv/bin/activate``
 - Run ``pip install -r requirements.txt``
 - Set environment BROKER_URL (Reference .env.example)
 - Set environment ALLOWED_HOSTS by separating comma (Reference .env.example)

<div align="center">
<strong>Run</strong>
</div>

 - Run ``python manage.py runserver``
 - Run ``celery -A the_eye worker -l INFO``

<div align="center">
<strong>Aggregator Endpoint</strong>
</div>

 - [POST] http://localhost:8000/webhook/event/

   It will only accept POST method


<div align="center">
<strong>TODO</strong>
</div>

 - Error Log
 - Client application
 - Dockerize
