import React from 'react'

function Countdown() {
  return (
    <div className="grid grid-flow-col gap-5 text-center auto-cols-max bg-slate-400">
        <div className="flex flex-col p-2 bg-neutral rounded-box text-neutral-content">
            <span className="countdown font-mono text-5xl">
                <span style={{"--value":15}}></span>
            </span>
            3 days
        </div> 
        <div className="flex flex-col p-2 bg-neutral rounded-box text-neutral-content">
            <span className="countdown font-mono text-5xl">
            <span style={{"--value":10}}></span>
            </span>
           5 hours
        </div> 
        <div className="flex flex-col p-2 bg-neutral rounded-box text-neutral-content">
            <span className="countdown font-mono text-5xl">
                <span style={{"--value":24}}></span>
            </span>
            10 min
        </div> 
        <div className="flex flex-col p-2 bg-neutral rounded-box text-neutral-content">
            <span className="countdown font-mono text-5xl">
                <span style={{"--value":53}}></span>
            </span>
        </div>
    </div>
  )
}

export default Countdown