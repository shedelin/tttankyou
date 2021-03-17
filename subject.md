# Back-End Remote Test

### Context

You've been asked to develop the new delivery system of a delivery company. 
They've already got a database, which can be found in the 'db' folder. 
In this folder, you'll find two files, one for the database structure, one for the data. 
The database is a Postgres DB. 
You'll need to write a REST API which comply to the database structure and provide some endpoints.

### Tasks

- You must write a REST API which will expose the following endpoints 
        <br />
    * Customers 
        * retrieve customers lists 
            * We must be able to filter the requst with customer fields
        * retrieve a customer from id
        * create a customer
        <br />
    * Drivers
        * Retrieve drivers list 
            * We must be able to filter request with driver fields
        * Retrieve a driver from id
        * Create a driver
    
        <br />
    * Zones 
        * Retrieve zones list.
        * Check if a position is in a list (lat / lng), must return the zone if in zone.
        * Check if an address is in zone, must return the zone if in zone. 
        * Create a new zones.
        
        <br />
    * Products
        * Retrieve products list 
            * We must be able to filter request with product fields
        * Retrive product from id 
        * Retrieve product prices history
        * Create a product
        * Add product price
        
        <br />
    * Deliveries 
        * Retrieve all deliveries (include any information you think is important to the delivery)
        * Retrieve deliveries filtered by
            * customer
            * zone
            * driver
            * date
        * Create a delivery (If the address given is not in zone, should fail)
        * Add product to a delivery
        * Set a specific privce for a product of a delivery (the price must be applied only on the delivery)
    
        <br />
- Implement tests
- **bonus** : Create an endpoint to make a simple delivery dispatch alogrithm, this endpoint should take two arguments : The day and the driver. 
With those information, you're asked to return a simple list of events which will represent the deliveries step by step of the driver on that day.
Your algorithm, should'nt take the deliveries dates into account, and should propose a new optimised organisation of deliveries.
<br />Exemple return:

```json
[{
    location: {
        address: "...",
        geo: {
            lat: ...,
            lng: ...
        }
    },
    step: 1,
    schedule_date: ...,
    order: {
        ...
    }
}, ...
]
```

### Requierments

- You can use the architecture you'd like. 
- You can use any language you'd like, but we would prefere python or go.
- You can use any of the framework or librairies that you think you'll need.
- You need to include a readme file which will explain how the application work and how it can be deployed or launch.