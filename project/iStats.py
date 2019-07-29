from flask import Flask, escape, request
from flask import Markup
from flask import Flask
from forms import searchForm
from flask import render_template
import analysis
import gather

app = Flask(__name__)

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

months = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"]  

days = [
    "Mon", "Tue", "Wed", "Thu",
    "Fri", "Sat", "Sun"] 

times = [
    "12:00", "1:00", "2:00", "3:00",
    "4:00", "5:00", "6:00", "7:00",
    "8:00", "9:00", "10:00", "11:00", "12:00"] 

footer = "Copyright © 2019 iStats: iMessage Statistics. All rights reserved."

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', footer=footer)

@app.route('/most-used')
def bar():
    bar_labels = analysis.w1
    bar_values = analysis.w2
    maxN = bar_values[0] / 100 + 20 + bar_values[0]
    bar_labels2 = analysis.c1
    bar_values2 = analysis.c2
    maxN2 = bar_values2[0] / 100 + 20 + bar_values2[0]
    pie_labels = analysis.e1
    pie_values = analysis.e2
    maxN3 = pie_values[0] / 100 + 20 + pie_values[0]
    return render_template('chart.html', title='iStats - Most Used', max=maxN, labels=bar_labels, values=bar_values, max2=maxN2, labels2=bar_labels2, values2=bar_values2, max3=maxN3, set=zip(pie_values, pie_labels, colors), footer=footer)

@app.route('/most-texted')
def mostTexted():
    mostTexted = analysis.mostTexted
    return render_template('mosttexted.html', title='iStats - Most Texted', number=mostTexted, footer=footer)

@app.route('/character-count')
def charCount():
    minChar = analysis.minChar
    maxChar = analysis.maxChar
    avgChar = analysis.avgChar
    return render_template('charcount.html', title="iStats - Character Count", minChar=minChar, maxChar=maxChar, avgChar=avgChar, footer=footer)

@app.route('/search-a-string', methods=['POST', 'GET'])
def searchAString():
    search = searchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('search.html', title="iStats - Search a String", form=search, footer=footer)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    lst = analysis.getMessageList(search_string)  
    return render_template('searchresults.html', title="iStats - Search a String", results=lst, searchTerm = search_string, footer=footer)


@app.route('/activity-by-date')
def line():
    hours, day, month = gather.date_count(gather.df)
    maxH = max(hours) /100 +20 + max(hours)
    maxM = max(month) /100 +20 + max(month)
    maxD = max(day) /100 +20 + max(day)
    return render_template('date.html', title="iStats - Activity by Date", max=maxM, labels=months, values=month,  max2 = maxD, labels2 = days, values2 = day, max3 = maxH, labels3 = times, values3 = hours, footer=footer)

@app.route('/about')
def about():
    return render_template('about.html', title="iStats - About", footer=footer)

if __name__ == '__main__':
	app.run(debug=True)