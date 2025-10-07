# Ex.07 Restaurant Website
# Date:5.10.2025
# AIM:
To develop a static Restaurant website to display the food items and services provided by them.

# DESIGN STEPS:
## Step 1:
Requirement collection.

## Step 2:
Creating the layout using HTML and CSS.

## Step 3:
Updating the sample content.

## Step 4:
Choose the appropriate style and color scheme.

## Step 5:
Validate the layout in various browsers.

## Step 6:
Validate the HTML code.

## Step 7:
Publish the website in the given URL.

# PROGRAM:
```
rest.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurant website</title>
    <style>
        body{
            background-image: url("https://i.pinimg.com/736x/dd/64/c8/dd64c88e75b5a2f67dba7c7f20abb294.jpg");
            background-size:cover;
        }
        .details{
            display: flex;
            flex-direction: row;
            background-color: #a98467;
            margin: auto;
            align: center;
            padding-left: 20px;
            width:1000px;
            border-radius: 20px;
        }
        .details div{
            flex:1;

        }
        .details div{
            flex:1;
        }
        .details div{
            flex:1;
        }
        .details div{
            flex:1;
        }
        .food img{
            width:75%;
            height: 350px;
            border-radius: 20px;
        }
        .food{
            text-align: center;
            width: 950px;
            font-size: xx-large;
            color: wheat;
            text-shadow: 2px 2px 5px black;;
            font-family: brush script mt;
        }
        .container{
            display: flex;
            flex-direction: row;
            align:center;
            margin: auto;
            width: 75%;
            position: relative;
            top:250px;
            gap: 30px;
           
        }
        .menu{
            flex:1;
            text-align: justify;
            font-size: larger;
            color: #522102;
            background-color: #aec178aa;
            padding: 20px;
            border-radius: 20px;
            
        }
        .slot{
            flex:1;
            text-align: justify;
            font-size: larger;
            color: #522102;
            background-color: #aec178aa;
            padding: 20px;
            border-radius: 20px;
        }
        .hours{
            flex:1;
            text-align: justify;
            font-size: larger;
            color: #522102;
            background-color: #aec178aa;
            padding: 20px;
            border-radius: 20px;
        }


    </style>
</head>
<body >
    <header style="display: flex; flex-direction: row;font-family: old english text mt;text-align: center;font-size: xx-large;padding-left: 30%;color: #543804;">
        <img src="static\restlogoorg.png" style="width: 100px;">
        <p>WELCOME TO "ATE'O CLOCK"</p>
    </header>
    <div class="details">
        <div><a href="">HOME</a></div>
        <div><a href="{% url 'menu' %}">MENU</a></div>
        <div><a href="{% url 'admin'%}">ADMINISTRATION</a></div>
        <div><a href="{% url 'contact' %}">CONTACT US</a></div>
    </div>

    <div class="food">
        
        <img style="position: absolute;left: 200px" src="static\discountfood.jpg">
        
        <div>
            <p style="position: relative;top:100px;left: 250px;background-color: rgba(238, 126, 22, 0.273);">🥗 “Dine More, Save More – Up to <b>30% OFF</b> on combos.”
At Ate’O Clock, every meal is a feast for both your taste buds and your wallet. Come hungry, leave happy—with delicious combos at unbeatable prices!</p>
        </div>
    
    </div>

    <div class="container">
        <div class="menu"><center><p style="font-family: algerian;font-size: x-large;color: #6c584c;">OUR MENU</p>
            <img src="static\food.jpg" style="width: 250px;height: 280px;"></center>
            <p ><i>Our new menu features fresh seasonal ingredients, chef’s signature creations, and flavor-packed combos made to suit every mood. Whether you’re craving something spicy, cheesy, or sweet, you’ll find something that hits the spot. 🍽️✨</i></p>
            <a href="{% url 'menu' %}">Our new menu</a>
        </div>

        <div class="slot">
            <center><p style="font-family: algerian;font-size: x-large;color: #6c584c;">BOOK A TABLE</p>
                <img src="static\table.jpg" style="width: 250px;height: 280px;"></center>
                <p><i>Ready for a great meal? Book your table at Ate’O Clock and let us serve you the flavors you love — no waiting, just dining!</i></p>
                <a href=""> Book your table now</a>

        </div>

        <div class="hours">
            <center><p style="font-family: algerian;font-size: x-large;color: #6c584c;">OPENING HOURS</p>
                <img src="static\hours.jpg" style="width: 200px;height:300px;"></center>
                <p><i>
                    Whether it’s a quick lunch, a cozy dinner, or a weekend treat, our doors are open to serve fresh, flavorful meals and a warm dining experience every day.
                    <pre>    Mon–Fri: 11 AM – 11 PM 
    Sat–Sun: 10 AM – 12 AM.</pre>
                </i></p>
                
        </div>
        

    </div>
    

</body>
</html>

menu.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MENU</title>
    <style>
        body{
            background-image: url("https://i.pinimg.com/1200x/77/5e/cc/775ecc6890b3a66ce7d8223a630e3c35.jpg");
            background-size: 100%;
            
        }
        .menu{
            display: flex;
            flex-direction: row;
            gap: 40px;
            text-align: justify;
            position: relative;
            left: 70px;
            
            font-size: larger;
        }
        .STARTERS{
            background: linear-gradient(135deg, #ffcad4, #ffd580);
            padding: 20px;
            border-radius: 20px;
           box-shadow: 0 2px 9px #ffd700; 
        }
        .main{
            background: linear-gradient(135deg, #ff5f7e, #ffb07c);
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 2px 9px #ffd700; 
            
        }
        .bread{
            background: linear-gradient(135deg, #ffcad4, #ffd580);
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 2px 9px #ffd700; 
        }
        .desserts{
            background:linear-gradient(135deg, #ff5f7e, #ffb07c);
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 2px 9px #ffd700; 
        }
        .bev{
            background: linear-gradient(135deg, #ffcad4, #ffd580);
            padding: 20px;
            border-radius: 20px;box-shadow: 0 2px 9px #ffd700; 
        }
    </style>
</head>
<body>
    
    <header>

    <p style="font-family: old english text mt;font-size: 100px;text-align:center;background: linear-gradient(90deg, #b8860b, #ffd700, #fff8aa, #ffd700, #b8860b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow:
    0 0 2px #fff8aa,
    0 0 5px #ffd700,
    0 0 10px #ffdd00,
    0 0 15px #ffd700,
    0 0 20px #b8860b;
" >Menu</p>
    </header>
    <div class="menu">
        <div class="STARTERS">
            <p style="color: #3c096c; font-size: x-large;font-family: lucida handwriting;"><b>STARTERS</b></p>
            <p><i>Paneer Tikka — ₹220<br><br>
Chicken 65 — ₹230<br><br>
Veg Spring Rolls — ₹180<br><br>
Loaded Nachos — ₹200<br><br>
Tandoori Chicken (Half) — ₹270<br><br>
Peri Peri Fries — ₹160<br><br>
Garlic Bread with Cheese — ₹150<br><br>
</i></p>
        </div>

        <div class="main">
            <b><p style="color: #3c096c; font-size: x-large;font-family: lucida handwriting;">MAIN COURSE</p></b>
            <p><i>
Butter Chicken — ₹290<br><br>
Paneer Butter Masala — ₹250<br><br>
Mutton Rogan Josh — ₹350<br><br>
Dal Makhani — ₹200<br><br>
Kadai Paneer — ₹240<br><br>
Veg Biryani — ₹220<br><br>
Chicken Biryani — ₹260<br><br>
</i></p>
        </div>

        <div class="bread">
            <p style="color: #3c096c; font-size: x-large;font-family: lucida handwriting;"><b>INDIAN BREADS</b></p>
            <p><i>
                Butter Naan — ₹60<br><br>
Garlic Naan — ₹70<br><br>
Tandoori Roti — ₹40<br><br>
Stuffed Kulcha — ₹90<br><br>
            </i></p>
        </div>

        <div class="desserts">
            <p style="color: #3c096c; font-size: x-large;font-family: lucida handwriting;"><b>DESSERTS</b></p>
            <p><i>
                Gulab Jamun — ₹90<br><br>
Chocolate Lava Cake — ₹150<br><br>
Brownie with Ice Cream — ₹180<br><br>
Rasmalai — ₹110<br><br>
Blueberry Cheesecake — ₹200<br><br>
            </i></p>
        </div>

        <div class="bev">
            <p style="color: #3c096c; font-size: x-large;font-family: lucida handwriting;"><b>BEVERAGES</b></p>
            <p><i>
                Masala tea — ₹50<br><br>
Cold Coffee — ₹120<br><br>
Lemon Mojito — ₹110<br><br>
Iced Latte — ₹140<br><br>
Fresh Lime Soda — ₹90<br><br>
Sweet Lassi — ₹90<br><br>
            </i></p>
        </div>
    </div>
</body>
</html>

adminis.html
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADMINISTRATION</title>
    <style>
        body{
            background-image: url("https://i.pinimg.com/1200x/37/da/e1/37dae199e0eedf881892ecca9a9399ec.jpg");
            background-size: cover;
        }
        .container{
            display: flex;
            flex-direction: row;
            gap:50px;
            text-align: justify;
            color: bisque;
            font-size: larger;
        }
        .ceo{
            flex:1;
            background-color: rgba(128, 128, 128, 0.699);
            padding: 20px;
            border-radius: 20px;
        }
        .ceo img{
            width: 200px;
            padding-left: 150px;
            padding-top: none;
            
        }
        .chef{
            flex:1;
            background-color: rgba(128, 128, 128, 0.699);
            padding: 20px;
            border-radius: 20px;
        }
        .chef img{
            width: 225px;
             padding-left: 150px;
             
        }
        .manager{
            flex:1;
            background-color: rgba(128, 128, 128, 0.699);
            padding: 20px;
            border-radius: 20px;
        }
        .manager img{
            width: 275px;
            padding-left: 150px;
            padding-top: 40px;
            
            
        }
    </style>
</head>
<body>
    <p style="font-size: 50px;font-family: old english text mt;text-align: center;background: linear-gradient(90deg, #b8860b, #ffd700, #fff8aa, #ffd700, #b8860b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow:
    0 0 2px #fff8aa,
    0 0 5px #ffd700,
    0 0 10px #ffdd00,
    0 0 15px #ffd700,
    0 0 20px #b8860b;">Administration</p>
    <div class="container">
        <div class="ceo">
            <img src="{% static 'ceo.jpg' %}"><br>
            <p style="color: goldenrod;font-size: x-large;text-align: center;"><b>Arun Rajan, CEO</b></p>
            <p>At Ate’O Clock, the restaurant’s leadership and operations are guided by a team of dedicated professionals. Arun Rajan, our Chief Executive Officer, oversees the overall vision, strategy, and growth of the restaurant, ensuring that every department aligns with the mission and standards.</p>
        </div>

        <div class="chef">
            <img src="{% static 'chef.jpg' %}"><br><br>
            <p style="color: goldenrod;font-size: x-large;text-align: center;"><b>Meera Krishnan, Excutive Chef</b></p>
            <p>Meera Krishnan, our Executive Chef, leads the kitchen team, crafting innovative menus while maintaining consistent quality and presentation, as well as coordinating with suppliers and managing staff schedules.</p>
        </div>

        <div class="manager">
            <img src="{% static 'manager.jpg' %}"><br><br><br>
            <p style="color: goldenrod;font-size: x-large;text-align: center;"><b>Karthik Subramanian, Manager</b></p>
            <p>Karthik Subramanian, the Restaurant Manager, handles all front-of-house operations, ensuring seamless service, managing staff, and maintaining exceptional customer satisfaction.</p>
        </div>
    </div>
</body>
</html>

cont.html
<!DOCTYPE html>
{% load static%}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <style>
        body{
            background-image: url("https://i.pinimg.com/1200x/f6/c3/71/f6c37190925923a040d406802717b963.jpg");
            background-size: cover;
            color: bisque;
        }
    </style>
</head>
<body>
    
    <p style="font-family: old english text mt;font-size:40px; background: linear-gradient(90deg, #b8860b, #ffd700, #fff8aa, #ffd700, #b8860b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow:
    0 0 2px #fff8aa,
    0 0 5px #ffd700,
    0 0 10px #ffdd00,
    0 0 15px #ffd700,
    0 0 20px #b8860b;"> Contact Us:</p>
    We’d love to hear from you! Whether you’re planning a cozy dinner, a family celebration, or simply want to share your feedback, our team at Ate’O Clock is always here to help.<br><br>

📍 Address: 45, Food Street, T. Nagar, Chennai – 600017<br><br>
📞 Phone: +91 98765 43210<br><br>
📧 Email: hello@ateoclock.com<br><br>

🕒 Opening Hours: Mon–Fri: 11 AM – 11 PM <br>
    Sat–Sun: 10 AM – 12 AM.<br><br>

<p style="font-family: brush script mt;font-size: xx-large;color:#b8860b"><b>Have a special request or want to reserve a table? Just reach out to us—we’ll make sure your dining experience is nothing short of delightful.</b></p>
<img src="{% static 'restlogoorg.png' %}" style="width: 100px;position:relative;left:450px;bottom: 90px;">
<img src="{% static 'thank you.png' %}" style="width: 300px;position: relative; left: 500px;"
</body>
</html>

```
# OUTPUT:
![alt text](<Screenshot 2025-10-07 143034.png>)
![alt text](<Screenshot 2025-10-07 143047.png>)
![alt text](<Screenshot 2025-10-07 143146.png>)
![alt text](<Screenshot 2025-10-07 143246.png>)
![alt text](<Screenshot 2025-10-07 143309.png>)

# RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
