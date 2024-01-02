import React from 'react';
import { FaSteamSquare } from 'react-icons/fa';

const SteamButton = () => {
  return (
    <a
      href="http://localhost:8000/"
      className="flex items-center bg-green-600 h-1/2 text-white cursor-pointer overflow-hidden rounded-5 rounded-lg justify-center p-2 gap-2"
    >
      <span className="font-bold tracking-wider uppercase text-14">Login With Steam</span>
      <FaSteamSquare className="text-white text-30 leading-50 transition-all" size={24}/>
    </a>
  );
};

export default SteamButton;
