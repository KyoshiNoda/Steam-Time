import React, { useState } from 'react';
import NavBar from '../components/NavBar/NavBar';
import CountDownTimer from '../components/Timer/CountDownTimer';
import TimeForm from '../components/Timer/TimeForm';
import dayjs from 'dayjs';
function Timer() {
  const [finalTime, setFinalTime] = useState(0);
  const timeHandler = (uHours, uMins) => {
    const timeMil = (uHours * 60 * 60 + uMins * 60) * 1000;
    setFinalTime(timeMil);
  };
  const currentTime = dayjs().valueOf() + finalTime;

  return (
    <>
      <NavBar />
      <CountDownTimer timeMS={currentTime} />
      <TimeForm getTime={timeHandler} />
    </>
  );
}

export default Timer;
