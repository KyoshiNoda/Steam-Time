import React, {useState,useEffect} from 'react'
import Axios from 'axios';
function Card() {

  useEffect(()=>{
    Axios.get('http://localhost:6969/profile')
    .then(res =>{
      console.log(res);
    })
    .catch(err =>{
      console.log(err);
    })
  })





  const user = {
      name : 'PlentyJapan',
      totalGames: 79,
      totalPlayTime: 1230,
      favGame: 'Watch_Dogs 2',
      image: 'https://avatars.akamai.steamstatic.com/b85bfe3287228fc57f8f555dbaa71da329abf8f9_full.jpg'
  };
  return (
    <div className='flex justify-evenly gap-5'>

      <div className="card card-compact w-96 bg-base-100 shadow-xl">
        <figure><img className = 'w-full' src= {user.image} alt = 'steamLogo'/></figure>
        <div className="card-body p-5 m-5 font-semibold">
            <h1 className="card-title justify-center text-3xl">{user.name}</h1>
            <h2>Games Owned: {user.totalGames}</h2>
            <h2>Total Playtime: {user.totalPlayTime} hours</h2>
            <h2>Favorite Game: {user.favGame}</h2>
        </div>
      </div>

      <div className="card card-compact w-96 bg-base-100 shadow-xl">
          <figure><img className = 'w-full' src= {user.image} alt = 'steamLogo'/></figure>
          <div className="card-body p-5 m-5 font-semibold">
              <h1 className="card-title justify-center text-3xl">{user.name}</h1>
              <h2>Games Owned: {user.totalGames}</h2>
              <h2>Total Playtime: {user.totalPlayTime} hours</h2>
              <h2>Favorite Game: {user.favGame}</h2>
          </div>
      </div>
    </div>

  )
}

export default Card