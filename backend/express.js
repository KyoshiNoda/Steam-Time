const express = require('express');
const path = require('path');
const app = express();
const cors=require("cors");
const corsOptions ={
   origin:'*', 
   credentials:true,  //access-control-allow-credentials:true
   optionSuccessStatus:200,
}

app.use(cors(corsOptions)) // Use this after the variable declaration

app.set('views', path.join(__dirname,'views'));
app.set('view engine', "ejs");

app.listen(3001,()=>{
  console.log("Listening to port 3001");
});

app.get('/',(req,res)=>{
  res.render("view");
});