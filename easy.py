def main():
	letters = ["a", "b", "c", "d", "e", "f"]
	new_letter = ["q"]
	for letter in letters:
		for x in range(1,7):
			# print("self." + letter + str(x) + " = " + letter + str(x) + ";"),
			print('"' + letter+str(x)+'h' + '"' + ','),
			print('"' + letter+str(x)+'a' + '"' + ','),
			# print('request.form["' + letter + str(x) + '"],' ),
			# print('request.form["' + letter + str(x) + 'a' + '"],' ),

main()

#needed to export psql
#export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin
#export DATABASE_URL='postgres:///nachotorras'
#export SENDGRID_KEY='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'
#export SOCCER_API_KEY='dHtlYGeDAKgDIm4z6oEOzGzNN2uuYb2MrAeWkpYVokEeCbJEx4vfiOl6IsDc'


#DB 
#dev33n47ctqkem

#Game A1
France (home) 2 - 1 Romania (away)
UPDATE submission SET points = points + 1 WHERE a1h>a1a;
UPDATE submission SET points = points + 2 WHERE a1h=2 and a1a=1;
#Game A2
Albania (home) 0  - 1 Switzerland (away)
UPDATE submission SET points = points + 1 WHERE a2h<a2a;
UPDATE submission SET points = points + 2 WHERE a2h=0 and a2a=1;

#Game B1
Wales (home) 2 - 1 Slovakia (away)
UPDATE submission SET points = points + 1 WHERE b1h>b1a;
UPDATE submission SET points = points + 2 WHERE b1h=2 and b1a=1;
#Game B2
England (home) 1 - 1  Russia (away)
UPDATE submission SET points = points + 1 WHERE b2h=b2a;
UPDATE submission SET points = points + 2 WHERE b2h=1 and b2a=1;

#Game C1
Poland (home) 1 - 0  North Ireland (away)
UPDATE submission SET points = points + 1 WHERE c1h>c1a;
UPDATE submission SET points = points + 2 WHERE c1h=1 and c1a=0;
#Game C2
Germany (home) 2 - 0  Ukraine (away)
UPDATE submission SET points = points + 1 WHERE c2h>c2a;
UPDATE submission SET points = points + 2 WHERE c2h=2 and c2a=0;

#Game D1
Turkey (home) 0 - 1 Croatia (away)
UPDATE submission SET points = points + 1 WHERE d1h<d1a;
UPDATE submission SET points = points + 2 WHERE d1h=0 and d1a=1;
#Game D2
Spain (home) 1 - 0 Czech Republic (away)
UPDATE submission SET points = points + 1 WHERE d2h>d2a;
UPDATE submission SET points = points + 2 WHERE d2h=1 and d2a=0;

#Game E1
R. Ireland (home) 1 - 1 Sweden (away)
UPDATE submission SET points = points + 1 WHERE e1h=e1a;
UPDATE submission SET points = points + 2 WHERE e1h=1 and e1a=1;
#Game E2
Belgium (home) 0 - 1 Italy (away)
UPDATE submission SET points = points + 1 WHERE e2h<e2a;
UPDATE submission SET points = points + 2 WHERE e2h=0 and e2a=2;

#Game F1
Austria (home) 0 - 2 Hungary (away)
UPDATE submission SET points = points + 1 WHERE f1h<f1a;
UPDATE submission SET points = points + 2 WHERE f1h=0 and f1a=2;
#Game F2
Portugal (home) 1 - 1 Iceland (away)
UPDATE submission SET points = points + 1 WHERE f2h=f2a;
UPDATE submission SET points = points + 2 WHERE f2h=1 and f2a=1;

#Game A3
Romania (home) 1 - 1 Switzerland (away)
UPDATE submission SET points = points + 1 WHERE a3h=a3a;
UPDATE submission SET points = points + 2 WHERE a3h=1 and a3a=1;
#Game A4
France (home) 2 - 0 Albania (away)
UPDATE submission SET points = points + 1 WHERE a4h>a4a;
UPDATE submission SET points = points + 2 WHERE a4h=2 and a4a=0;

