from flask import Flask, render_template,request
import requests
import webbrowser
import webCrawler

Pricer = Flask(__name__)


@Pricer.route('/')
def home_page():
    return render_template("homepage.html")

@Pricer.route('/search_for_item', methods=['POST'])
def search_for_item():
    itemSet = {}
    if len(request.form['search_item']) == 0 :

        return "please enter an item!"

    else:

            itemSet = webCrawler.searchTheItem(request.form['search_item'])
            return render_template("display_results.html", itemsRecieved= itemSet, requested_item=request.form['search_item'])




if __name__ == '__main__':
   Pricer.run()
