import logging
from flask import Flask, render_template, Response, request, redirect, url_for, jsonify
import pymysql
import json
import datetime
import random

#initializing mysql database connection
db = pymysql.connect("localhost", "hop_owner", "", "hop_to_it")

#initializing app
app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('home.html')

#Login test ------------------------------------
@app.route('/login/')
def loginSysL():
	return render_template('user_systems/login.php')

@app.route('/welcome')
def welcomeBiches():
	return render_template('user_systems/welcome.php')

#----------------------------------------------

@app.route('/advanced_search/')
def advanced_search():
	return render_template('advanced_search.html')

@app.route('/admin/insert/')
def admin_insert():
	db_cursor = db.cursor()
	query_list = []
	breweries = "Select * from Brewery;"
	query_list.append(breweries)
	styles = "Select * from BEER_STYLE;"
	query_list.append(styles)
	availability = "Select * from SEASONAL_AVAILABILITY;"
	query_list.append(availability)
	price_range = "Select * from PRICE_RANGE;"
	query_list.append(price_range)
	regions = "Select * from Region;"
	query_list.append(regions)

	brewery_data = []
	style_data = []
	availability_data = []
	price_range_data = []
	regions_data = []

	for query in range(0, len(query_list)):
		db_cursor.execute(query_list[query])
		headers=[header[0] for header in db_cursor.description] #return headers with values
		data = db_cursor.fetchall()
		for attribute in data:
			if query == 0:
				brewery_data.append(dict(zip(headers,attribute)))
			elif query == 1:
				style_data.append(dict(zip(headers,attribute)))
			elif query == 2:
				availability_data.append(dict(zip(headers,attribute)))
			elif query == 3:
				price_range_data.append(dict(zip(headers,attribute)))
			else:
				regions_data.append(dict(zip(headers,attribute)))

	return render_template('insert.html', breweries=(brewery_data), styles=(style_data), prices=(price_range_data), availabilities=(availability_data), regions=(regions_data))

@app.route('/admin/remove/')
def admin_remove():
	db_cursor = db.cursor()
	query_list = []
	breweries = "Select * from Brewery;"
	query_list.append(breweries)
	bars = "Select * from Bar;"
	query_list.append(bars)
	food_pairing = "Select * from FOOD_PAIRING;"
	query_list.append(food_pairing)
	beers = "Select * from Beer;"
	query_list.append(beers)

	brewery_data = []
	bar_data = []
	food_pairing_data = []
	beer_data = []

	for query in range(0, len(query_list)):
		db_cursor.execute(query_list[query])
		headers=[header[0] for header in db_cursor.description] #return headers with values
		data = db_cursor.fetchall()
		for attribute in data:
			if query == 0:
				brewery_data.append(dict(zip(headers,attribute)))
			elif query == 1:
				bar_data.append(dict(zip(headers,attribute)))
			elif query == 2:
				food_pairing_data.append(dict(zip(headers,attribute)))
			else:
				beer_data.append(dict(zip(headers,attribute)))

	return render_template('remove.html', breweries=(brewery_data), bars=(bar_data), food_pairings=(food_pairing_data), beers=(beer_data))

@app.route('/admin/remove/brewery', methods=['GET', 'POST'])
def remove_brewery():
	db_cursor = db.cursor()
	brewery_id = request.form["brewery_id"]
	remove_query = "DELETE FROM brewery WHERE brewery_id = %s"
	db_cursor.execute(remove_query, (brewery_id))
	db.commit()

	return render_template('remove.html')

@app.route('/admin/remove/beer', methods=['GET', 'POST'])
def remove_beer():
	db_cursor = db.cursor()
	beer_id = request.form["beer_id"]
	remove_query = "DELETE FROM beer WHERE beer_id = %s"
	db_cursor.execute(remove_query, (beer_id))
	db.commit()

	return render_template('remove.html')

@app.route('/admin/remove/beer_food', methods=['GET', 'POST'])
def remove_beer_food():
	db_cursor = db.cursor()
	food_id = request.form["food_id"]
	remove_query = "DELETE FROM FOOD_PAIRING WHERE food_id = %s"
	print remove_query, "id: ", food_id
	db_cursor.execute(remove_query, (food_id))
	db.commit()

	return render_template('remove.html')

@app.route('/admin/remove/bar', methods=['GET', 'POST'])
def remove_bar():
	db_cursor = db.cursor()
	bar_id = request.form["bar_id"]
	remove_query = "DELETE FROM bar WHERE bar_id = %s"
	db_cursor.execute(remove_query, (bar_id))
	db.commit()

	return render_template('remove.html')

@app.route('/admin/insert/brewery', methods=['GET', 'POST'])
def insert_brewery():
	db_cursor = db.cursor()
	name = request.form["name"]
	date_established = request.form["date_established"]
	phone_number = request.form["phone_number"]
	website = request.form["website"]
	city = request.form["city"]
	state = request.form["state"]
	country = request.form.get("country")
	zipcode = int(request.form["zipcode"])
	region_id = request.form.get("region_id")
	history_description = request.form["history_description"]

	insert_query = "INSERT INTO BREWERY (name, date_established, phone_number, website, city, country, state, zipcode, region_id, history_description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
	db_cursor.execute(insert_query, (str(name), str(date_established), str(phone_number), str(website), str(city), str(country), str(state), int(zipcode), int(region_id), str(history_description)))
	db.commit()

	return render_template('insert.html')

