from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"ef0e4baeed34c0964a8f5ba6fadbc0e4"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		price_range = {'low':1,'mid':2,'high':3}
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 500)
		d = json.loads(results)
		restaurants = sorted(d['restaurants'], key=lambda rest: rest['restaurant']['user_rating']['aggregate_rating'], reverse=True)
		response=""
		restaurant_cnt=0
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in restaurants:
				if((price_range.get(price) == 1) and (restaurant['restaurant']['average_cost_for_two'] < 300) and (restaurant_cnt < 10)):
    					response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " with average budget of "+ str(restaurant['restaurant']['average_cost_for_two'])+" for two people has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
    					restaurant_cnt = restaurant_cnt + 1
				elif((price_range.get(price) == 2) and (restaurant['restaurant']['average_cost_for_two'] >= 300) and (restaurant['restaurant']['average_cost_for_two'] <= 700) and (restaurant_cnt < 10)):
    					response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " with average budget of "+ str(restaurant['restaurant']['average_cost_for_two'])+" for two people has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
    					restaurant_cnt=restaurant_cnt+1
				elif((price_range.get(price) == 3) and (restaurant['restaurant']['average_cost_for_two'] > 700) and (restaurant_cnt < 10)):
    					response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " with average budget of "+ str(restaurant['restaurant']['average_cost_for_two'])+" for two people has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
    					restaurant_cnt=restaurant_cnt+1   
				if(restaurant_cnt==5):
    					dispatcher.utter_message(response) 
                    	          	             
		if(restaurant_cnt<5 and restaurant_cnt>0):
    			dispatcher.utter_message(response)
		if(restaurant_cnt==0):
    			response = "No restaurants found for your criteria."
    			dispatcher.utter_message(response)
		return [SlotSet('emailbody',response)]
    
class ActionCheckLocation(Action):
    	def name(self):
    			return 'action_checklocation'
		
    	def run(self, dispatcher, tracker, domain):
    			loc = tracker.get_slot('location')
    			cities_in_tier1and2 = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Lucknow', 'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Ahmedabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore', 'Nagpur', 'Cuttack', 'Dehradun', 'Dhanbad', 'Durg-Bhilai Nagar', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur',' Kanpur','Kochi','Kottayam','Kolhapur','Kollam','Kota','Kozhikode','Kurnool', 'Ludhiana','Madurai','Malappuram','Mathura','Goa','Mangalore','Meerut','Moradabad','Mysore', 'Nanded', 'Nashik','Nellore','Noida','Palakkad','Patna','Pondicherry','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Siliguri', 'Solapur','Srinagar','Sultanpur','Surat','Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 'Tiruppur', 'Tiruvannamalai', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal']
    			cities_final=[x.lower() for x in cities_in_tier1and2]
    			if loc.lower() not in cities_final:
    					dispatcher.utter_message("We do not operate in that area yet")
    					return [SlotSet('location','not_found')]
    			return

class ActionSendEmail(Action):
    	def name(self):
    			return 'action_sendemail'

    	def run(self, dispatcher, tracker, domain):
    			bot_id = 'restaurant.chatbotfoodie@gmail.com'
    			customer_id = tracker.get_slot('email')
    			password = 'upgrad@study'
    			email_body = tracker.get_slot('emailbody')
    			msg = MIMEMultipart()
    			msg['From'] = bot_id
    			msg['TO'] = customer_id
    			msg['Subject'] = 'Foodie suggests you these restaurants !!'
    			msg.attach(MIMEText(email_body,'plain'))
    			session = smtplib.SMTP('smtp.gmail.com',587)
    			session.starttls()
    			session.login(bot_id, password)
    			text = msg.as_string()
    			session.sendmail(bot_id,customer_id,text)
    			session.quit()