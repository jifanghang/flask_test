Flask - Sessions

Unlike a Cookie, Session data is stored on server. Session is the time interval when a client logs into a server and logs out of it. The data, which is needed to be held across this session, is stored in a temporary directory on the server.

A session with each client is assigned a Session ID. The Session data is stored on top of cookies and the server signs them cryptographically. For this encryption, a Flask application needs a defined SECRET_KEY.

Session object is also a dictionary object containing key-value pairs of session variables and associated values.
