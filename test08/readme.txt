Flask - Redirect & Errors

Flask class has a redirect() function. When called, it returns a response object and redirects the user to another target location with specified status code.

Usage: Flask.redirect(location, statuscode, response)

- location parameter is the URL where response should be redirected.
- statuscode sent to browser’s header, defaults to 302.
- response parameter is used to instantiate response.

Status codes:
- HTTP_300_MULTIPLE_CHOICES
- HTTP_301_MOVED_PERMANENTLY
- HTTP_302_FOUND
- HTTP_303_SEE_OTHER
- HTTP_304_NOT_MODIFIED
- HTTP_305_USE_PROXY
- HTTP_306_RESERVED
- HTTP_307_TEMPORARY_REDIRECT
The default status code is 302, which is for ‘found’.
