import requests
from time import sleep
from lxml import etree  # because xml.etree doesn't have DOCTYPE support and pretty printing

# author ayberk

# function to make rate api call, returns latest rate and time
def fetch_latest_rate():
    #getting request from bloomberg api
    response = requests.get("http://www.bloomberght.com/piyasa/intradaydata/dolar")
    #putting corresponding data to an array
    arr = response.json()['SeriesData']
    #taking the last data
    latest_time = arr[-1][0]
    latest_rate = arr[-1][1]
    return (latest_rate, latest_time)


# function to initialize html elements, returns root element
def create_page_skeleton(timestamp_tag, rate_tag):
    # create base elements
    html_tag = etree.Element('html', attrib={'lang': 'en'})
    head_tag = etree.SubElement(html_tag, 'head')
    body_tag = etree.SubElement(html_tag, 'body')

    # include libraries jquery etc.
    jquery = etree.SubElement(head_tag, 'script', attrib={
        'src': "https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"}).text = ''
    moment = etree.SubElement(head_tag, 'script',
                              attrib={'src': "https://rawgit.com/moment/moment/2.2.1/min/moment.min.js"}).text = ''

    # attach elements with dynamic content
    body_tag.append(timestamp_tag)
    body_tag.append(rate_tag)

    h1_tag_date = etree.SubElement(body_tag, 'h1', attrib={'id': 'date'}).text = ''

    # add client side code as javascript runs on client side
    readyFunction = etree.SubElement(body_tag, 'script').text = '''     
      $(document).ready(function() {
        $("#date").text(moment.unix($('#timestamp').text() / 1000).format('DD-MM-YYYY HH:mm'));
      });

      setTimeout(function() {
        location.reload();
      }, 30000);
    ''' # setTimeout allows html website refresh itself in every 30 seconds.
    return html_tag


# initialize elements with dynamic content
h1_tag_timestamp = etree.Element('h1', attrib={'id': 'timestamp'})
h1_tag_rate = etree.Element('h1', attrib={'id': 'rate'})
root = create_page_skeleton(h1_tag_timestamp, h1_tag_rate)

while (1):
    # fetch data and generate html file
    (rate, timestamp) = fetch_latest_rate()
    h1_tag_rate.text = str(rate)
    h1_tag_timestamp.text = str(timestamp)
    etree.ElementTree(root).write("./test.html", method='xml', doctype="<!DOCTYPE html>", pretty_print=True)
    # wait a bit between requests
    sleep(1)