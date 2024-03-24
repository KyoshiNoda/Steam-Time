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

  const [emailError, setEmailError] = useState('');
  const [passwordError, setPasswordError] = useState(false);
  const dispatch = useAppDispatch();
  const navigate = useNavigate();

  const registerAccount = async () => {
    try {
      await dispatch(
        registerUser({
          email: emailRef.current.value,
          password: passwordRef.current.value,
          steamURL: steamURLRef.current.value,
          apiKey: apiKeyRef.current.value,
        })).unwrap();
        navigate('auth/main');
    } catch (error) {
      console.log(error);
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
          className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="name@company.com"
        />
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
          className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        />
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
          className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        />
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
          className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        />
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
          className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        />
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
