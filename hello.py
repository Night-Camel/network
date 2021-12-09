def wsgi_application(environ, start_response):
    start_response("200 OK", [("Content_Type", "text/plain")])
    return ["\r\n".join(environ["QUERY_STRING"].split("&"))]
