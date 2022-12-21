import React from "react";

function TimeForm() {
  return (
    <div className="flex flex-col">
      <div className="flex justify-center gap-10">
        <div className="form-control w-32 max-w-xs">
          <label className="label">
            <span className="label-text font-semibold">Hours</span>
          </label>
          <input
            type="number"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs"
          />
        </div>

        <div className="form-control w-32 max-w-xs">
          <label className="label">
            <span className="label-text font-semibold">Minutes</span>
          </label>
          <input
            type="number"
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs"
          />
        </div>
      </div>

      <div className="flex justify-center m-3">
        <button className="btn btn-primary w-32">Submit Me</button>
      </div>
    </div>
  );
}

export default TimeForm;
