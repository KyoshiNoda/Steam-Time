import React from "react";

function CountDown(props) {
  return (
    <span className="countdown font-mono text-5xl">
      <span>{props.value}</span>
    </span>
  );
}

export default CountDown;
