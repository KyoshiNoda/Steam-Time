import React from "react";
import Background from "../components/Background";
import NavBar from "../components/NavBar/NavBar";
import Time from "../components/Timer/Time";
function Timer() {
  return (
    <Background>
      <NavBar />
      <div className="flex justify-center items-center h-96 bg-base-300">
        <Time/>
      </div>
    </Background>
  );
}

export default Timer;
