import React from 'react'

function CountDownTimer() {
  return (
    <div className='flex justify-center gap-5 bg-slate-600 p-10 text-white font-bold text-6xl'>
        <div className='h-96 w-96 bg-slate-500 rounded'>
            <div className='flex justify-center items-end h-1/2'>
                <span>2</span>
            </div>

            <div className='flex justify-center items-end h-1/2'>
                <span>Hours</span>
            </div>
        </div>
        <div className='h-96 w-96 bg-slate-500 rounded'>
            <div className='flex justify-center items-end h-1/2'>
                <span>30</span>
            </div>

            <div className='flex justify-center items-end h-1/2'>
                <span>Mins</span>
            </div>
        </div>
        <div className='h-96 w-96 bg-slate-500 rounded'>
            <div className='flex justify-center items-end h-1/2'>
                <span>2</span>
            </div>

            <div className='flex justify-center items-end h-1/2'>
                <span>Secs</span>
            </div>
        </div>

    </div>
  )
}

export default CountDownTimer