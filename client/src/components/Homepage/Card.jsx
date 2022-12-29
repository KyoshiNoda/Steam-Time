import React, { useState, useEffect } from 'react';
import Axios from 'axios';
function Card() {
  let games = {};
  const [gameList, setGameList] = useState(games);
  const [profile, setProfile] = useState({});
  const [gameID, setGameID] = useState("loading");
  useEffect(() => {
    let cancel = false;
    async function startFetch(){
      Axios.get('http://localhost:6969/ownedgames')
      .then((res) => {
        games = res.data.response.games;
        setGameList(games);
      })
      .catch((err) => {
        console.log(err);
      });
    }
    startFetch();
    return () =>{
      cancel = true;
    }
  },[]);
  useEffect(() => { 
    let cancel = false;
    async function startFetch(){
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
    }
    startFetch();
    return () =>{
      cancel = true;
    }
  },[]);
  useEffect(() => { 
    let cancel = false;
    async function startFetch(){
      Axios.get(`http://localhost:3001/appid/${favGame}`)
      .then((res) =>{
        favGame = res;
        setGameID(res.data);
        console.log(res);
      })
      .catch((err) => {
          console.log(err);
      });
    }
    startFetch();
    return () =>{
      cancel = true;
    }
  },[]);
  const mostPlayedGame = () =>{
    let maxTime = 0;
    let name = '';
    for (let i = 0; i < gameList.length; i++) {
      if (gameList[i].playtime_forever > maxTime) {
        name = gameList[i].appid;
        maxTime = gameList[i].playtime_forever;
      }
    }
    return name;
  }
  const totalMins = () =>{
    let totalMins = 0;
    for (let i = 0; i < gameList.length; i++) {
      totalMins += gameList[i].playtime_forever;
    }
    return totalMins;
  }
  let favGame = mostPlayedGame();
  let hoursPlayed = Math.round(totalMins() / 60);

  const user = {
    name: profile.name,
    totalGames: gameList.length,
    totalPlayTime: hoursPlayed,
    favGame: gameID,
    image: profile.image,
  };

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
