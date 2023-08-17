customer_table=[
  {
    "id": 1, 
    "first_name": "John", 
    "last_name": "Doe",
    "age": 35,
    "postal_code": "90210"
  },
  {  
    "id": 2,
    "first_name": "Jane",
    "last_name": "Smith", 
    "age": 27,
    "postal_code": "12345"
  },
  {
    "id": 3, 
    "first_name": "Bob",
    "last_name": "Jones",
    "age": 42,
    "postal_code": "55555"
  },
  {
    "id": 4,
    "first_name": "Sara", 
    "last_name": "Miller",
    "age": 29, 
    "postal_code": "13579"
  },
  {
    "id": 5,
    "first_name": "Mark",
    "last_name": "Davis",
    "age": 31,
    "postal_code": "02468"
  },
  {
    "id": 6,
    "first_name": "Laura",
    "last_name": "Wilson",
    "age": 24,
    "postal_code": "98765" 
  },
  {
    "id": 7,
    "first_name": "Steve",
    "last_name": "Moore",
    "age": 36,
    "postal_code": "11223"
  },
  {
    "id": 8,
    "first_name": "Michelle",
    "last_name": "Chen",
    "age": 22,
    "orders": [
        {
            "order_id": 1,
            "quantity": 1,
            "description": "Pack of 12 pencils"
        },
        {
            "order_id": 2,
            "quantity": 12,
            "description": "Markers"
        }
    ],
    "postal_code": "33215"
  },
  {
    "id": 9,
    "first_name": "David",
    "last_name": "Lee",
    "age": 29,
    "orders": [
        {
            "order_id": 11,
            "quantity": 12,
            "description": "Notebooks"
        },
        {
            "order_id": 21,
            "quantity": 120,
            "description": "Pens"
        }
    ],
    "postal_code": "99567"
  },
  {
    "id": 10,
    "first_name": "Jessica",
    "last_name": "Brown",
    "age": 18, 
    "postal_code": "43210"
  }
]

def list_customers(filter):        
    return customer_table

def customer_lookup(id):
    for customer in customer_table:
        if customer["id"] == int(id):
            return customer
        
    return None


