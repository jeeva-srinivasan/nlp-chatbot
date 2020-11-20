## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "More than Rs. 700"}
    - slot{"price": "More than Rs. 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* goodbye
    - utter_goodbye
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* goodbye
    - utter_goodbye
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "More than Rs. 700"}
    - slot{"price": "More than Rs. 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_checklocation
* greet

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_checklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "tokyo"}
    - slot{"location": "tokyo"}
    - action_checklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "tokyo"}
    - slot{"location": "tokyo"}
    - action_checklocation
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_checklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": "AB's - Absolute Barbecues in 45, GN Chetty Road, T. Nagar, Chennai with price 1400 has been rated 4.8\nEast Coast At Madras Square in 2/520 D, 2nd Avenue, Sandeep Nagar Main Road, Neelangarai, Chennai with price 1700 has been rated 4.6\nCoal Barbecues in Shop 17 & 18, Rajalakshmi Nagar, 7th Cross Street, 100 Feet Bypass Road, Velachery, Chennai with price 1400 has been rated 4.5\nSoy Soi in 2/10, Gandhi Mandapam Road, Kotturpuram, Chennai with price 1400 has been rated 4.5\nBasil With A Twist in 58-A, Habibullah Road, T. Nagar, Chennai with price 1500 has been rated 4.5\nCoal Barbecues in 40, 2nd Floor, Bazullah Road, T. Nagar, Chennai with price 1400 has been rated 4.4\nFromage in Somerset Greenway, Lords Avenue, MRC Nagar, Chennai with price 1000 has been rated 4.4\nWild Garden Cafe - Amethyst in Whites Road, Royapettah, Chennai  with price 1400 has been rated 4.4\nSukkubhai Biriyani in New 14, Old 11/3Q, Railway Station Road, MKN Road, Near Antony Church, Alandur, Chennai with price 1000 has been rated 4.3\nAmelie's in 6,Seshadri Road, Venus Colony, Alwarpet, Chennai with price 900 has been rated 4.3\n"}
* restaurant_search

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_checklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": "AB's - Absolute Barbecues in 45, GN Chetty Road, T. Nagar, Chennai with price 1400 has been rated 4.8\nEast Coast At Madras Square in 2/520 D, 2nd Avenue, Sandeep Nagar Main Road, Neelangarai, Chennai with price 1700 has been rated 4.6\nCoal Barbecues in Shop 17 & 18, Rajalakshmi Nagar, 7th Cross Street, 100 Feet Bypass Road, Velachery, Chennai with price 1400 has been rated 4.5\nSoy Soi in 2/10, Gandhi Mandapam Road, Kotturpuram, Chennai with price 1400 has been rated 4.5\nBasil With A Twist in 58-A, Habibullah Road, T. Nagar, Chennai with price 1500 has been rated 4.5\nCoal Barbecues in 40, 2nd Floor, Bazullah Road, T. Nagar, Chennai with price 1400 has been rated 4.4\nFromage in Somerset Greenway, Lords Avenue, MRC Nagar, Chennai with price 1000 has been rated 4.4\nWild Garden Cafe - Amethyst in Whites Road, Royapettah, Chennai  with price 1400 has been rated 4.4\nSukkubhai Biriyani in New 14, Old 11/3Q, Railway Station Road, MKN Road, Near Antony Church, Alandur, Chennai with price 1000 has been rated 4.3\nAmelie's in 6,Seshadri Road, Venus Colony, Alwarpet, Chennai with price 900 has been rated 4.3\n"}
    - utter_ask_emailmessage
* affirm
    - utter_ask_emailid
* restaurant_search{"email": "findjeeva1@gmail.com"}
    - slot{"email": "findjeeva1@gmail.com"}
    - action_sendemail
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "tokyo"}
    - slot{"location": "tokyo"}
    - action_checklocation
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_checklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": "AB's - Absolute Barbecues in Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad with price 1200 has been rated 4.9\nLé Vantage Cafe Bar in Plot 197/A & 197, Road 13, Jubilee Hills, Hyderabad with price 1000 has been rated 4.5\nCoffee Cup in E 89, 1st Floor, Near Canara Bank, Sainikpuri, Secunderabad with price 800 has been rated 4.5\nConçu in Plot 738, Road 37, Jubilee Hills, Hyderabad with price 1000 has been rated 4.4\nFat Pigeon - Bar Hop in Plot 1335/A, Road 45, Jubilee Hills, Hyderabad with price 2200 has been rated 4.4\nBawarchi in Plot 44, RTC Cross Road, Chikkadpally, Opposite Sandhya Theatre, Nallakunta, Hyderabad with price 750 has been rated 4.3\nThe Roastery Coffee House in 8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad with price 800 has been rated 4.3\nOlive Bistro & Bar in Road 46, Jubilee Hills, Hyderabad with price 2000 has been rated 4.3\nExotica in Door 8-2-686/B/6/PH, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad with price 1800 has been rated 4.3\nFarzi Cafe in Door.No:8-2-296/82/A/1200, Plot.No:1200, Road.no:59, Jubileehills,Hyderabad with price 1800 has been rated 4.3\n"}
    - utter_ask_emailmessage
