import React, { useState } from 'react';
import SignUpForm from './SignUpForm';
import SteamBox from './SteamBox';
function SignUpContainer() {
  const [isManual, setIsManual] = useState(true);
  const [isSteam, setIsSteam] = useState(false);

  const handleManualClick = () => {
    setIsManual(true);
    setIsSteam(false);
  };

  const handleSteamClick = () => {
    setIsManual(false);
    setIsSteam(true);
  };
  
  return (
    <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
      <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
        <h1 className="text-center text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
          Create Account
        </h1>
        <div className="flex justify-center items-center gap-3">
          <button className="btn btn-accent" onClick={handleManualClick}>
            Manual
          </button>
          <button className="btn btn-secondary" onClick={handleSteamClick}>
            Steam
          </button>
        </div>
        {isManual && <SignUpForm />}
        {isSteam && <SteamBox />}
      </div>
    </div>
  );
}

export default SignUpContainer;
