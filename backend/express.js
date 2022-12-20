const express = require('express');
const path = require('path');
const app = express();


app.set('views', path.join(__dirname,'views'));
app.set('view engine', "ejs");

app.listen(3001,()=>{
  console.log("Listening to port 3001");
});

app.get('/',(req,res)=>{
  res.render("view");
});