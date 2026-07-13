import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from "recharts";


const VolatilityChart = ({ data }) => {

  return (
    <div className="card">
      <h3>Oil Price Volatility</h3>

      <ResponsiveContainer width="100%" height={300}>

        <LineChart data={data}>

          <CartesianGrid strokeDasharray="3 3"/>

          <XAxis 
            dataKey="Date"
          />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="volatility"
            stroke="#ff7300"
            strokeWidth={2}
          />

        </LineChart>

      </ResponsiveContainer>

    </div>
  );
};


export default VolatilityChart;