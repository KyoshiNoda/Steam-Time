import React,{useState} from "react";
import SignInForm from "../components/SignIn/SignInForm";
function SignIn() {
  return (
    <>
      <div className="hero min-h-screen bg-base-200">
        <div className="hero-content flex-col lg:flex-row-reverse">
          <div className="text-center lg:text-left">
            <h1 className="text-5xl font-bold">Login now!</h1>
            <p className="py-6">
              Get access to your steam game playtime and learn more about your gaming habits!
            </p>
          </div>
          <SignInForm/>
        </div>
      </div>
    </>
  );
}

export default SignIn;