* affirm
    - utter_ask_emailid
* restaurant_search{"email": "findjeeva1@gmail.com"}
    - slot{"email": "findjeeva1@gmail.com"}
    - action_sendemail
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": "Truffles in 28, 4th B Cross, Koramangala 5th Block, Bangalore with price 900 has been rated 4.8\nBurma Burma in 607, Ground Floor, 12th Main, Hal 2nd Stage, Indiranagar, Bangalore with price 1500 has been rated 4.7\nCommuniti in 67 & 68, Brigade Solitaire, Opposite Advaith Hyundai, Residency Road, Bangalore with price 1500 has been rated 4.7\nWindmills Craftworks in 331, EPIP Area, Road 5B, Near KTPO, Whitefield, Bangalore with price 2500 has been rated 4.7\nBrahma Brews in Opposite Brigade Palm Springs, 24th Main, 7th Phase, JP Nagar, Bangalore with price 1900 has been rated 4.6\nByg Brewski Brewing Company in Opposite MK Retail, Sarjapur Road, Bangalore with price 1600 has been rated 4.4\nToit in 298, 100 Feet Road, Namma Metro Pillar 62, Indiranagar, Bangalore with price 2000 has been rated 4.4\nMISU in 4th Floor, Building 9, Halcyon Complex, St. Marks Road, Bangalore with price 1700 has been rated 4.4\nBiergarten in 2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore with price 2400 has been rated 4.3\nTBC Sky Lounge in Astra Hotel, 2795, 27th Main, Sector 1, HSR, Bangalore with price 1600 has been rated 4.3\n"}
    - utter_ask_emailmessage
* affirm
    - utter_ask_emailid
* restaurant_search{"email": "findjeeva1@gmail.com"}
    - slot{"email": "findjeeva1@gmail.com"}
    - action_sendemail
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": "AB's - Absolute Barbecues in 45, GN Chetty Road, T. Nagar, Chennai with price 1400 has been rated 4.8\nEast Coast At Madras Square in 2/520 D, 2nd Avenue, Sandeep Nagar Main Road, Neelangarai, Chennai with price 1700 has been rated 4.6\nCoal Barbecues in Shop 17 & 18, Rajalakshmi Nagar, 7th Cross Street, 100 Feet Bypass Road, Velachery, Chennai with price 1400 has been rated 4.5\nSoy Soi in 2/10, Gandhi Mandapam Road, Kotturpuram, Chennai with price 1400 has been rated 4.5\nBasil With A Twist in 58-A, Habibullah Road, T. Nagar, Chennai with price 1500 has been rated 4.5\nCoal Barbecues in 40, 2nd Floor, Bazullah Road, T. Nagar, Chennai with price 1400 has been rated 4.4\nFromage in Somerset Greenway, Lords Avenue, MRC Nagar, Chennai with price 1000 has been rated 4.4\nWild Garden Cafe - Amethyst in Whites Road, Royapettah, Chennai  with price 1400 has been rated 4.4\nSukkubhai Biriyani in New 14, Old 11/3Q, Railway Station Road, MKN Road, Near Antony Church, Alandur, Chennai with price 1000 has been rated 4.3\nAmelie's in 6,Seshadri Road, Venus Colony, Alwarpet, Chennai with price 900 has been rated 4.3\n"}
    - utter_ask_emailmessage
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_checklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": "AB's - Absolute Barbecues in 45, GN Chetty Road, T. Nagar, Chennai with price 1400 has been rated 4.8\nEast Coast At Madras Square in 2/520 D, 2nd Avenue, Sandeep Nagar Main Road, Neelangarai, Chennai with price 1700 has been rated 4.6\nCoal Barbecues in Shop 17 & 18, Rajalakshmi Nagar, 7th Cross Street, 100 Feet Bypass Road, Velachery, Chennai with price 1400 has been rated 4.5\nSoy Soi in 2/10, Gandhi Mandapam Road, Kotturpuram, Chennai with price 1400 has been rated 4.5\nBasil With A Twist in 58-A, Habibullah Road, T. Nagar, Chennai with price 1500 has been rated 4.5\nCoal Barbecues in 40, 2nd Floor, Bazullah Road, T. Nagar, Chennai with price 1400 has been rated 4.4\nFromage in Somerset Greenway, Lords Avenue, MRC Nagar, Chennai with price 1000 has been rated 4.4\nWild Garden Cafe - Amethyst in Whites Road, Royapettah, Chennai  with price 1400 has been rated 4.4\nSukkubhai Biriyani in New 14, Old 11/3Q, Railway Station Road, MKN Road, Near Antony Church, Alandur, Chennai with price 1000 has been rated 4.3\nAmelie's in 6,Seshadri Road, Venus Colony, Alwarpet, Chennai with price 900 has been rated 4.3\n"}
    - utter_ask_emailmessage
