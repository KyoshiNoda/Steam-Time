import React, { useState, useEffect } from 'react';
import { getTimeLeftMS } from '../../Utils/CountDownTimerUtils';
const defaultTime = {
  hours: '00',
  mins: '00',
  secs: '00',
};

function CountDownTimer(props) {
  const [timeLeft, setTimeLeft] = useState(defaultTime);

  useEffect(() => {
    const timeID = setInterval(() => {
      updateTimeLeft(props.timeMS);
    }, 1000);
    return () => clearInterval(timeID);
  }, [props.timeMS]);

  const updateTimeLeft = (countdown) => {
    setTimeLeft(getTimeLeftMS(countdown));
  };
  return (
    <div className="flex justify-center gap-5 bg-slate-600 p-10 text-white font-bold text-6xl">
      <div className="h-96 w-96 bg-slate-500 rounded">
        <div className="flex justify-center items-end h-1/2">
          <span>{timeLeft.hours}</span>
        </div>

        <div className="flex justify-center items-end h-1/2">
          <span>Hours</span>
        </div>
      </div>
      <div className="h-96 w-96 bg-slate-500 rounded">
        <div className="flex justify-center items-end h-1/2">
          <span>{timeLeft.mins}</span>
        </div>

        <div className="flex justify-center items-end h-1/2">
          <span>Mins</span>
        </div>
      </div>
      <div className="h-96 w-96 bg-slate-500 rounded">
        <div className="flex justify-center items-end h-1/2">
          <span>{timeLeft.secs}</span>
        </div>

        <div className="flex justify-center items-end h-1/2">
          <span>Secs</span>
        </div>
      </div>
    </div>
  );
}

export default CountDownTimer;
