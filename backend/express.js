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
  res.send("THIS IS WORKINGGGG");
});

(async () => {
  let dota = await appid("Counter-Strike")
  console.log(dota.appid) // 10

  let mystery = await appid(730)
  console.log(mystery.name) //  "Counter-Strike: Global Offensive"

  let gta = await appid(/Grand Theft Auto/)
  console.log(gta.slice(0,5))

})();