#Game B3
Russia (home) 1 - 2 Slovakia (away)
UPDATE submission SET points = points + 1 WHERE b3h<b3a;
UPDATE submission SET points = points + 2 WHERE b3h=1 and b3a=2;
#Game B4
England (home) 2 - 1 Wales (away)
UPDATE submission SET points = points + 1 WHERE b4h>b4a;
UPDATE submission SET points = points + 2 WHERE b4h=2 and b4a=1;

#Game C3
Ukraine (home) 0 - 2 Northern Ireland (away)
UPDATE submission SET points = points + 1 WHERE c3h<c3a;
UPDATE submission SET points = points + 2 WHERE c3h=0 and c3a=2;
#Game C4
Germany (home) 0 - 0 Poland (away)
UPDATE submission SET points = points + 1 WHERE c4h=c4a;
UPDATE submission SET points = points + 2 WHERE c4h=0 and c4a=0;

#Game D3
Czech (home) 2 - 2 Croatia (away)
UPDATE submission SET points = points + 1 WHERE d3h=d3a;
UPDATE submission SET points = points + 2 WHERE d3h=2 and d3a=2;
#Game D4
Spain (home) 3 - 0 Turkey (away)
UPDATE submission SET points = points + 1 WHERE d4h>d4a;
UPDATE submission SET points = points + 2 WHERE d4h=3 and d4a=0;

#Game E3
Italy (home) 1 - 0 Sweden (away)
UPDATE submission SET points = points + 1 WHERE e3h>e3a;
UPDATE submission SET points = points + 2 WHERE e3h=1 and e3a=0;
#Game E4
Belgium (home) 3 - 0 Ireland (away)
UPDATE submission SET points = points + 1 WHERE e4h>e4a;
UPDATE submission SET points = points + 2 WHERE e4h=3 and e4a=0;

#Game F3
Iceland (home) 1 - 1 Hungary (away)
UPDATE submission SET points = points + 1 WHERE f3h=f3a;
UPDATE submission SET points = points + 2 WHERE f3h=1 and f3a=1;
#Game F4
Portugal (home) 0 - 0 Austria (away)
UPDATE submission SET points = points + 1 WHERE f4h=f4a;
UPDATE submission SET points = points + 2 WHERE f4h=0 and f4a=0;

#Game A5
Switzerland (home) 0 - 0 France (away)
UPDATE submission SET points = points + 1 WHERE a5h=a5a;
UPDATE submission SET points = points + 2 WHERE a5h=0 and a5a=0;
#Game A6
Romania (home) 0 - 1 Albania (away)
UPDATE submission SET points = points + 1 WHERE a6h<a6a;
UPDATE submission SET points = points + 2 WHERE a6h=0 and a6a=1;
#GROUP A RESULTS
UPDATE submission SET points = points + 3 WHERE a1='France';
UPDATE submission SET points = points + 3 WHERE a2='Switzerland';
UPDATE submission SET points = points + 2 WHERE a1='Switzerland';
UPDATE submission SET points = points + 2 WHERE a2='France';
UPDATE submission SET points = points + 2 WHERE third2='France' or third3='France';
UPDATE submission SET points = points + 2 WHERE third2='Switzerland' or third3='Switzerland';

#Game B5
Slovakia (home) 0 - 0 England (away)
UPDATE submission SET points = points + 1 WHERE b5h=b5a;
UPDATE submission SET points = points + 2 WHERE b5h=0 and b5a=0;
#Game B6
Russia (home) 0 - 3 Wales (away)
UPDATE submission SET points = points + 1 WHERE b6h<b6a;
UPDATE submission SET points = points + 2 WHERE b6h=0 and b6a=3;
#GROUP B RESULTS
UPDATE submission SET points = points + 3 WHERE b1='Wales';
UPDATE submission SET points = points + 3 WHERE b2='England';
UPDATE submission SET points = points + 2 WHERE b1='England';
UPDATE submission SET points = points + 2 WHERE b2='Wales';
UPDATE submission SET points = points + 2 WHERE third1='Wales' or third3='Wales';
UPDATE submission SET points = points + 2 WHERE third1='England' or third3='England';

