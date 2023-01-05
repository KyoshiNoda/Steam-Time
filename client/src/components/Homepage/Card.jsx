import React, { useState, useEffect } from 'react';
import {totalMins } from '../../Utils/CardAPI';
import Axios from 'axios';
function Card() {
  const [gameList, setGameList] = useState({});
  const [profile, setProfile] = useState({});
  const [favGame, setFavGame] = useState("loading");
  useEffect(() => {
    Axios.get('http://localhost:6969/ownedgames')
    .then((res) => {
      setGameList(res.data.response.games);
    })
    .catch((err) => {
      console.log(err);
    });
  },[]);
  useEffect(() => {
    Axios.get('http://localhost:6969/profile')
    .then((res) => {
      setProfile({
        name : res.data.personaname,
        image : res.data.avatarfull,
        link : res.data.profileurl
      });
    })
    .catch((err) => {
      console.log(err);
    });
  },[]);
  useEffect(() => { 
    Axios.get(`http://localhost:3001/appid`)
    .then((res) =>{
      setFavGame(res.data);
    })
    .catch((err) => {
        console.log(err);
    });
  },[]);

  // let gameID = favGameID(gameList);
  let hoursPlayed = Math.round(totalMins(gameList) / 60);

  const user = {
    name: profile.name,
    totalGames: gameList.length,
    totalPlayTime: hoursPlayed,
    gameName: favGame,
    image: profile.image,
    link : profile.link
  };

  return (
    <a href = {user.link}>
      <div className="flex justify-evenly gap-5">
        <div className="card card-compact w-96 bg-base-100 shadow-xl">
          <figure>
            <img className="w-full" src={user.image} alt="steamLogo" />
          </figure>
          <div className="card-body p-5 m-5 font-semibold">
            <h1 className="card-title justify-center text-3xl">{user.name}</h1>
            <h2>Games Owned: {user.totalGames}</h2>
            <h2>Total Playtime: {user.totalPlayTime} hours</h2>
            <h2>Favorite Game ID: {user.gameName}</h2>
          </div>
        </div>
      </div>
    </a>
  );
}

export default Card;
