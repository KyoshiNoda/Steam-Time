import React from "react";
import Background from "../components/Background";
import NavBar from "../components/NavBar/NavBar";
import CountDown from "../components/Timer/CountDown";
function Timer() {
  return (
    <Background>
      <NavBar />
      <div className="flex justify-center items-center h-96 bg-base-300">
        <CountDown />
      </div>
    </Background>
  );
}

export default Timer;