@app.route('/admin/insert/beer', methods=['GET', 'POST'])
def insert_beer():
	db_cursor = db.cursor()
	beer_name = request.form["beer_name"]
	alcohol_by_volume = request.form["alcohol_by_volume"]
	ibu_rank = request.form["ibu_rank"]
	standard_reference_method = request.form["standard_reference_method"]
	style_id = request.form["style_id"]
	time_of_year_availability_id = request.form["time_of_year_availability_id"]
	price_range_code = request.form.get("price_range_code")
	brewery_id = request.form["brewery_id"]

	insert_query = "INSERT INTO BEER (beer_name, alcohol_by_volume, ibu_rank, standard_reference_method, style_id, time_of_year_availability_id, price_range_code, brewery_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
	db_cursor.execute(insert_query, (str(beer_name), (alcohol_by_volume), (ibu_rank), (standard_reference_method), int(style_id), int(time_of_year_availability_id), int(price_range_code), int(brewery_id)))
	db.commit()

	return render_template('insert.html')

@app.route('/admin/insert/beer_food', methods=['GET', 'POST'])
def insert_beer_food():
	db_cursor = db.cursor()
	food_type = request.form["food_type"]

	insert_query = "INSERT INTO FOOD_PAIRING(food_type) VALUES (%s);"
	db_cursor.execute(insert_query, (str(food_type)))
	db.commit()

	return render_template('insert.html')

@app.route('/admin/insert/bar', methods=['GET', 'POST'])
def insert_bar():
	db_cursor = db.cursor()
	bar_name = request.form["bar_name"]
	city = request.form["city"]
	state = request.form["state"]
	country = request.form["country"]
	zipcode = request.form["zipcode"]
	website_url = request.form["website_url"]
	phone_number = request.form.get("phone_number")

	insert_query = "INSERT INTO BAR(bar_name, city, state, country, zipcode, website_url, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s);"
	db_cursor.execute(insert_query, (str(bar_name), str(city), str(state), str(country), int(zipcode), str(website_url), str(phone_number)))
	db.commit()

	return render_template('insert.html')

# @app.route('/admin/login/')
# def admin_login():
# 	username = request.form.get('username')
# 	password = request.form.get('password')
# 	db_cursor = db.cursor()
# 	username_query = ("Select username from users where username = '{}';".format(username))
# 	password_query = ("Select password from users where password = '{}';".format(password))
#
# 	if username == username_query and password == password_query:
# 		db_cursor.execute(query)
# 		headers=[header[0] for header in db_cursor.description] #return headers with values
# 		data = db_cursor.fetchall()
# 		json_data=[]
# 		for attribute in data:
# 			json_data.append(dict(zip(headers,attribute)))
# 		return render_template('admin_login.html', data=(json_data))
# 	else:
# 		return render_template('login_error.html')


@app.route('/search/', methods=['POST'])
def search_post():
	text = request.form['text']
	search_term = text.upper()
	db_cursor = db.cursor()
	query = ("Select * from {}".format(search_term))
	db_cursor.execute(query)
	headers=[header[0] for header in db_cursor.description] #return headers with values
	data = db_cursor.fetchall()
	json_data=[]
	for attribute in data:
		json_data.append(dict(zip(headers,attribute)))
	return render_template('search.html', search_term=search_term, search_results=(json_data))

@app.route('/breweries/')
def breweries():
	# db_cursor = db.cursor()
	# # data = db_cursor.fetchone()
	# db_cursor.execute("Select * from Brewery")
	# headers=[header[0] for header in db_cursor.description] #return headers with values
	# data = db_cursor.fetchall()
	# json_data=[]
	# for attribute in data:
	# 	json_data.append(dict(zip(headers,attribute)))
	# # return render_template('brewery_info.html', data=json.dumps(json_data, default=date_handler))
	# return render_template('breweries.html', data=(json_data))
	# # return  jsonify(data)
	db_cursor = db.cursor()
	query_list = []
	breweries = "Select * from Brewery;"
	query_list.append(breweries)
	regions = "Select * from Region;"
	query_list.append(regions)

	brewery_data = []
	regions_data = []

	for query in range(0, len(query_list)):
		db_cursor.execute(query_list[query])
		headers=[header[0] for header in db_cursor.description] #return headers with values
		data = db_cursor.fetchall()
		for attribute in data:
			if query == 0:
				brewery_data.append(dict(zip(headers,attribute)))
			else:
				regions_data.append(dict(zip(headers,attribute)))

	return render_template('breweries.html', breweries=(brewery_data), regions=(regions_data))

