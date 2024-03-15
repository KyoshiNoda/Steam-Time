import React from 'react';
import SignUpContainer from '../components/Signup/SignUpContainer';
import { Link } from 'react-router-dom';
function SignUp() {
  return (
    <section className="bg-gradient-to-b from-slate-900 to-slate-500 dark:bg-gray-900">
      <div className="flex flex-col items-center justify-center px-2 py-2 mx-auto md:h-screen lg:py-0">
        <Link
          to="/"
          className="text-white flex items-center mb-6 text-4xl font-semibold dark:text-white"
        >
          SteamTime
        </Link>
        <SignUpContainer />
      </div>
    </section>
  );
}

export default SignUp;
