few_shots = [
    {'Question' : "How many extra extra large shirt are remaining in j.?",
     'SQLQuery' : "SELECT stock_quantity FROM clothing_items WHERE category = 'Shirt' AND brand = 'J.' AND size = 'XXL'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '90'},
    {'Question': "how much discount available for shirt in Khaadi?",
     'SQLQuery':"SELECT pct_discount FROM discounts JOIN clothing_items ON discounts.item_id = clothing_items.item_id WHERE clothing_items.category = 'Shirt' AND clothing_items.brand = 'Khaadi'",
     'SQLResult': "Result of the SQL query",
     'Answer': '35'},
    {'Question': "how much acesseries available in Khadi for large items",
     'SQLQuery': "SELECT stock_quantity FROM clothing_items WHERE category = 'Accessories' AND brand = 'Khaadi' AND size = 'L'",
     'SQLResult': "Result of the SQL query",
     'Answer': '86'} ,
     {'Question' : "If we have to sell all the J. shirts today with discounts applied. How much revenue our store will generate (post discounts)?" ,
      'SQLQuery': """select sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, item_id from clothing_items where brand = 'J.'
group by item_id) a left join discounts on a.item_id = discounts.item_id""",
      'SQLResult': "Result of the SQL query",
      'Answer' : '118043.46'},
    {'Question': "how much purple color items available for outfitters?",
     'SQLQuery' : "SELECT stock_quantity FROM clothing_items WHERE color = 'Purple' AND brand = 'Outfitters'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '38'
     }
]