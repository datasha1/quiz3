import sqlite3
import requests
import json
url = "https://official-joke-api.appspot.com/random_joke"
print(requests.get(url).headers)
number = input('Enter your id number: ')
joke = input("Enter your joke type: ")
informatio = {'id':number,'type':joke,'setup':'setup','punchline':'punchline'}
r= requests.get(url, params=informatio)
print(r.status_code)
res = json.loads(r.text)
conn = sqlite3.connect("jokes.sqllite3")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS artistt(
               id INTEGER,
               type VARCHAR(50),
               setup VARCHAR(50),
               punchline VARCHAR(50))
               ;''')
cursor.execute("INSERT INTO artistt VALUES (?,?,?,?)",(number,joke,res['setup'],res['punchline']));
conn.commit()
conn.close()