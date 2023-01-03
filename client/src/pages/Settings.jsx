import React from 'react';
import NavBar from '../components/NavBar/NavBar';
function Settings() {
  return (
    <>
      <NavBar />
      <div className="flex justify-center">
        <div className="bg-slate-50 w-1/2 justify-evenly font-bold p-10 rounded space-y-5">
          <h1 className="text-3xl text-black">John Doe</h1>
          <div className="flex">
            <div className="flex-1 first:mr-10">
              <div className="form-control w-full max-w-xs">
                <label className="label">
                  <span className="label-text lg:text-xl">First Name</span>
                </label>
                <input
                  type="text"
                  placeholder="John"
                  className="input input-bordered w-full max-w-xs"
                />
              </div>
              <div className="form-control w-full max-w-xs">
                <label className="label">
                  <span className="label-text lg:text-xl">Last Name</span>
                </label>
                <input
                  type="text"
                  placeholder="Doe"
                  className="input input-bordered w-full max-w-xs"
                />
              </div>
            </div>

            <div className="mr-10">
              <div className="form-control w-full max-w-xs">
                <label className="label">
                  <span className="label-text lg:text-xl">Steam URL</span>
                </label>
                <input
                  type="text"
                  placeholder="https://steamcommunity.com/id/Dilian1"
                  className="input input-bordered w-full max-w-xs"
                />
              </div>
              <div className="form-control w-full max-w-xs">
                <label className="label">
                  <span className="label-text lg:text-xl">API Key</span>
                </label>
                <input
                  type="text"
                  placeholder="JH2H32K3214H1213"
                  className="input input-bordered w-full max-w-xs"
                />
              </div>
            </div>

          </div>

          <div className='flex justify-center gap-5'>
            <button className="btn btn-outline btn-success">
              Save Changes
            </button>
            <button className="btn btn-outline btn-warning">
              Change Password
            </button> 
          </div>
        </div>
      </div>
    </>
  );
}

export default Settings;
