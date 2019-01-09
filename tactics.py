from flask import Flask, render_template, request
import time
import random
import requests
import webbrowser

headers = {"User-Agent":
           "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}	
session = requests.Session()
		   
app = Flask(__name__)
url = "tacticsboardshop.wufoo.com" 

recaptchasitekey = "6Lds3D8UAAAAAPcAz2bYCfSuvZYffjOXi6bVvPhO" 
port = "9999"
names = ["Beck", "Glenn", "Becker", "Carl", "Beckett", "Samuel", "Beddoes", "Mick", "Beecher", "HenryWard", "Beethoven",
         "Ludwigvan", "Begin", "Menachem", "Bell", "Alexander", "Graham", "Belloc", "Hilaire", "Bellow", "Saul",
         "Benchley", "Robert", "Benenson", "Peter", "BenGurion", "David", "Benjamin", "Walter", "Benn", "Tony",
         "Bennington", "Chester", "Benson", "Leana", "Bent", "Silas", "Bentsen", "Lloyd", "Berger", "Ric", "Bergman",
         "Ingmar", "Berio", "Luciano", "Berle", "Milton", "Berlin", "Irving", "Berne", "Eric", "Bernhard", "Sandra",
         "Berra", "Yogi", "Berry", "Halle", "Berry", "Wendell", "Bethea", "Erin", "Bevan", "Aneurin", "Bevel", "Ken",
         "Biden", "Joseph", "Bierce", "Am", "Brose", "Biko", "Steve", "Billings", "Josh", "Biondo", "Frank", "Birrell",
         "Augustine", "Black", "Elk", "Blair", "Ro", "Bert", "Blair", "Tony", "Blake", "William", "Blakey", "Art",
         "Blalock", "Jolene", "Blanc", "Mel", "Blanc", "Raymond", "Blanchet", "Cate", "Blix", "Hans", "Blood",
         "Rebecca"]
sizes = ['7', '7.5', '8', '8.5', '9', '9.5', '10', '10.5', '11', '11.5', '12', '13']
catchall = "@deeznuts.io", #change this to your catchall domain
proxy = ["0.0.0.1:1000", "0.0.0.2:2222", "3.3.3.3:3333"]  # change this

proxies = {
    "https": random.choice(proxy)
}	   
print("Tactics Raffle Script by @Fayeezus"),
print("Starting Now..."), 
# CHANGE the fields as the comments say
# app.debug = true
@app.route('/')
@app.route('/submit', methods=['GET', 'POST'])
def main():
    sitekey = recaptchasitekey
    if request.method == "POST":
        token = request.form.get('g-recaptcha-response')
		
        api = 'https://tacticsboardshop.wufoo.com/embed/r1l2gsha0qmrlgy/#public'
        form = {
            "refer_source": "https://tacticsboardshop.wufoo.com/embed/r1l2gsha0qmrlgy/#public",
            "entry_source": "https://tacticsboardshop.wufoo.com/embed/r1l2gsha0qmrlgy/#public",  
            "Field1": names[random.randint(0, 99)],
            "Field2": names[random.randint(0, 99)],
            "Field3": names[random.randint(0, 99)] + catchall,		
            "Field4": sizes[random.randint(0, 11)],
            "currentPage": "62OYKaexXcJLfslbGbJJd1uoLKTDwMON4duqld9RR60=", #dont change
            "saveForm": "Submit", #dont change
            "g-recaptcha-response": token
        }
        time.sleep (1)
        resp = session.post(api, data=form, headers=headers, proxies=proxies)
        print(response.text)
		
    return render_template('home.html', sitekey=sitekey)

if __name__ == "__main__":
  print("each entry will be submitted after each captcha is solved.")
  webbrowser.open("http://" + url + ":" + port + "/")
  app.run(port=port)
