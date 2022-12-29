import React, { useState, useEffect } from 'react';
import Axios from 'axios';
function Card() {
  let games = {};
  const [gameList, setGameList] = useState(games);
  const [profile, setProfile] = useState({});
  useEffect(() => {
    Axios.get('http://localhost:6969/ownedgames')
      .then((res) => {
        games = res.data.response.games;
        setGameList(games);
      })
      .catch((err) => {
        console.log(err);
      });
    Axios.get('http://localhost:6969/profile')
      .then((res) => {
        setProfile({
          name: res.data[3],
          link: res.data[4],
          image: res.data[7],
        });
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);
  let totalMins = 0;
  let maxTime = 0;
  let favGame = '';
  for (let i = 0; i < gameList.length; i++) {
    totalMins += gameList[i].playtime_forever;
    if (gameList[i].playtime_forever > maxTime) {
      favGame = gameList[i].appid;
      maxTime = gameList[i].playtime_forever;
    }
  }
  let totalHours = Math.round(totalMins / 60);
  const user = {
    name: profile.name,
    totalGames: gameList.length,
    totalPlayTime: totalHours,
    favGame: favGame,
    image: profile.image,
  };
  useEffect(() =>{
    Axios.post('http://localhost:3001/appid',favGame)
    .then((res)=>{
      console.log(res.data);
    })
  },[favGame]);


  return (
    <div className="flex justify-evenly gap-5">
      <div className="card card-compact w-96 bg-base-100 shadow-xl">
        <figure>
          <img className="w-full" src={user.image} alt="steamLogo" />
        </figure>
        <div className="card-body p-5 m-5 font-semibold">
          <h1 className="card-title justify-center text-3xl">{user.name}</h1>
          <h2>Games Owned: {user.totalGames}</h2>
          <h2>Total Playtime: {user.totalPlayTime} hours</h2>
          <h2>Favorite Game ID: {user.favGame}</h2>
        </div>
      </div>
    </div>
  );
}

export default Card;
