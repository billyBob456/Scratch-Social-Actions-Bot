
from scratchclient import ScratchSession as s
from flask import Flask, render_template

app = Flask(__name__)

scratch = s('viewbot4repl2', 'securePassword1') #please don't hack. this is for everyone.

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/<action>/<id>')
def love_fave_view(action, id):
	if action.lower() == "love":
		try:
			project = scratch.get_project(id)
			project.love()
			return 'Loved by viewbot4repl!</p>'
		except:
			return 'Oops! An error occurred!</p>'
	elif action.lower() == "favourite":
		try:
			project = scratch.get_project(id)
			project.favorite()
			return 'Favourited by viewbot4repl!</p>'
		except:
			return 'Oops! An error occurred!</p>'
	elif action.lower() == "view":
		try:
			project = scratch.get_project(id)
			project.view()
			return 'Viewed! It might take a minute to show on Scratch. Once it\'s showed, you can reload to add another view!</p>'
		except:
			return 'Oops! An error occurred!</p>'
	elif action.lower() == "follow":
		try:
			user = scratch.get_user(id)
			user.follow()
			return 'Followed by viewbot4repl!</p>'
		except:
			return 'Oops! An error occurred!</p>'

app.run(debug=False, host='0.0.0.0', port=8080)