@app.route('/breweries/filter_by/', methods=['GET', 'POST'])
def filter_breweries():
	db_cursor = db.cursor()
	region_id = request.form.get("region_id")
	filter_query = "Select name From Brewery Where region_id=%s;"
	db_cursor.execute(filter_query, (int(region_id)))

	headers=[header[0] for header in db_cursor.description] #return headers with values
	data = db_cursor.fetchall()
	json_data=[]
	for attribute in data:
		json_data.append(dict(zip(headers,attribute)))
	return render_template('breweries.html', breweries=(json_data))
	# return render_template('breweries.html', breweries=(brewery_data), regions=(regions_data))

@app.route('/beers/filter_by/', methods=['GET', 'POST'])
def filter_beers():
	db_cursor = db.cursor()
	style_id = request.form.get("style_id")
	filter_query = "Select beer_name From Beer Where style_id=%s;"
	db_cursor.execute(filter_query, (int(style_id)))

	headers=[header[0] for header in db_cursor.description] #return headers with values
	data = db_cursor.fetchall()
	json_data=[]
	for attribute in data:
		json_data.append(dict(zip(headers,attribute)))
	return render_template('beers.html', beers=(json_data))
	# return render_template('breweries.html', breweries=(brewery_data), regions=(regions_data))

@app.route('/beers/')
def beers():
	db_cursor = db.cursor()
	# data = db_cursor.fetchone()
	query = """SELECT b.beer_name, b.alcohol_by_volume, b.ibu_rank, b.standard_reference_method, bs.style_name, b.time_of_year_availability_id, pr.price_range, br.name
				FROM beer b INNER JOIN BEER_STYLE bs ON (b.style_id = bs.style_id)
				INNER JOIN PRICE_RANGE pr ON (b.price_range_code = pr.price_range_code)
				INNER JOIN BREWERY br ON (b.brewery_id = br.brewery_id);"""
	# db_cursor.execute(query)
	# headers=[header[0] for header in db_cursor.description] #return headers with values
	# data = db_cursor.fetchall()
	# json_data=[]
	# for attribute in data:
	# 	json_data.append(dict(zip(headers,attribute)))
	# return render_template('beers.html', beers=(json_data))
	query_list = []
	query_list.append(query)
	styles = "Select * from BEER_STYLE;"
	query_list.append(styles)

	beers_data = []
	styles_data = []

	for query in range(0, len(query_list)):
		db_cursor.execute(query_list[query])
		headers=[header[0] for header in db_cursor.description] #return headers with values
		data = db_cursor.fetchall()
		for attribute in data:
			if query == 0:
				beers_data.append(dict(zip(headers,attribute)))
			else:
				styles_data.append(dict(zip(headers,attribute)))

	return render_template('beers.html', beers=(beers_data), styles=(styles_data))

@app.route('/bars/')
def bars():
	db_cursor = db.cursor()
	# data = db_cursor.fetchone()
	query = """SELECT * FROM BAR;"""
	db_cursor.execute(query)
	headers=[header[0] for header in db_cursor.description] #return headers with values
	data = db_cursor.fetchall()
	json_data=[]
	for attribute in data:
		json_data.append(dict(zip(headers,attribute)))
	# return render_template('brewery_info.html', data=json.dumps(json_data, default=date_handler))
	return render_template('bars.html', bars=(json_data))
	# return  jsonify(data)


@app.route('/brewery_info/<brewery>')
def brewery_info(brewery):
	db_cursor = db.cursor()
	query = "Select * from Brewery where name = '{}';".format(brewery)
	db_cursor.execute(query)
	headers=[header[0] for header in db_cursor.description] #return headers with values
	data = db_cursor.fetchall()
	json_data=[]
	for attribute in data:
		json_data.append(dict(zip(headers,attribute)))
	# return render_template('brewery_info.html', data=json.dumps(json_data, default=date_handler))
	return render_template('brewery_info.html', brewery=brewery, data=(json_data))

@app.route('/beers/<brewery>/')
def brewery_beers(brewery):
	# brewery_name = brewery.replace('_', "")
	db_cursor = db.cursor()
	query = """SELECT b.beer_name, b.alcohol_by_volume, b.ibu_rank, b.standard_reference_method, bs.style_name,
			b.time_of_year_availability_id, pr.price_range, br.name
			FROM beer b INNER JOIN BEER_STYLE bs ON (b.style_id = bs.style_id)
			INNER JOIN PRICE_RANGE pr ON (b.price_range_code = pr.price_range_code)
			INNER JOIN BREWERY br ON (b.brewery_id = br.brewery_id)
			WHERE (br.name = "{}");""".format(brewery)
	db_cursor.execute(query)
	headers=[header[0] for header in db_cursor.description] #return headers with values
	data = db_cursor.fetchall()
	json_data=[]
	for attribute in data:
		json_data.append(dict(zip(headers,attribute)))
	return render_template('brewery_beers.html', brewery=brewery, beers=(json_data))

def date_handler(attribute):
    # if hasattr(attribute, 'isoformat'):
    #     return str(attribute)
	if isinstance(attribute, datetime.datetime):
		return attribute.isoformat()

@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)

if __name__ == "__main__":
    app.run(debug=True)
