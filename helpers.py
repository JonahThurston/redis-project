# import the necessary packages
import numpy as np
import base64
import sys
import os
from datetime import datetime

def base64_encode_image(a):
	# base64 encode the input NumPy array
	return base64.b64encode(a).decode("utf-8")

def base64_decode_image(a, dtype, shape):
	# if this is Python 3, we need the extra step of encoding the
	# serialized NumPy string as a byte object
	if sys.version_info.major == 3:
		a = bytes(a, encoding="utf-8")

	# convert the string to a NumPy array using the supplied data
	# type and target shape
	a = np.frombuffer(base64.b64decode(a), dtype=dtype)
	a = a.reshape(shape)

	# return the decoded image
	return a

def log_action(server_name, action):
	# central logging to keep all entries uniform
	script_name = os.path.basename(sys.argv[0]) or "<unknown>"
	timestamp = datetime.utcnow().isoformat() + "Z"
	message = f"[{timestamp}] server={server_name} script={script_name} action={action}"
	print(message)
	return message
