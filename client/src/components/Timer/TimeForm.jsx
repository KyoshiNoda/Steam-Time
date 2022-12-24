import React, {useState} from "react";

function TimeForm() {
  const [hours,setHours] = useState();
  const [mins, setMins] = useState();

  const hoursHandler = (event)=>{
    setHours(event.target.value);
    console.log(hours);
  }

  const minsHandler = (event) =>{
    setMins(event.target.value);
    console.log(mins);
  }


  return (
    <div className="flex flex-col">
      <div className="flex justify-center gap-10">
        <div className="form-control w-32 max-w-xs">
          <label className="label">
            <span className="label-text font-semibold">Hours</span>
          </label>
          <input
            type="number"
            onChange={hoursHandler}
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
            onChange={minsHandler}
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