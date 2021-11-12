import random
import csv

names = ["Alvin Carpenter","Lorna Jenkins","Nisha Vang","Ashlee Owens",
        "Rojin Sparrow","Madeeha Bellamy","Ewen Stott","Franco Crouch",
        "Jensen Conroy","Clarissa Churchill","Batman","Aron Parsons",
        "Tyron Goodman","Shahzaib Petty","Julius Colley","Calista Cummings",
        "Eiliyah West","Adem Wardle","Keaton Ferry","Salman Whitley",
        "Simran Dudley","Halle Sampson","Zander Spencer","Gurveer Lutz",
        "Hasnain Mendoza","Scarlette Mohammed","Nadeem Craft","Ajay Bryan",
        "Kiera Ridley","Otto Valenzuela","Tarik Corona","Ella-Rose Choi",
        "Roland Burns","Sheena Walls","Robert Horne","Eleasha Firth",
        "Gracie Hood","Albert Cross","Domonic Keller","Kenya Hartman",
        "Luna Crosby","Isabella-Rose Hawkins","Kathryn Lindsey","Karen Diaz",
        "Gianluca Walker","Ephraim Booth","Zayan Yang","Conal Taylor",
        "Jimmie Gallegos","Ritik Moses","Lois Wong","Sylvie Yoder",
        "Romana Wagner","Kelly Hodge","Romy Cohen","Renee Park",
        "Siraj Blevins","Lexi Hendricks","Mario Easton","Aoife Wynn",
        "Devon Lowry","Mathias Russo","Fionn Cochran","Ella-Grace Hollis",
        "Karis Lane","Huseyin Sargent","Charlene Myers","Leighton Bloggs",
        "Marilyn Burks","Alessio Day","Maisha Frost","Keri Rocha","Lillie Paterson",
        "Andre Matthews","Blair Torres","Roscoe Dunne","Larissa Kinney","Camron Rees",
        "Jagdeep Sims","Sandra Wickens","Soraya Bevan","Libbi Driscoll","Shanaya Bouvet",
        "Zaynab Markham","Sinead Holland","Dougie Whelan","Rylee Hinton","Federico Ray",
        "Fatima Goodwin","Amandeep Mclean","Eleri Garza","Heath Robson","Areebah Calhoun",
        "Nour Fox","Lillie-Mae O'Neill","Margot Reyna","Ibrahim Witt","Rukhsar Roman",
        "Frida Rayner","Keir Soto","Cody Buckley"]

    
sports = ["Archery","Badminton","Cricket","Bowling","Boxing",
        "Curling","Tennis","Skateboarding","Surfing","Hockey",
        "Figure skating","Yoga","Fencing","Fitness","Gymnastics",
        "Karate","Volleyball","Weightlifting","Basketball",
        "Baseball","Rugby","Wrestling","High jumping",
        "Hang gliding","Car racing","Cycling","Running",
        "Table tennis","Fishing","Judo","Climbing","Pool",
        "Shooting","Horse racing","Horseback riding","Golf","Soccer"]

genders = ['Male', 'Female', 'Non-binary']

f1 = open('members.csv','w', newline='\n')
writer = csv.writer(f1)

writer.writerow(["ID","Name","Sport","Gender","Age"])

for n in range(random.randint(500, 1000)):
    writer.writerow([n+1, random.choice(names), random.choice(sports),
                     random.choice(genders), random.randint(12, 86)])

f1.close()