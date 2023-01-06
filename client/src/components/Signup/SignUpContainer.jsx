import React from 'react';
import SignUpForm from './SignUpForm';
function SignUpContainer() {
  const currentUserHandler = (user) =>{
    console.log(user);
  }
  return (
    <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
      <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
        <h1 className="text-center text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
          Create Account
        </h1>
        <SignUpForm currentUser = {currentUserHandler}/>
      </div>
    </div>
  );
}

export default SignUpContainer;
