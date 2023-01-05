import React from 'react'
import { Line } from 'react-chartjs-2';
import {Chart as ChartJS} from 'chart.js/auto';
function BarChart({chartData}) {
  return (
   <Line data={chartData}/>
  )
}

export default BarChart