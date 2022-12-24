import React from "react";
import NavBar from '../components/NavBar/NavBar';
import CountDownTimer from "../components/Timer/CountDownTimer";
import TimeForm from "../components/Timer/TimeForm";
function Timer() {
  return (
    <>
      <NavBar />
      <CountDownTimer timeMS = {401410104014010}/>
      <TimeForm/>
    </>
  );
}

export default Timer;
