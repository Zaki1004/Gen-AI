from pathlib import Path
import sqlite3

import init_db

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "coffee.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ==========================
# Categories
# ==========================

categories = [
    ("Coffee", "Coffee Based Drinks"),
    ("Non Coffee", "Non Coffee Drinks"),
    ("Snack", "Light Meals"),
    ("Heavy Meal", "Main Course")
]

cursor.executemany("""
INSERT OR IGNORE INTO categories
(name, description)
VALUES (?, ?)
""", categories)

# ==========================
# Menu Items
# ==========================

coffee_menu = [

("Americano",1,25000,4.5,100,5,"High","Low","Hot","assets/americano.jpg","Espresso dengan air panas",1),

("Espresso",1,20000,4.7,100,3,"High","Low","Hot","assets/espresso.jpg","Single shot espresso",1),

("Double Espresso",1,25000,4.8,100,5,"Very High","Low","Hot","assets/double_espresso.jpg","Double shot espresso",0),

("Cappuccino",1,30000,4.8,100,120,"Medium","Medium","Hot","assets/cappuccino.jpg","Espresso dengan milk foam",1),

("Cafe Latte",1,32000,4.7,100,150,"Medium","Medium","Hot","assets/cafe_latte.jpg","Latte klasik",1),

("Caramel Latte",1,35000,4.9,100,180,"Medium","High","Cold","assets/caramel_latte.jpg","Latte dengan caramel",1),

("Vanilla Latte",1,35000,4.8,100,175,"Medium","High","Hot","assets/vanilla_latte.jpg","Latte vanilla",1),

("Hazelnut Latte",1,36000,4.7,100,180,"Medium","High","Hot","assets/hazelnut_latte.jpg","Latte hazelnut",0),

("Mocha",1,37000,4.9,100,210,"Medium","High","Hot","assets/mocha.jpg","Kopi dan coklat",1),

("White Mocha",1,39000,4.8,100,220,"Medium","High","Hot","assets/white_mocha.jpg","Mocha putih",0),

("Flat White",1,34000,4.6,100,130,"Medium","Low","Hot","assets/flat_white.jpg","Flat White Australia",1),

("Cold Brew",1,33000,4.8,100,10,"Medium","Low","Cold","assets/cold_brew.jpg","Ekstraksi dingin",1),

("Nitro Cold Brew",1,40000,4.7,100,15,"Medium","Low","Cold","assets/nitro.jpg","Cold brew nitrogen",0),

("Affogato",1,38000,4.9,100,250,"Medium","Medium","Cold","assets/affogato.jpg","Espresso dan es krim",1),

("Macchiato",1,29000,4.5,100,80,"Medium","Low","Hot","assets/macchiato.jpg","Espresso dengan foam",0),

("Piccolo Latte",1,30000,4.6,100,90,"Medium","Low","Hot","assets/piccolo.jpg","Mini latte",0),

("Irish Coffee",1,45000,4.7,100,180,"High","Medium","Hot","assets/irish.jpg","Kopi khas irlandia",0),

("Spanish Latte",1,39000,4.8,100,210,"Medium","High","Cold","assets/spanish_latte.jpg","Latte susu kental",1),

("Salted Caramel Latte",1,41000,4.8,100,220,"Medium","High","Cold","assets/salted_caramel.jpg","Latte caramel asin",1),

("Butterscotch Latte",1,42000,4.7,100,230,"Medium","High","Hot","assets/butterscotch.jpg","Latte butterscotch",0)

]

