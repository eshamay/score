def application(environ, start_fn):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return ["<h1 style='color:green'>Bello There!</h1>"]
