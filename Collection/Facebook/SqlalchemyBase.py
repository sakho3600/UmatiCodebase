
'''
Script    : Facebook Query
Created   : November 21, 2014
Author(s) : iHub Research
Version   : v1.0
License   : Apache License, Version 2.0
'''


#The purpose of this file is that sqlalchemy has a slightly annoying but also useful
#feature the table are inherited from a Base class that is generated by the function "declarative_base"
#it's a bit weird but means that the particular Base class is connected to it's inherited table so can easily do
#things like "create_all" tables inherited from it.
#Makes it slightly tricky to spread defs of tables across modules as you need to call the "declarative base" function
#to inherit the tables from.
#Answer is to put construction of class in this file then import via "from SqlalchemyBase import Base" in files
#where the defs for the tables are

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
