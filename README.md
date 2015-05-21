# Scrapy-Crawler
####Web crawler using scrapy library

This crawler was done for a project of a Computer Science class at college called Tailored Studio Learning.
The project is about creating a software that generates a Top Ten list of songs heard at various radio stations of the same kind of music in Guatemala. It was divided into different stages; the first one consisted of extracting the data from three radio station's websites and loading it into a database that would then generate a list of the ten most listened songs.
We uploaded the various web crawlers that we did using the Scrapy library to extract the information we wanted from the following radio stations: 949 radio, atmosfera 96.5 y yosi sideral 90.1.


##Database Developement

We created a database using mySQL Workbench called Tailored with a table named music. This table has a primary key and the following columns: Song, Artist, and Album.

######To insert the information we used the following query:

LOAD DATA INFILE 'C:/Users/MariaInes/Downloads/yosifinal.csv'

INTO TABLE music

FIELDS TERMINATED BY ',' ENCLOSED BY '"'

LINES TERMINATED BY '\n'

IGNORE 1 ROWS

(Song,Artist,Album)
