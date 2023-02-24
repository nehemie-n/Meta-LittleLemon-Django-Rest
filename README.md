<!-- Output copied to clipboard! -->

<!-----

Yay, no errors, warnings, or alerts!

Conversion time: 1.189 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Fri Feb 24 2023 05:15:31 GMT-0800 (PST)
* Source doc: LittleLemon API
* Tables are currently converted to HTML tables.
----->



# **About**

## **Run**

    cd LittleLemon

    pipenv shell

    pipenv install 

    python manage.py makemigrations 

    python manage.py migrate

    python manage.py runserver

## **Scope**

Created a fully functioning API project for the Little Lemon restaurant so that the client application developers can use the APIs to develop web and mobile applications. People with different roles will be able to browse, add and edit menu items, place orders, browse orders, assign delivery crew to orders and finally deliver the orders.

The next section will walk you through the required endpoints with an authorization level and other helpful notes. Your task is to create these endpoints by following the instructions.


## **Structure**

Created one single Django app called LittleLemonAPI and implement all API endpoints in it. Use pipenv to manage the dependencies in the virtual environment. Review the video about[ Creating a Django Project using pipenv.](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/sn2Ez/video-subtitles)


## **Function or class-based views**

Used class-based views or both in this project. Follow the proper API naming convention throughout the project. Review the video about[ Function- and class-based views](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/4BASB/video-subtitles) as well as the video about[ Naming conventions](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/1jSCM/video-subtitles).


## **User groups**

Created the following two user groups and then create some random users and assign them to these groups from the Django admin panel.

* Manager
* Delivery crew

Users not assigned to a group will be considered customers. Review the video about[ User roles](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/12F4H/video-subtitles).


## **Error check and proper status codes**

Displayed error messages with appropriate HTTP status codes for specific errors. These include when someone requests a non-existing item, makes unauthorized API requests, or sends invalid data in a **<code>POST</code></strong>, <strong><code>PUT</code></strong> or <strong><code>PATCH</code></strong> request. Here is a full list.


<table>
  <tr>
   <td><strong>HTTP Status code</strong>
   </td>
   <td><strong>Reason</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>200 - Ok</code></strong>
   </td>
   <td>For all successful <strong><code>GET</code></strong>, <strong><code>PUT</code></strong>, <strong><code>PATCH</code></strong> and <strong><code>DELETE </code></strong>calls
   </td>
  </tr>
  <tr>
   <td><strong><code>201 - Created</code></strong>
   </td>
   <td>For all successful <strong><code>POST</code></strong> requests
   </td>
  </tr>
  <tr>
   <td><strong><code>403 - Unauthorized</code></strong>
   </td>
   <td>If authorization fails for the current user token
   </td>
  </tr>
  <tr>
   <td><strong><code>401 – Forbidden</code></strong>
   </td>
   <td>If user authentication fails
   </td>
  </tr>
  <tr>
   <td><strong><code>400 – Bad request</code></strong>
   </td>
   <td>If validation fails for <strong><code>POST</code></strong>, <strong><code>PUT</code></strong>, <strong><code>PATCH</code></strong> and <strong><code>DELETE</code></strong> calls
   </td>
  </tr>
  <tr>
   <td><strong><code>404 – Not found</code></strong>
   </td>
   <td>If the request was made for a non-existing resource
   </td>
  </tr>
</table>



## **API endpoints**

Here are all the required API routes for this project grouped into several categories.


### **User registration and token generation endpoints**

Used Djoser in the project to automatically create the following endpoints and functionalities for you.


<table>
  <tr>
   <td><strong>Endpoint</strong>
   </td>
   <td><strong>Role</strong>
   </td>
   <td><strong>Method</strong>
   </td>
   <td><strong>Purpose</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/users</code></strong>
   </td>
   <td>No role required
   </td>
   <td><strong><code>POST</code></strong>
   </td>
   <td>Creates a new user with name, email and password
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/users/users/me/</code></strong>
 
   </td>
   <td>Anyone with a valid user token
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Displays only the current user
   </td>
  </tr>
  <tr>
   <td><strong><code>/token/login/</code></strong>
   </td>
   <td>Anyone with a valid username and password
   </td>
   <td><strong><code>POST</code></strong>
   </td>
   <td>Generates access tokens that can be used in other API calls in this project
   </td>
  </tr>
