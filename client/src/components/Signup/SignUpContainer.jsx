import React, { useState } from 'react';
import SignUpForm from './SignUpForm';
import Axios from 'axios';
import Alert from './Alert';
function SignUpContainer() {
  const [isMissingInfo, setIsMissingInfo] = useState(false);
  const [isPasswordLength, setIsPasswordLength] = useState(false);
  const [isPasswordMatch, setIsPasswordMatch] = useState(false);
  const currentUserHandler = (user) => {
    let jsonUser = JSON.stringify(user);
    Axios.post(`http://localhost:6969/createaccount`, jsonUser)
      .then((res) => {
        console.log(res);
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
  return (
    <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
      <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
        <h1 className="text-center text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
          Create Account
        </h1>
        <SignUpForm
          currentUser={currentUserHandler}
          missingInfo={alertHandler}
          passwordLength={passwordLengthHandler}
          passwordMatch={passwordMatchHandler}
        />
        {isMissingInfo ? <Alert text="You are missing info!" /> : <></>}
        {isPasswordLength ? <Alert text="password not long enough" /> : <></>}
        {isPasswordMatch ? <Alert text="password does not match" /> : <></>}
      </div>
    </div>
  );
}

export default SignUpContainer;