non_coffee_menu = [

("Matcha Latte",2,32000,4.6,100,160,"Low","Medium","Cold","assets/matcha.jpg","Matcha premium",1),

("Chocolate",2,30000,4.7,100,200,"None","High","Hot","assets/chocolate.jpg","Chocolate drink",1),

("Red Velvet",2,32000,4.8,100,210,"None","High","Cold","assets/redvelvet.jpg","Red Velvet Latte",1),

("Thai Tea",2,28000,4.7,100,190,"Low","High","Cold","assets/thaitea.jpg","Thai Tea Original",1),

("Green Tea Latte",2,31000,4.5,100,170,"Low","Medium","Hot","assets/green_tea.jpg","Green Tea Latte",0),

("Taro Latte",2,33000,4.8,100,230,"None","High","Cold","assets/taro.jpg","Taro Latte",1),

("Milk Tea",2,29000,4.6,100,180,"Low","Medium","Cold","assets/milktea.jpg","Milk Tea",0),

("Cookies Cream",2,35000,4.9,100,250,"None","High","Cold","assets/cookies.jpg","Cookies and Cream",1),

("Lemon Tea",2,25000,4.5,100,90,"None","Medium","Cold","assets/lemontea.jpg","Lemon Tea",0),

("Peach Tea",2,28000,4.5,100,100,"None","Medium","Cold","assets/peachtea.jpg","Peach Tea",0),

("Strawberry Milk",2,33000,4.7,100,220,"None","High","Cold","assets/strawberry.jpg","Strawberry Milk",1),

("Mango Smoothie",2,36000,4.8,100,230,"None","High","Cold","assets/mango.jpg","Mango Smoothie",1),

("Avocado Smoothie",2,37000,4.8,100,250,"None","Medium","Cold","assets/avocado.jpg","Avocado Smoothie",1),

("Lychee Tea",2,29000,4.5,100,120,"None","Medium","Cold","assets/lychee.jpg","Lychee Tea",0),

("Mineral Water",2,10000,4.0,100,0,"None","None","Cold","assets/water.jpg","Air Mineral",0),

("Sparkling Water",2,18000,4.1,100,0,"None","None","Cold","assets/sparkling.jpg","Air Soda",0),

("Orange Juice",2,30000,4.6,100,140,"None","Medium","Cold","assets/orange.jpg","Jus Jeruk",1),

("Apple Juice",2,30000,4.6,100,150,"None","Medium","Cold","assets/apple.jpg","Jus Apel",0),

("Yakult Strawberry",2,32000,4.7,100,180,"None","High","Cold","assets/yakult.jpg","Yakult Strawberry",1),

("Blue Ocean",2,35000,4.8,100,210,"None","High","Cold","assets/blue_ocean.jpg","Mocktail Blue Ocean",1)

]

snack_menu = [

("Croissant",3,18000,4.5,100,250,"","","","assets/croissant.jpg","Croissant butter",1),

("French Fries",3,20000,4.3,100,320,"","","","assets/fries.jpg","Kentang goreng",0),

("Onion Ring",3,22000,4.4,100,280,"","","","assets/onion.jpg","Onion Ring",0),

("Garlic Bread",3,18000,4.5,100,200,"","","","assets/garlic.jpg","Garlic Bread",0),

("Cheese Stick",3,22000,4.7,100,300,"","","","assets/cheese_stick.jpg","Cheese Stick",1),

("Waffle",3,25000,4.8,100,350,"","","","assets/waffle.jpg","Belgian Waffle",1),

("Donut",3,15000,4.3,100,180,"","","","assets/donut.jpg","Donut Gula",0),

("Brownies",3,24000,4.8,100,320,"","","","assets/brownies.jpg","Brownies Coklat",1),

("Muffin",3,22000,4.5,100,250,"","","","assets/muffin.jpg","Blueberry Muffin",0),

("Churros",3,25000,4.8,100,290,"","","","assets/churros.jpg","Churros Cinnamon",1),

("Banana Bread",3,23000,4.5,100,260,"","","","assets/banana.jpg","Banana Bread",0),

("Toast",3,18000,4.2,100,210,"","","","assets/toast.jpg","Toast Butter",0),

("Chicken Nugget",3,24000,4.6,100,300,"","","","assets/nugget.jpg","Chicken Nugget",1),

("Potato Wedges",3,23000,4.5,100,280,"","","","assets/wedges.jpg","Potato Wedges",0),

("Chicken Wings",3,30000,4.8,100,400,"","","","assets/wings.jpg","Chicken Wings",1),

("Nachos",3,28000,4.6,100,350,"","","","assets/nachos.jpg","Nachos Cheese",1),

("Mini Pizza",3,32000,4.8,100,420,"","","","assets/pizza.jpg","Mini Pizza",1),

("Sosis Bakar",3,20000,4.4,100,260,"","","","assets/sosis.jpg","Sosis Bakar",0),

("Dimsum",3,25000,4.7,100,240,"","","","assets/dimsum.jpg","Dimsum Ayam",1),

("Spring Roll",3,22000,4.5,100,230,"","","","assets/springroll.jpg","Spring Roll",0)

]

