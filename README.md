
Using the USD/TRY Exchange Rate API URL below, project takes the last data of
“SeriesData” list, it prints the timestamp and exchange rate value into separate h1 tag in an
html document. it keeps doing this process in an infinite loop in order to keep values
updated.
http://www.bloomberght.com/piyasa/intradaydata/dolar
In the html page, using Javascript’s jQuery library, it takes
the timestamp value. it then turns this value into readable date-time format, i.e., DD-MM-YYYY
HH:MM. And prints this readable date-time string into another h1 tag in the html document.
Using javascript, it makes the html webpage refresh itself in every 30 seconds. So, anyone can see the exchange rate updates
