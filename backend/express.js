const express = require('express');
const app = express();

app.listen(3001,()=>{
  console.log("Listening to port 3001");
});

app.get('/',(req,res)=>{
  res.sendFile(path.join(__dirname, '/index.html'));
});