heavy_meal_menu = [

("Nasi Goreng",4,35000,4.7,100,550,"","","","assets/nasgor.jpg","Nasi Goreng Spesial",1),

("Mie Goreng",4,34000,4.6,100,530,"","","","assets/miegoreng.jpg","Mie Goreng Jawa",1),

("Chicken Katsu",4,45000,4.8,100,650,"","","","assets/katsu.jpg","Chicken Katsu",1),

("Chicken Steak",4,50000,4.8,100,700,"","","","assets/steak.jpg","Chicken Steak",1),

("Beef Burger",4,48000,4.7,100,650,"","","","assets/beefburger.jpg","Beef Burger",1),

("Chicken Burger",4,42000,4.6,100,600,"","","","assets/chickenburger.jpg","Chicken Burger",0),

("Fish and Chips",4,47000,4.7,100,650,"","","","assets/fishchips.jpg","Fish and Chips",1),

("Spaghetti Carbonara",4,48000,4.8,100,700,"","","","assets/carbonara.jpg","Carbonara",1),

("Spaghetti Bolognese",4,46000,4.7,100,680,"","","","assets/bolognese.jpg","Bolognese",1),

("Rice Bowl Teriyaki",4,40000,4.6,100,580,"","","","assets/teriyaki.jpg","Rice Bowl",1),

("Rice Bowl Sambal Matah",4,42000,4.7,100,600,"","","","assets/matah.jpg","Rice Bowl Matah",0),

("Ayam Geprek",4,35000,4.8,100,620,"","","","assets/geprek.jpg","Ayam Geprek",1),

("Ayam Bakar",4,42000,4.6,100,610,"","","","assets/ayambakar.jpg","Ayam Bakar",0),

("Beef Teriyaki",4,55000,4.8,100,700,"","","","assets/beefteriyaki.jpg","Beef Teriyaki",1),

("Chicken Curry",4,45000,4.6,100,650,"","","","assets/curry.jpg","Chicken Curry",0),

("Sop Buntut",4,65000,4.9,100,750,"","","","assets/sopbuntut.jpg","Sop Buntut",1),

("Rawon",4,55000,4.8,100,680,"","","","assets/rawon.jpg","Rawon",0),

("Chicken Rice",4,38000,4.5,100,550,"","","","assets/chickenrice.jpg","Chicken Rice",0),

("Fried Rice Seafood",4,45000,4.7,100,650,"","","","assets/seafoodrice.jpg","Nasi Goreng Seafood",1),

("Beef Blackpepper",4,60000,4.9,100,720,"","","","assets/blackpepper.jpg","Beef Blackpepper",1)

]

menu_items = (
    coffee_menu +
    non_coffee_menu +
    snack_menu +
    heavy_meal_menu
)

cursor.executemany("""
INSERT INTO menu_items (
name,
category_id,
price,
rating,
stock,
calories,
caffeine_level,
sweetness_level,
serving_type,
image_path,
description,
is_recommended
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", menu_items)

# ==========================
# Popularity
# ==========================

popularity = [
(1, 150),
(2, 220),
(3, 300),
(4, 180),
(5, 90),
(6, 75),
(7, 120)
]

cursor.executemany("""
INSERT INTO menu_popularity (
menu_id,
total_order
)
VALUES (?, ?)
""", popularity)

conn.commit()
conn.close()

print("Seed data berhasil dimasukkan")