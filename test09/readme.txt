Flask - Message Flashing

A good GUI based application provides feedback to a user about the interaction. For example, the desktop applications use dialog or message box and JavaScript uses alerts for similar purpose.

Generating such informative messages is easy in Flask web application. Flashing system of Flask framework makes it possible to create a message in one view and render it in a view function called 'next'.

flash(message, category)
- message: the actual message to be flashed
- category: optional. Can be either 'error', 'info', or 'warning'