#Game C5
N Ireland (home) 0 - 1 Germany (away)
UPDATE submission SET points = points + 1 WHERE c5h<c5a;
UPDATE submission SET points = points + 2 WHERE c5h=0 and c5a=1;
#Game C6
Ukraine (home) 0 - 1 Poland (away)
UPDATE submission SET points = points + 1 WHERE c6h<c6a;
UPDATE submission SET points = points + 2 WHERE c6h=0 and c6a=1;
#GROUP C RESULTS
UPDATE submission SET points = points + 3 WHERE c1='Germany';
UPDATE submission SET points = points + 3 WHERE c2='Poland';
UPDATE submission SET points = points + 2 WHERE c1='Poland';
UPDATE submission SET points = points + 2 WHERE c2='Germany';
UPDATE submission SET points = points + 2 WHERE third2='Germany' or third4='Germany';
UPDATE submission SET points = points + 2 WHERE third2='Poland' or third4='Poland';

#Game D5
Croatia (home) 2 - 1 Spain (away)
UPDATE submission SET points = points + 1 WHERE d5h>d5a;
UPDATE submission SET points = points + 2 WHERE d5h=2 and d5a=1;
#Game D6
Czech Republic (home) 0 - 2 Turkey (away)
UPDATE submission SET points = points + 1 WHERE d6h<d6a;
UPDATE submission SET points = points + 2 WHERE d6h=0 and d6a=2;
#GROUP C RESULTS
UPDATE submission SET points = points + 3 WHERE d1='Croatia';
UPDATE submission SET points = points + 3 WHERE d2='Spain';
UPDATE submission SET points = points + 2 WHERE d1='Spain';
UPDATE submission SET points = points + 2 WHERE d2='Croatia';
UPDATE submission SET points = points + 2 WHERE third2='Croatia' or third4='Croatia';
UPDATE submission SET points = points + 2 WHERE third2='Spain' or third4='Spain';

#Game E5
Sweden (home) 0 - 1 Beglium (away)
UPDATE submission SET points = points + 1 WHERE e5h<e5a;
UPDATE submission SET points = points + 2 WHERE e5h=0 and e5a=1;
#Game E6
Italy (home) 0 - 1 Republic of Ireland (away)
UPDATE submission SET points = points + 1 WHERE e6h<e6a;
UPDATE submission SET points = points + 2 WHERE e6h=0 and e6a=1;
#GROUP C RESULTS
UPDATE submission SET points = points + 3 WHERE e1='Italy';
UPDATE submission SET points = points + 3 WHERE e2='Belgium';
UPDATE submission SET points = points + 2 WHERE e1='Belgium';
UPDATE submission SET points = points + 2 WHERE e2='Italy';
UPDATE submission SET points = points + 2 WHERE third1='Italy' or third4='Italy';
UPDATE submission SET points = points + 2 WHERE third1='Belgium' or third4='Belgium';

#Game F5
Hungary (home) 3 - 3 Portugal (away)
UPDATE submission SET points = points + 1 WHERE f5h=f5a;
UPDATE submission SET points = points + 2 WHERE f5h=3 and f5a=3;
#Game F6
Iceland (home) 2 - 1 Austria (away)
UPDATE submission SET points = points + 1 WHERE f6h>f6a;
UPDATE submission SET points = points + 2 WHERE f6h=2 and f6a=1;
#GROUP F RESULTS
UPDATE submission SET points = points + 3 WHERE f1='Hungary';
UPDATE submission SET points = points + 3 WHERE f2='Iceland';
UPDATE submission SET points = points + 2 WHERE f1='Iceland';
UPDATE submission SET points = points + 2 WHERE f2='Hungary';
UPDATE submission SET points = points + 2 WHERE third1='Hungary' or third3='Hungary';
UPDATE submission SET points = points + 2 WHERE third1='Iceland' or third3='Iceland';

