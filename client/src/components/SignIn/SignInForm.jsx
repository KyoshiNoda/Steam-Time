import React, { useState } from 'react';
import SignInModal from './SignInModal';
import { Link } from 'react-router-dom';
import SteamLogin from './SteamLogin';
function SignInForm() {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();

  const emailHandler = (event) => {
    setEmail(event.target.value);
    console.log(email);
  };
  const passwordHandler = (event) => {
    setPassword(event.target.value);
    console.log(password);
  };
  return (
    <div className="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
      <div className="card-body">
        <div className="form-control">
          <label className="label">
            <span className="label-text">Email</span>
          </label>
          <input
            onChange={emailHandler}
            type="text"
            placeholder="email"
            className="input input-bordered"
          />
        </div>
        <div className="form-control">
          <label className="label">
            <span className="label-text">Password</span>
          </label>
          <input
            onChange={passwordHandler}
            type="text"
            placeholder="password"
            className="input input-bordered"
          />
          <div className="flex">
            <label className="label">
              <SignInModal />
            </label>
            <Link to={'/register'}>
              <label className="label justify-end text-sm cursor-pointer">
                Don't have any account?
              </label>
            </Link>
          </div>
        </div>
        <div className="form-control mt-2">
          <button className="btn btn-primary">Login</button>
        </div>
        <div className="form-control">
          <SteamLogin />
        </div>
      </div>
    </div>
  );
}

export default SignInForm;