</table>


When you include Djoser endpoints, Djoser will create other useful endpoints as discussed in the[ Introduction to Djoser library for better authentication](https://www.coursera.org/learn/apis/lecture/bldmJ/introduction-to-djoser-library-for-better-authentication) video.


## ** Menu-items endpoints**


<table>
  <tr>
   <td><strong>Endpoint</strong>
   </td>
   <td><strong>Role</strong>
   </td>
   <td><strong>Method</strong>
   </td>
   <td><strong>Purpose</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/menu-items</code></strong>
   </td>
   <td>Customer, delivery crew
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Lists all menu items. Return a <strong><code>200 – Ok</code></strong> HTTP status code
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/menu-items</code></strong>
   </td>
   <td>Customer, delivery crew
<p>
 
   </td>
   <td><strong><code>POST</code></strong>, <strong><code>PUT</code></strong>, <strong><code>PATCH</code></strong>, <strong><code>DELETE</code></strong>
   </td>
   <td>Denies access and returns <strong><code>403 – Unauthorized</code></strong> HTTP status code
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/menu-items/{menuItem}</code></strong>
   </td>
   <td>Customer, delivery crew
<p>
 
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Lists single menu item
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/menu-items/{menuItem}</code></strong>
   </td>
   <td>Customer, delivery crew
   </td>
   <td><strong><code>POST</code></strong>, <strong><code>PUT</code></strong>, <strong><code>PATCH</code></strong>, <strong><code>DELETE</code></strong>
   </td>
   <td>Returns <strong><code>403 - Unauthorized</code></strong>
   </td>
  </tr>
  <tr>
   <td> 
   </td>
   <td> 
   </td>
   <td> 
   </td>
   <td> 
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/menu-items</code></strong>
   </td>
   <td>Manager
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Lists all menu items
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/menu-items</code></strong>
   </td>
   <td>Manager
   </td>
   <td><strong><code>POST</code></strong>
   </td>
   <td>Creates a new menu item and returns <strong><code>201 - Created</code></strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/menu-items/{menuItem}</code></strong>
   </td>
   <td>Manager
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Lists single menu item
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/menu-items/{menuItem}</code></strong>
   </td>
   <td>Manager
   </td>
   <td><strong><code>PUT</code></strong>, <strong><code>PATCH</code></strong>
   </td>
   <td>Updates single menu item
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/menu-items/{menuItem}</code></strong>
   </td>
   <td>Manager
   </td>
   <td><strong><code>DELETE</code></strong>
   </td>
   <td>Deletes menu item
   </td>
  </tr>
</table>



## **User group management endpoints**


<table>
  <tr>
   <td><strong>Endpoint</strong>
   </td>
   <td><strong>Role</strong>
   </td>
   <td><strong>Method</strong>
   </td>
   <td><strong>Purpose</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/groups/manager/users</code></strong>
   </td>
   <td>Manager
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Returns all managers
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/groups/manager/users</code></strong>
 
   </td>
   <td>Manager
   </td>
   <td><strong><code>POST</code></strong>
   </td>
   <td>Assigns the user in the payload to the manager group and returns <strong><code>201-Created</code></strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/groups/manager/users/{userId}</code></strong>
   </td>
   <td>Manager
   </td>
   <td><strong><code>DELETE</code></strong>
   </td>
   <td>Removes this particular user from the manager group and returns <strong><code>200 – Success</code></strong> if everything is okay.
If the user is not found, returns <strong><code>404 – Not found</code></strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/groups/delivery-crew/users</code></strong>
   </td>
   <td>Manager
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Returns all delivery crew
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/groups/delivery-crew/users</code></strong>
 
   </td>
   <td>Manager
   </td>
   <td><strong><code>POST</code></strong>
   </td>
   <td>Assigns the user in the payload to delivery crew group and returns <strong><code>201-Created</code></strong> HTTP
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/groups/delivery-crew/users/{userId}</code></strong>
   </td>
   <td>Manager
   </td>
   <td><strong><code>DELETE</code></strong>
   </td>
   <td>Removes this user from the manager group and returns <strong><code>200 – Success</code></strong> if everything is okay.
If the user is not found, returns  <strong><code>404 – Not found</code></strong>
   </td>
  </tr>
</table>



## **Cart management endpoints**


<table>
  <tr>
   <td><strong>Endpoint</strong>
   </td>
   <td><strong>Role</strong>
   </td>
   <td><strong>Method</strong>
   </td>
   <td><strong>Purpose</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/cart/menu-items</code></strong>
   </td>
   <td>Customer
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Returns current items in the cart for the current user token
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/cart/menu-items</code></strong>
 
   </td>
   <td>Customer
<p>
 
   </td>
   <td><strong><code>POST</code></strong>
   </td>
   <td>Adds the menu item to the cart. Sets the authenticated user as the user id for these cart items
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/cart/menu-items</code></strong>
 
   </td>
   <td>Customer
<p>
 
   </td>
   <td><strong><code>DELETE</code></strong>
   </td>
   <td>Deletes all menu items created by the current user token
   </td>
  </tr>
</table>



## **Order management endpoints**


<table>
  <tr>
   <td><strong>Endpoint</strong>
   </td>
   <td><strong>Role</strong>
   </td>
   <td><strong>Method</strong>
   </td>
   <td><strong>Purpose</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/orders</code></strong>
   </td>
   <td>Customer
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Returns all orders with order items created by this user
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/orders</code></strong>
 
   </td>
   <td>Customer
<p>
 
   </td>
   <td><strong><code>POST</code></strong>
   </td>
   <td>Creates a new order item for the current user. Gets current cart items from the cart endpoints and adds those items to the order items table. Then deletes all items from the cart for this user.
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/orders/{orderId}</code></strong>
 
   </td>
   <td>Customer
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Returns all items for this order id. If the order ID doesn’t belong to the current user, it displays an appropriate HTTP error status code.
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/orders</code></strong>
   </td>
   <td>Manager
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Returns all orders with order items by all users
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/orders/{orderId}</code></strong>
 
   </td>
   <td>Customer
<p>
 
   </td>
   <td><strong><code>PUT</code></strong>, <strong><code>PATCH</code></strong>
   </td>
   <td>Updates the order. A manager can use this endpoint to set a delivery crew to this order, and also update the order status to 0 or 1.
<p>
If a delivery crew is assigned to this order and the <strong><code>status = 0</code></strong>, it means the order is out for delivery.
If a delivery crew is assigned to this order and the <strong><code>status = 1</code></strong>, it means the order has been delivered.
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/orders/{orderId}</code></strong>
   </td>
   <td>Manager
   </td>
   <td><strong><code>DELETE</code></strong>
   </td>
   <td>Deletes this order
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/orders</code></strong>
   </td>
   <td>Delivery crew
   </td>
   <td><strong><code>GET</code></strong>
   </td>
   <td>Returns all orders with order items assigned to the delivery crew
   </td>
  </tr>
  <tr>
   <td><strong><code>/api/orders/{orderId}</code></strong>
   </td>
   <td>Delivery crew
<p>
 
   </td>
   <td><strong><code>PATCH</code></strong>
   </td>
   <td>A delivery crew can use this endpoint to update the order status to 0 or 1. The delivery crew will not be able to update anything else in this order.
   </td>
  </tr>
</table>



## **Additional step**

Implement proper filtering, pagination and sorting capabilities for **<code>/api/menu-items</code></strong> and <strong><code>/api/orders</code></strong> <strong><code>endpoints</code></strong>. Review the videos about[ Filtering and searching](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/h7QUx/video-subtitles) and[ Pagination](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/mEYFj/video-subtitles)<span style="text-decoration:underline;"> </span>as well as the reading[ More on filtering and pagination](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/supplement/oCL3M).


## **Throttling**

Finally, apply some throttling for the authenticated users and anonymous or unauthenticated users. Review the video[ Setting up API throttling](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/lecture/rPE4B/video-subtitles) and the reading[ API throttling for class-based views](https://www.coursera.org/teach/apis/g98MzcdAEeyduw6ktL3Xvw/content/item/supplement/1h6WO) for guidance.

