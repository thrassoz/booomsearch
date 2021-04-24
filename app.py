from flask import Flask, request, redirect, render_template, url_for
import bs4
import requests


app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        season = ["Λαμπάδες", "λαμπάδες", "ΛΑΜΠΑΔΕΣ", "πασχαλινά", "Πασχαλινά",
        "ΠΑΣΧΑΛΙΝΑ", "ΛΑΜΠΑΔΑ", "λαμπαδα", "λαμπαδες"
        ]
        if request.form['name'] in season:
            return redirect('https://www.booomtoys.gr/el/epoxiaka/pasxalina')
        
        if request.form['name'] != '':
            res = requests.get('https://www.booomtoys.gr/el/products-list&product_search=' + request.form['name'])
            page = bs4.BeautifulSoup(res.text, 'html.parser')
            results = page.select('.prodSliderCart')
            if len(results) > 0:
                return redirect('https://www.booomtoys.gr/el/products-list&product_search=' + request.form['name'], 301)
            else: #decide were to redirect the client if results not found
                return render_template('index.html', key=len(results), posted=request.form)

        elif request.form['code'] != '':
            res = requests.get('https://www.booomtoys.gr/el/products-list&product_search=' + request.form['code'])
            page = bs4.BeautifulSoup(res.text, 'html.parser')
            results = page.select('.prodSliderCart')
            if len(results) > 0:
                return redirect('https://www.booomtoys.gr/el/products-list&product_search=' + request.form['code'], 301)
            else:
                return render_template('index.html', key=len(results), posted=request.form)

        elif request.form['company'] != '':
            res = requests.get('https://www.booomtoys.gr/el/products-list&product_search=' + request.form['company'])
            page = bs4.BeautifulSoup(res.text, 'html.parser')
            results = page.select('.prodSliderCart')
            if len(results) > 0:
                return redirect('https://www.booomtoys.gr/el/products-list&product_search=' + request.form['company'], 301)
            else:
                return render_template('index.html', key=len(results), posted=request.form)
        elif request.form['category'] != '':
            return redirect('https://www.booomtoys.gr/el/' + request.form['category'], 301)
        else:
            return render_template('index.html')
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
