import myerror

def oopsTest():
	try:
		oops()
	except myerror.MyError as e:
		print(e)
	except IndexError:
		print("hi")
	finally:
		pass

def oops():
	raise myerror.MyError("Hi")


oopsTest()

