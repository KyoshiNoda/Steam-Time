const express = require('express');
const appid = require("appid");
const bodyParser = require("body-parser");
const cors=require("cors");
const app = express();

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.listen(3001,()=>{
  console.log("Listening to port 3001");
});

app.get('/',(req,res)=>{
  res.send("nodemon is working");
});

app.get('/appid',(req,res)=>{
  (async () => {
    let game = await appid(1085660)
    res.send(game.name);
  })();
});