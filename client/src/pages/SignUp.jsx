import React from 'react'
import SignUpContainer from '../components/Signup/SignUpContainer'
function SignUp() {
  return (
    <section className=" bg-gradient-to-b from-slate-900 to-slate-500 dark:bg-gray-900">
      <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
        <a href="/" className="text-white flex items-center mb-6 text-4xl font-semibold dark:text-white">
            SteamTime
        </a>
        <SignUpContainer/>
      </div>
    </section>
  )
}

export default SignUp