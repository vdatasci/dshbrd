<!doctype html>
<html>
   <body>
   
      <table border = 1>
         <thead>
            <td>Name</td>
            <td>Address</td>
            <td>city</td>
            <td>Pincode</td>
         </thead>
         
         {% for row in rows %}
            <tr>
               <td>{{row["name"]}}</td>
               <td>{{row["addr"]}}</td>
               <td> {{ row["city"]}}</td>
               <td>{{row['pin']}}</td>	
            </tr>
         {% endfor %}
      </table>
      
      <a href = "/">Go back to home page</a>
      
   </body>
</html>
