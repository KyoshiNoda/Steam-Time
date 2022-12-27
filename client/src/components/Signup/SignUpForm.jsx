import React,{useState} from 'react'
function SignUpForm() {
    const [email,setEmail] = useState();
    const [password, setPassword] = useState();
    const [confirmPassword, setConfirmPassword] = useState();
    const [steamURL, setSteamURL] = useState();

    const emailHandler = (event) =>{
        setEmail(event.target.value);
        console.log(email);
    }

    const passwordHandler = (event) =>{
        setPassword(event.target.value);
        console.log(password);
    }

    const confirmPasswordHandler = (event) =>{
        setConfirmPassword(event.target.value);
        console.log(confirmPassword);
    }

    const steamURLHandler =(event) =>{
        setSteamURL(event.target.value);
        console.log(steamURL);
    }
    
    return (
        <form className="space-y-4 md:space-y-6" action="#">
            <div>
                <label htmlFor="email" 
                className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    Your email
                </label>
                <input type="email"
                onChange={emailHandler}
                name="email" id="email" 
                required=""
                className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                placeholder="name@company.com" 
                />
            </div>
            <div>
                <label 
                htmlFor="password" 
                className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    Password
                </label>
                <input type="password"
                onChange = {passwordHandler}
                name="password" 
                id="password" 
                placeholder="••••••••" 
                required=""
                className= "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                />
            </div>
            <div>
                <label 
                htmlFor="confirm-password" 
                className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    Confirm password
                </label>
                <input
                onChange = {confirmPasswordHandler}
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
                className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                    Steam URL
                </label>
                <input
                onChange={steamURLHandler}
                type="text"
                name="steamURL"
                id="steamURL"
                placeholder="https://steamcommunity.com/id/PlentyJapan"
                required=""
                className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                />
            </div>
            <button 
            className="btn btn-success w-full">
                Submit 
            </button>
            <p className="text-sm font-lighttext-gray-500 dark:text-gray-400">
                Already have an account? 
                <a href="/signout" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                    Login here
                </a>
            </p>
        </form>
  )
}

export default SignUpForm