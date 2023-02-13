import React from 'react';

function SignInModal() {
  return (
    <>
      {/* The button to open modal */}
      <label htmlFor="my-modal-3" className="label-text-alt link link-hover">
        Forgot Password?
      </label>
      <input type="checkbox" id="my-modal-3" className="modal-toggle" />
      <div className="modal">
        <div className="modal-box relative">
          <label
            htmlFor="my-modal-3"
            className="btn btn-sm btn-circle absolute right-2 top-2"
          >
            ✕
          </label>
          <h3 className="text-lg font-bold mb-5 text-center">
            Please check your email and submit code below!
          </h3>
          <div className='flex justify-center'>
            <input
              type="text"
              className="input input-bordered text-center"
            />
          </div>
        </div>
      </div>
    </>
  );
}

export default SignInModal;
