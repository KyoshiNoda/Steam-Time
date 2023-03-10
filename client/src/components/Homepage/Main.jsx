import React from 'react';
import Card from './Card';
function Main() {
  return (
    <div className="hero min-h-screen bg-base-200">
      <div className="hero-content flex-col lg:flex-row-reverse">
        <Card />
        <div className="flex flex-col gap-2 m-20">
          <h1 className="text-5xl font-bold">Steam Time!</h1>
          <div className="font-semibold">
            Tracks their gaming session and provide health statistics.
            <br />
            Cultivates a healthy game/break ratio and attempts to prevent the
            user from playing videogames too long <br />
          </div>
          <a href = '/signup' className='flex flex-col'>
            <button className="btn btn-primary text-lg">View More</button>
          </a>
        </div>
      </div>
    </div>
  );
}

export default Main;
