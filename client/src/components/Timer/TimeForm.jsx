import React, {useState} from "react";

function TimeForm({getTime}) {
  const [hours,setHours] = useState(0);
  const [mins, setMins] = useState(0);

  const formHandler = (event) =>{
    event.preventDefault();
    getTime(hours,mins);
  };

  const hoursHandler = (event)=>{ setHours(event.target.value) }
  const minsHandler = (event) =>{ setMins(event.target.value) }

  return (
    <form onSubmit={formHandler}>
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
                <button type = 'submit' className="btn btn-primary w-32">Submit Me</button>
            </div>
        </div>
    </form>
  );
}
export default TimeForm;