* affirm
    - utter_ask_emailid
* restaurant_search{"email": "findjeeva1@gmail.com"}
    - slot{"email": "findjeeva1@gmail.com"}
    - action_sendemail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_checklocation
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"emailbody": "Great Wall in E-97, 3rd Main Road, Besant Nagar, Chennai with price 550 has been rated 4.1\nThe Noodle Theory in 106/26, Landon's Road, Kilpauk, Chennai with price 450 has been rated 4.0\nDallay in 18/11, Nagendra Nagar, Velachery, Chennai with price 350 has been rated 3.9\nDragon's Den in New 8/2, Old 5/2, MG Road, Adyar, Chennai with price 500 has been rated 3.8\nHuTong in 2/15, Ganapathy Colony Main Road, Near Bank of Baroda ATM, Sri Ram Nagar, Teynampet, Chennai with price 700 has been rated 3.8\n"}
* restaurant_search

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_checklocation
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"emailbody": "Great Wall in E-97, 3rd Main Road, Besant Nagar, Chennai with price 550 has been rated 4.1\nThe Noodle Theory in 106/26, Landon's Road, Kilpauk, Chennai with price 450 has been rated 4.0\nDallay in 18/11, Nagendra Nagar, Velachery, Chennai with price 350 has been rated 3.9\nDragon's Den in New 8/2, Old 5/2, MG Road, Adyar, Chennai with price 500 has been rated 3.8\nHuTong in 2/15, Ganapathy Colony Main Road, Near Bank of Baroda ATM, Sri Ram Nagar, Teynampet, Chennai with price 700 has been rated 3.8\n"}
    - utter_ask_emailmessage
* affirm
    - utter_ask_emailid
* restaurant_search{"email": "ajiseeni1@gmail.com"}
    - slot{"email": "ajiseeni1@gmail.com"}
    - action_sendemail
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_checklocation
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"emailbody": "Pishu's in Shop 9, Nandkripa Shopping Centre, Ratan Nagar Lane, Near Ganesh Sai Dham Mandir, Market Area, 4 Bungalows, Mumbai with price 400 has been rated 4.1\n"}
    - utter_ask_emailmessage
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Delhi"}
    - slot{"cuisine": "american"}
    - slot{"location": "Delhi"}
    - action_checklocation
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": "The All American Diner in India Habitat Centre, Lodhi Road, New Delhi with average budget of  1800 for two people has been rated 4.3\nSAZ - American Brasserie in 21, 1st Floor, Sunder Nagar Market, Near HDFC Bank, Sunder Nagar, New Delhi with average budget of  2300 for two people has been rated 4.3\nThe American Connection Diner in F1, 2nd Floor, Kalkaji Main Market, Kalkaji, New Delhi with average budget of  1500 for two people has been rated 4.0\nBig Fat Sandwich in A 15/A, Market Lane, Block E, Hauz Khas, New Delhi with average budget of  800 for two people has been rated 4.0\n"}
    - utter_ask_emailmessage
* affirm
    - utter_ask_emailid
