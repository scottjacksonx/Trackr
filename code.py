import web
import sqlite3

urls = (
	'/', 'home',
	'/like', 'like'
)

DEBUG = False
web.config.debug = True

templatePath = "/srv/www/trackr.scottjackson.org/templates/"
if DEBUG:
	templatePath = "templates/"

render = web.template.render(templatePath)

app = web.application(urls, globals())

class like:
	def GET(self):
		if web.cookies().get("userid") == None:
			web.debug("need to set User ID")
			addNewUser()
		return render.form()
		
	def POST(self):
		
		userID = web.cookies().get("userid")
		
		input = web.input()
		url = input.url
		reason = input.reason
		
		if reason == "other":
			reason = input.otherReason
		
		addLike(userID, url, reason)
		
		return render.done()
		
class home:
	def GET(self):
		return render.home()

def addNewUser():
	# Add the user to the user database
	dbPath = "/srv/www/trackr.scottjackson.org/db/users.db"
	if DEBUG:
		dbPath = "/Users/scottjacksonx/Documents/dev/git/trackr/db/users.db"
	
	userID = 0
	conn = sqlite3.connect(dbPath)
	c = conn.cursor()
	c.execute("select MAX(id) from users")
	for row in c:
		userID = int(row[0])
		userID += 1
		web.debug("userID = " + str(userID))
		thirtyOneDays = 2678400
		web.setcookie("userid", userID, thirtyOneDays)
	c.execute("insert into users values(?)", (userID,))
	conn.commit()
	c.close()
	
	# Add a new table in the likes database for the user's likes
	dbPath = "/srv/www/trackr.scottjackson.org/db/likes.db"
	if DEBUG:
		dbPath = "/Users/scottjacksonx/Documents/dev/git/trackr/db/likes.db"
	conn = sqlite3.connect(dbPath)
	c = conn.cursor()
	values = (userID,)
	c.execute("create table ? (id INTEGER PRIMARY KEY)", values)
	conn.commit()
	c.close()
	
	
def addLike(userID, link, reason):
	dbPath = "/srv/www/trackr.scottjackson.org/db/likes.db"
	if DEBUG:
		dbPath = "/Users/scottjacksonx/Documents/dev/git/trackr/db/likes.db"
	
	conn = sqlite3.connect(dbPath)
	c = conn.cursor()
	values = (userID, link, reason)
	c.execute("insert into ? values(NULL, ?, ?)", values)
	conn.commit()
	c.close()

if __name__ == "__main__":
	app.run()
	
app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()