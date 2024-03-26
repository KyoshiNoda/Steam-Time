import { useState } from 'react';
import SignInModal from './SignInModal';
import { Link, useNavigate } from 'react-router-dom';
import SteamLogin from './SteamLogin';
import { useAppDispatch } from '../../redux/store';
import { loginUser } from '../../redux/feats/auth/authActions';
function SignInForm() {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();

  const dispatch = useAppDispatch();
  const navigate = useNavigate();

  const [errorMessage, setErrorMessage] = useState('');

  const [emailError, setEmailError] = useState(false);
  const [passwordError, setPasswordError] = useState(false);
  const [isMissing, setIsMissing] = useState(false);

  const loginHandler = async () => {
    try {
      await dispatch(loginUser({ email: email, password: password })).unwrap();
      navigate('/auth/main');
    } catch (error) {
      let errorMessage = error.response.data.error;
      setErrorMessage(errorMessage);
      if (errorMessage.includes('User')) {
        console.log('for email');
        setEmailError(true);
      } else if (errorMessage.includes('Password')) {
        setPasswordError(true);
      } else {
        setIsMissing(true);
      }
    }
  };

  return (
    <div className="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
      <div className="card-body">
        <div className="form-control">
          <label className="label">
            <span className="label-text">Email</span>
          </label>
          <input
            onChange={(event) => setEmail(event.target.value)}
            type="text"
            placeholder="email"
            className={`input input-bordered border ${
              emailError || isMissing ? 'border-rose-500' : ''
            }`}
          />
          {emailError && (
            <span className="text-xs text-red-500">{errorMessage}</span>
          )}
          {isMissing && (
            <span className="text-xs text-red-500">{errorMessage}</span>
          )}
        </div>
        <div className="form-control">
          <label className="label">
            <span className="label-text">Password</span>
          </label>
          <input
            onChange={(event) => setPassword(event.target.value)}
            type="password"
            placeholder="password"
            className={`input input-bordered border ${
              passwordError || isMissing ? 'border-rose-500' : ''
            }`}
          />
          {passwordError && (
            <span className="text-xs text-red-500">{errorMessage}</span>
          )}
          {isMissing && (
            <span className="text-xs text-red-500">{errorMessage}</span>
          )}
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
          <button className="btn btn-primary" onClick={loginHandler}>
            Login
          </button>
        </div>
        <div className="form-control">
          <SteamLogin />
        </div>
      </div>
    </div>
  );
}

export default SignInForm;