#Third Place
UPDATE submission SET points = points + 3 WHERE third1='Slovakia' or third3='Slovakia';
UPDATE submission SET points = points + 2 WHERE b1='Slovakia' or b2='Slovakia';

UPDATE submission SET points = points + 3 WHERE third1='Republic of Ireland' or third4='Republic of Ireland';
UPDATE submission SET points = points + 2 WHERE e1='Republic of Ireland' or e2='Republic of Ireland';

UPDATE submission SET points = points + 3 WHERE third1='Portugal' or third3='Portugal';
UPDATE submission SET points = points + 2 WHERE f1='Portugal' or f2='Portugal';

UPDATE submission SET points = points + 3 WHERE third2='Northern Ireland' or third4='Northern Ireland';
UPDATE submission SET points = points + 2 WHERE c1='Northern Ireland' or c2='Northern Ireland';

#Quarters
UPDATE submission SET points = points + 4 WHERE q1='Poland' or q2='Poland' or q3='Poland' or q4='Poland' or q5='Poland' or q6='Poland' or q7='Poland' or q8='Poland';
UPDATE submission SET points = points + 4 WHERE q1='Wales' or q2='Wales' or q3='Wales' or q4='Wales' or q5='Wales' or q6='Wales' or q7='Wales' or q8='Wales';
UPDATE submission SET points = points + 4 WHERE q1='Portugal' or q2='Portugal' or q3='Portugal' or q4='Portugal' or q5='Portugal' or q6='Portugal' or q7='Portugal' or q8='Portugal';
UPDATE submission SET points = points + 4 WHERE q1='France' or q2='France' or q3='France' or q4='France' or q5='France' or q6='France' or q7='France' or q8='France';
UPDATE submission SET points = points + 4 WHERE q1='Germany' or q2='Germany' or q3='Germany' or q4='Germany' or q5='Germany' or q6='Germany' or q7='Germany' or q8='Germany';
UPDATE submission SET points = points + 4 WHERE q1='Belgium' or q2='Belgium' or q3='Belgium' or q4='Belgium' or q5='Belgium' or q6='Belgium' or q7='Belgium' or q8='Belgium';
UPDATE submission SET points = points + 4 WHERE q1='Italy' or q2='Italy' or q3='Italy' or q4='Italy' or q5='Italy' or q6='Italy' or q7='Italy' or q8='Italy';
UPDATE submission SET points = points + 4 WHERE q1='Iceland' or q2='Iceland' or q3='Iceland' or q4='Iceland' or q5='Iceland' or q6='Iceland' or q7='Iceland' or q8='Iceland';

UPDATE submission SET points = points + 6 WHERE semi1='Portugal' or semi2='Portugal' or semi3='Portugal' or semi4='Portugal';
UPDATE submission SET points = points + 6 WHERE semi1='Wales' or semi2='Wales' or semi3='Wales' or semi4='Wales';
UPDATE submission SET points = points + 6 WHERE semi1='Germany' or semi2='Germany' or semi3='Germany' or semi4='Germany';
UPDATE submission SET points = points + 6 WHERE semi1='France' or semi2='France' or semi3='France' or semi4='France';

UPDATE submission SET points = points + 10 WHERE fin1='Portugal' or fin2='Portugal';
UPDATE submission SET points = points + 10 WHERE fin1='France' or fin2='France';

UPDATE submission SET points = points + 25 WHERE champion='Portugal';
UPDATE submission SET points = points + 10 WHERE top_scorer='Antoine Griezmann';



SELECT first_name, points from submission WHERE q1='Northern Ireland' or q2='Northern Ireland' or q3='Northern Ireland' or q4='Northern Ireland' or q5='Northern Ireland' or q6='Northern Ireland' or q7='Northern Ireland' or q8='Northern Ireland';
