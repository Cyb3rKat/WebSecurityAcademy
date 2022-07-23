#Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data


 This lab contains an SQL injection vulnerability in the **product category** filter. When the user selects a category, the application carries out an SQL query like the following: 


 > SELECT * FROM products WHERE category = 'Gifts' AND released = 1

  To solve the lab, perform an SQL injection attack that causes the application to display details of all products in any category, both released and unreleased.




Analysis:
 
 - SELECT * FROM products where catergory='PETS' and released = 1

 we need to make it so that released = 1 is not taken into affect so we can use the OR operator to change the query and add -- to comment out the rest of the query.


> SELECT * FROM products  where category='' or 1=1--;' and released=1

so our payload will be:
> ' OR 1=1--

as 1 will always equal 1 we will get all the products from all categories no matter if they are released or not. 
 



## even though we are not using any additional packages in the first few projects its always good to practice the standards so i will be building a virtual enviroment for each lab script 