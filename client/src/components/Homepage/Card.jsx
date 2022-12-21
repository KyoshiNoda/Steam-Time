import React from 'react'

function Card() {
    const user = {
        name : 'PlentyJapan',
        totalGames: 79,
        totalPlayTime: 1230
    };
  return (
    <div className="card w-96 glass text-white">
        <figure><img src="https://placeimg.com/400/225/arch" alt="car!"/></figure>
        <div className="card-body">
            <h1 className="card-title">{user.name}</h1>
            <h2>Games Owned: {user.totalGames}</h2>
            <h2>Total Playtime: {user.totalPlayTime}</h2>
            <div className="card-actions justify-end">
                <button className="btn btn-primary">View More</button>
            </div>
        </div>
    </div>

    // <div class="card w-96 h-96 bg-base-100 shadow-xl image-full">
    //     <figure><img src="https://placeimg.com/400/225/arch" alt="Shoes" /></figure>
    //     <div class="card-body">
    //         <h2 class="card-title">{user.name}</h2>
    //         <h2>Games Owned: {user.totalGames}</h2>
    //         <h2>Total Playtime: {user.totalPlayTime}</h2>
    //         <div class="card-actions justify-end">
    //         </div>
    //     </div>
    // </div>



  )
}

export default Card