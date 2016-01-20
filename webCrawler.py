import requests
from bs4 import BeautifulSoup

items={}
flipkart= {}
snapdeal= {}


def searchTheItem(itemname=None):
    items.clear()
    flipkart.clear()
    snapdeal.clear()

    count_fk=0
    count_sd=0
    url_flipkart = "http://www.flipkart.com/search?pr?p%5B%5D=sort%3Dpopularity&sid=tyy&q="+itemname
    url_snapdeal = "http://www.snapdeal.com/search?keyword="+itemname


    sourcecode_flipkart = requests.get(url_flipkart)
    sourcecode_snapdeal = requests.get(url_snapdeal)

    plaintext_flipkart = sourcecode_flipkart.text
    plaintext_snapdeal = sourcecode_snapdeal.text

    soup_flipkart_name = BeautifulSoup(plaintext_flipkart,"html.parser")
    soup_snapdeal_name = BeautifulSoup(plaintext_snapdeal,"html.parser")
    soup_flipkart_price = soup_flipkart_name
    soup_snapdeal_price = soup_snapdeal_name



    for each_item_flipkart in soup_flipkart_name.findAll('div',{'class':'pu-title'}) :

        if count_fk <=5:
            count=0

            name = each_item_flipkart.text

            for each_item_price in soup_flipkart_price.findAll('div',{'class':'pu-final'}):
                if count == count_fk:
                    price = each_item_price.text
                    flipkart[name] = price
                    count+=1
                elif count > count_fk:
                    break
                else:
                     count+=1

            count_fk+=1

        else:
                break



    for each_item_snapdeal in soup_snapdeal_name.findAll('p',{'class':'product-title'}) :

        if count_sd <=5:
            count=0

            name = each_item_snapdeal.text

            for each_item_price in soup_snapdeal_price.findAll('span',{'class':'product-price'}):
                if count == count_sd:
                    price = each_item_price.text
                    snapdeal[name] = price
                    count+=1
                elif count > count_sd:
                    break
                else:
                     count+=1

            count_sd+=1

        else:
                break


    items["flipkart"] = flipkart
    items["snapdeal"] = snapdeal


    return items