* restaurant_search{"email": "findjeeva1@gmail.com"}
    - slot{"email": "findjeeva1@gmail.com"}
    - action_sendemail
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Hyderabad"}
    - action_checklocation
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": "Churrolto in Film Nagar Main Road, Opposite Indian Oil, Film Nagar, Hyderabad with average budget of 1200 for two people has been rated 4.9\nProst Brew Pub in 882/A, Road 45, Jubilee Hills, Hyderabad with average budget of 2200 for two people has been rated 4.6\nLé Vantage Cafe Bar in Plot 197/A & 197, Road 13, Jubilee Hills, Hyderabad with average budget of 1000 for two people has been rated 4.5\nCoffee Cup in E 89, 1st Floor, Near Canara Bank, Sainikpuri, Secunderabad with average budget of 800 for two people has been rated 4.5\nZero40 Brewing in 271-A, Road 10, Jubilee Hills, Hyderabad with average budget of 2400 for two people has been rated 4.5\nBroadway in 8-2-293/82/A/1017, Kavuri Hills, Jubilee Hills, Hyderabad with average budget of 2700 for two people has been rated 4.5\nThe Glass Onion in Survey 236, Vattinagulappally Village, Rajendra Nagar Mandal, Gachibowli, Hyderabad with average budget of 1200 for two people has been rated 4.5\nFat Pigeon - Bar Hop in Plot 1335/A, Road 45, Jubilee Hills, Hyderabad with average budget of 2200 for two people has been rated 4.4\n36 Downtown Brew Pub in Plot 753, Road 36, Jubilee Hills, Hyderabad with average budget of 2500 for two people has been rated 4.4\nThe Roastery Coffee House in 8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad with average budget of 800 for two people has been rated 4.3\n"}
    - utter_ask_emailmessage
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - action_checklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"emailbody": "22nd Parallel in 1st Floor, Tapan Complex, Besides M Cube Mall, Alkapuri, Vadodara with average budget of 400 for two people has been rated 4.6\nJassi De Parathe in R.C Dutt Road, Near Kalaniketan, Alkapuri, Vadodara with average budget of 600 for two people has been rated 4.5\nBrown Burger Co in Near Dairy Den Circle, Sayajiganj, Vadodara with average budget of 500 for two people has been rated 4.4\nShree Kathiyawadi Khadki in Navrang Cinema Road, Near Tower Four Ways, Raopura, Mandvi, Vadodara with average budget of 300 for two people has been rated 4.3\nKFC in 19, Ground Floor, Vadodara Central Mall, Near Genda Circle, Wadi Road, Alkapuri, Vadodara with average budget of 450 for two people has been rated 4.3\nHariyali Restaurant in Vrundavan Heights, Near Parivar Char Rasta, Waghodia, Kendranagar, Vadodara with average budget of 400 for two people has been rated 4.3\nDomino's Pizza in B-33, Ground Floor & 1st Floor, Uma Colony, Housing Society Limited, Waghodia Road, Kendranagar, Vadodara with average budget of 400 for two people has been rated 4.3\nBurger King in 2nd Floor, Inorbit Mall, Subhanpura, Vadodara with average budget of 350 for two people has been rated 4.2\nUstaad Miyaan in 13 Alkapuri shopping center, opposite vishwas colony, Alkapuri, vadodara, Alkapuri, Vadodara with average budget of 600 for two people has been rated 4.2\nBurger King in Shop 8, Ground Floor, Golden Icon, Opposite BSNL Office, Bird Circle, Alkapuri, Vadodara with average budget of 350 for two people has been rated 4.2\n"}
    - utter_ask_emailmessage
* affirm
    - utter_ask_emailid
* restaurant_search{"email": "venusrules25@gmail.com"}
    - slot{"email": "venusrules25@gmail.com"}
    - action_sendemail
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"emailbody": "Mezze in Old 19, New 4, Abhinav Center, Off Chamiers Road, Alwarpet, Chennai with average budget of 700 for two people has been rated 4.5\nYaa Mohaideen Biryani in Old Shop 4/158, Church Road, Opposite Uzhavar Santhai, Pallavaram, Chennai with average budget of 600 for two people has been rated 4.4\nWriter's Cafe in 98, Peter's Road, Near Philip's Service Centre, Gopalapuram, Chennai with average budget of 600 for two people has been rated 4.4\nFusilli Reasons in 2/64, Ormes Main Road, Kilpauk, Chennai with average budget of 400 for two people has been rated 4.4\n"}
    - utter_ask_emailmessage
* goodbye
    - utter_goodbye
