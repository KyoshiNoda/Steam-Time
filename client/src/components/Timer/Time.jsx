import React, { useState, useEffect } from "react";
import CountDown from "./CountDown";
function Time() {
  const [value, setValue] = useState('0')

  useEffect(() => {
    const timer = setTimeout(() => {
      setValue((v) => (v <= 0 ? value : v - 1));
    }, 1000);
    
    return () => {
      clearTimeout(timer);
    };
  }, [value]);

  return (
    <div className="grid grid-flow-col gap-5 text-center auto-cols-max">
      <div className="flex flex-col p-2 bg-neutral rounded-box text-neutral-content">
        <CountDown className="font-mono text-5xl" value={15} />
        days
      </div>
      <div className="flex flex-col p-2 bg-neutral rounded-box text-neutral-content">
        <CountDown className="font-mono text-5xl" value={10} />
        hours
      </div>
      <div className="flex flex-col p-2 bg-neutral rounded-box text-neutral-content">
        <CountDown className="font-mono text-5xl" value={24} />
        min
      </div>
      <div className="flex flex-col p-2 bg-neutral rounded-box text-neutral-content">
        <CountDown className="font-mono text-5xl" value={value} />
        sec
      </div>
    </div>
  );
}

export default Time;
