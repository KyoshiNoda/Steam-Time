import React, { useState } from 'react';
import Axios from 'axios';
function SignUpForm() {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();
  const [confirmPassword, setConfirmPassword] = useState();
  const [url, setURL] = useState();
  const [apiKey, setAPIKey] = useState();

  const formHandler = (event) => {
    event.preventDefault();
    if (
      email === undefined ||
      password === undefined ||
      confirmPassword === undefined ||
      apiKey === undefined
    ) {
      return;
    }
    if (password.length < 10) {
      console.log('password not long enough');
      return;
    }
    if (password !== confirmPassword) {
      console.log('password does not match');
      return;
    }

    let user = {
      email: email,
      password: password,
      apiKey: apiKey,
      steamURL: url,
    };
    Axios.post('http://localhost:8000/api/auth/register', user)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  return (
    <form className="space-y-4 md:space-y-6" action="#">
      <div>
        <label
          htmlFor="email"
          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >
          Your email
        </label>
        <input
          type="email"
          onChange={(event) => setEmail(event.target.value)}
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
          onChange={(event) => setPassword(event.target.value)}
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
          onChange={(event) => setConfirmPassword(event.target.value)}
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
          onChange={(event) => setURL(event.target.value)}
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
          onChange={(event) => setAPIKey(event.target.value)}
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
        onClick={formHandler}
        className="btn btn-success w-full"
      >
        Submit
      </button>
      <p className="text-sm font-lighttext-gray-500 dark:text-gray-400">
        Already have an account? {}
        <a
          href="/SignIn"
          className="font-medium text-primary-600 hover:underline dark:text-primary-500"
        >
          Login here
        </a>
      </p>
    </form>
  );
}

export default SignUpForm;
