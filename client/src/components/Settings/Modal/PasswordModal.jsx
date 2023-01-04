import React from 'react';

function PasswordModal() {
  return (
    <>
      <label htmlFor="my-modal-3" className="btn bg-yellow-400 hover:bg-blue-400 text-white">
        Change Password
      </label>
      <input type="checkbox" id="my-modal-3" className="modal-toggle" />
      <div className="modal">
        <div className= "flex flex-col modal-box w-11/12 max-w-5xl">

          <label
            htmlFor="my-modal-3"
            className="btn btn-sm btn-circle absolute right-2 top-2"
          >
            x
          </label>
          <label className="label">
            <span className="label-text">Current Password</span>
          </label>
          <input
            type="password"
            placeholder="••••••••"
            className="input input-bordered"
          />
          <label className="label">
            <span className="label-text">New Password</span>
          </label>
          <input
            type="password"
            placeholder="••••••••"
            className="input input-bordered"
          />
          <label className="label">
            <span className="label-text">Confirm new password</span>
          </label>
          <input
            type="password"
            placeholder="••••••••"
            className="input input-bordered"
          />
          <button className="btn btn-success">Change</button>
        </div>
      </div>
    </>
  );
}

export default PasswordModal;
