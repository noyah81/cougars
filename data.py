
def Locations():
	#these locations will correspond to items in db once established
	locations = [
		{
			'id': 1,
			'title': 'Statue of Liberty',
			'image': 'NewYork-StatueOfLiberty.jpg',
			'url': 'statue-of-liberty'
			'body': 'The Statue of Liberty is made of copper and sits on Ellis Island. She is an icon that represents liberty.',
			'gmapLink': 'https://www.google.com/maps/d/u/0/viewer?msa=0&ie=UTF8&t=m&ll=40.70276500000001%2C-74.032574&spn=0.032534%2C0.102825&z=13&source=embed&mid=1genpW9bQ6PCexDig26nmoPfMWnA',
			'stations': 'No trains go to the island. Try the Ferry!'
		},
		{
			'id': 2,
			'title': 'Empire State Building',
			'image': 'NewYork-EmpireState.jpg',
			'url': 'empire-state-building'
			'body': '<p>The Empire State Building is a landmark that looks over New York City. The inside of the building holds antennas for radio and television networks.',
			'gmapLink': 'https://www.google.com/maps/d/u/0/viewer?gl=US&ie=UTF8&oe=UTF8&msa=0&mid=1qqg24F8Al_Uq2Bieu9cDHur_Cas&ll=40.748492%2C-73.985699&z=17',
			'stations': ['Enter a list of stations near the empire state building']
		},
		{
			'id': 3,
			'title': 'Madison Square Garden',
			'image': 'NewYork-MadisonSquareGarden.jpg',
			'url': 'madison-square-garden'
			'body': 'Madison Square Garden is a multipurpose stadium. It is used for hockey, boxing, concerts, and other events. It is an indoor arena.',
			'gmapLink': 'https://www.google.com/maps/d/u/0/viewer?source=embed&geocode&ie=UTF8&hq=madison%20square%20garden&hnear&oe=UTF8&msa=0&mid=1nxW50kSAW5br07FWO2aPBjM42vU&ll=40.746204129484845%2C-73.99023750000002&z=16',
			'stations': 'Enter a list of stations near madison square garden'
		},
		{
			'id': 4,
			'title': 'Liberty Park',
			'image': 'NewYork-LibertyPark.jpg',
			'url': 'liberty-park'
			'body': '<p>The Statue of Liberty is made of copper and sits on Ellis Island. She is an icon that represLiberty Park is a park in the World Trade Center.',
			'gmapLink': 'https://www.google.com/maps/d/u/0/viewer?gl=us&ptab=2&ie=UTF8&oe=UTF8&msa=0&mid=1zzP0aARpzx3GVhp-VqspM-Fpcmw&ll=38.451515000000015%2C-78.86990099999998&z=17',
			'stations': ['Enter a list of stations near wtc liberty park']
		},
		{
			'id': 5,
			'title': 'Museum of Art',
			'image': 'NewYork-MuseumOfArt.jpg',
			'url': 'museum-of-art'
			'body': '<p>The museum holds a lot of valuable art pieces. It is the largest art museum in the United States.',
			'gmapLink': 'https://www.google.com/maps/d/u/0/viewer?hl=en&ie=UTF8&msa=0&ll=40.78001300000004%2C-73.962075&spn=0.004891%2C0.00913&z=17&mid=1_ZIfxtkBKensYp7guvhjFMMnI8o',
			'stations': ['Enter a list of stations near museum of art']
		},		
		{
			'id': 6,
			'title': 'Times Square',
			'image': 'NewYork-TimesSquare.jpg',
			'url': 'times-square'
			'body': '<p>Times Square is a major commercial intersection, tourist destination, entertainment center, and neighborhood in the Midtown Manhattan',
			'gmapLink': 'https://www.google.com/maps/d/u/0/viewer?hl=en&ie=UTF8&msa=0&ll=40.758639637688084%2C-73.98797400000002&mid=1L1Q0la-nI5BtDHHdbUNkY18DjkM&z=15',
			'stations': ['Enter a list of stations near times square']
		},

	]

	return articles