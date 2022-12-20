const button = document.querySelector('button');
const fetchAPI = () =>{
  const url = `http://api.steampowered.com/ISteamApps/GetAppList/v2`;
  fetch(url).then((res)=>{
    res.json()
  }).then((data)=>{
    console.log(data);
  })
}

button.addEventListener('click',()=>{
  fetchAPI();
});