import React, { useState } from 'react';
import SignUpForm from './SignUpForm';
import Axios from 'axios';
import Alert from './Alert';
import SteamBox from './SteamBox';
function SignUpContainer() {
  const [isManual, setIsManual] = useState(true);
  const [isSteam, setIsSteam] = useState(false);
  const [isMissingInfo, setIsMissingInfo] = useState(false);
  const [isPasswordLength, setIsPasswordLength] = useState(false);
  const [isPasswordMatch, setIsPasswordMatch] = useState(false);
  const currentUserHandler = (user) => {
    let jsonUser = JSON.stringify(user);
    Axios.post(`http://localhost:5000/create-account`, {
      email: "dyl@example.com",
      steam_name: "Dilianx",
      password: "test123",
      api_key: "lolol"
    })
      .then((res) => {
        console.log(res);
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err);
      });
  };
  const alertHandler = (res) => {
    setIsMissingInfo(res);
  };
  const passwordLengthHandler = (res) => {
    setIsPasswordLength(res);
  };
  const passwordMatchHandler = (res) => {
    setIsPasswordMatch(res);
  };

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
        <div className='flex justify-center items-center gap-3'>
          <button className="btn btn-accent" onClick={handleManualClick}>Manual</button>
          <button className='btn btn-secondary' onClick={handleSteamClick}>Steam</button>
        </div>
        {
          isManual &&
          <SignUpForm
            currentUser={currentUserHandler}
            missingInfo={alertHandler}
            passwordLength={passwordLengthHandler}
            passwordMatch={passwordMatchHandler}
          />
        }
        {
          isSteam && <SteamBox />
        }

        {isMissingInfo ? <Alert text="You are missing info!" /> : <></>}
        {isPasswordLength ? <Alert text="password not long enough" /> : <></>}
        {isPasswordMatch ? <Alert text="password does not match" /> : <></>}
      </div>
    </div>
  );
}

export default SignUpContainer;
