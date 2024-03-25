import { useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import SteamLogin from '../SignIn/SteamLogin';
import { useAppDispatch } from '../../redux/store';
import { useNavigate } from 'react-router-dom';
import { registerUser } from '../../redux/feats/auth/authActions';
const SignUpForm = () => {
  const emailRef = useRef(null);
  const passwordRef = useRef(null);
  const confirmPasswordRef = useRef(null);
  const steamURLRef = useRef(null);
  const apiKeyRef = useRef(null);

  const [isMissing, setIsMissing] = useState(false);
  const [missingMessage, setMissingMessage] = useState('');

  const [invalidCred, setInvalidCred] = useState(false);
  const [credMessage, setCredMessage] = useState('');

  const [isFound, setIsFound] = useState(false);
  const [foundMessage, setFoundMessage] = useState('');

  const [passwordError, setPasswordError] = useState(false);
  const [passwordErrorMessage, setPasswordErrorMessage] = useState('');

  const dispatch = useAppDispatch();
  const navigate = useNavigate();

  const registerAccount = async () => {
    if (passwordRef.current.value !== confirmPasswordRef.current.value) {
      setPasswordError(true);
      setPasswordErrorMessage('Password do not match');
      return;
    }
    try {
      await dispatch(
        registerUser({
          email: emailRef.current.value,
          password: passwordRef.current.value,
          steamURL: steamURLRef.current.value,
          apiKey: apiKeyRef.current.value,
        })
      ).unwrap();
      navigate('/auth/main');
    } catch (error) {
      const res = error.response;
      const errorMessage = res.data.error;
      if (res.status === 400) {
        setIsMissing(true);
        setMissingMessage(errorMessage);
      } else if (res.status === 403) {
        setIsFound(true);
        setFoundMessage(errorMessage);
      } else if (res.status === 404) {
        setInvalidCred(true);
        setCredMessage(errorMessage);
      } else {
        console.log(error);
      }
    }
  };
  return (
    <div className="space-y-4 md:space-y-6 p-4">
      <div>
        <label
          htmlFor="email"
          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >
          Your email
        </label>
        <input
          ref={emailRef}
          type="email"
          name="email"
          id="email"
          required=""
          placeholder="name@company.com"
          className={`bg-gray-50 border text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
          ${
            isFound || isMissing
              ? 'border-red-500 dark:border-red-700'
              : 'border-gray-300 dark:border-gray-600'
          }`}
        />
        {isMissing && (
          <span className="text-xs text-red-500">{missingMessage}</span>
        )}
        {isFound && (
          <span className="text-xs text-red-500">{foundMessage}</span>
        )}
      </div>
      <div>
        <label
          htmlFor="password"
          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >
          Password
        </label>
        <input
          type="password"
          ref={passwordRef}
          name="password"
          id="password"
          placeholder="••••••••"
          required=""
          className={`bg-gray-50 border text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
          ${
            passwordError || isMissing
              ? 'border-red-500 dark:border-red-700'
              : 'border-gray-300 dark:border-gray-600'
          }`}
        />
        {isMissing && (
          <span className="text-xs text-red-500">{missingMessage}</span>
        )}
        {passwordError && (
          <span className="text-xs text-red-500">{passwordErrorMessage}</span>
        )}
      </div>
      <div>
        <label
          htmlFor="confirm-password"
          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >
          Confirm password
        </label>
        <input
          ref={confirmPasswordRef}
          type="password"
          name="confirm-password"
          id="confirm-password"
          placeholder="••••••••"
          required=""
          className={`bg-gray-50 border text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
          ${
            passwordError || isMissing
              ? 'border-red-500 dark:border-red-700'
              : 'border-gray-300 dark:border-gray-600'
          }`}
        />
        {isMissing && (
          <span className="text-xs text-red-500">{missingMessage}</span>
        )}
        {passwordError && (
          <span className="text-xs text-red-500">{passwordErrorMessage}</span>
        )}
      </div>
      <div>
        <label
          htmlFor="steamURL"
          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >
          Steam URL
        </label>
        <input
          ref={steamURLRef}
          type="text"
          name="steamURL"
          id="steamURL"
          placeholder="https://steamcommunity.com/id/PlentyJapan"
          required=""
          className={`bg-gray-50 border text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
          ${
            invalidCred || isMissing
              ? 'border-red-500 dark:border-red-700'
              : 'border-gray-300 dark:border-gray-600'
          }`}
        />
        {isMissing && (
          <span className="text-xs text-red-500">{missingMessage}</span>
        )}
        {invalidCred && (
          <span className="text-xs text-red-500">{credMessage}</span>
        )}
      </div>
      <div>
        <label
          htmlFor="APIKEY"
          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >
          API Key
        </label>
        <input
          ref={apiKeyRef}
          type="password"
          name="apiKEY"
          id="apiKEY"
          placeholder="••••••••••••••"
          required=""
          className={`bg-gray-50 border text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
          ${
            invalidCred || isMissing
              ? 'border-red-500 dark:border-red-700'
              : 'border-gray-300 dark:border-gray-600'
          }`}
        />
        {isMissing && (
          <span className="text-xs text-red-500">{missingMessage}</span>
        )}
        {invalidCred && (
          <span className="text-xs text-red-500">{credMessage}</span>
        )}
      </div>
      <button
        type="submit"
        onClick={registerAccount}
        className="btn btn-success w-full"
      >
        Submit
      </button>
      <SteamLogin />
      <p className="text-sm font-lighttext-gray-500 dark:text-gray-400">
        Already have an account? {}
        <Link
          to="/login"
          className="font-medium text-primary-600 hover:underline dark:text-primary-500"
        >
          Login here
        </Link>
      </p>
    </div>
  );
};

export default SignUpForm;
