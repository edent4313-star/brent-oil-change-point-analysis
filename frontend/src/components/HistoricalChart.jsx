import React from 'react';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, ReferenceLine, Legend
} from 'recharts';

const HistoricalChart = ({ priceData = [], changePointDate, events = [] }) => {
  
  if (!priceData || priceData.length === 0) {
    return <div className="h-full flex items-center justify-center text-slate-500 italic">Syncing Market Data...</div>;
  }

  return (
    // FORCING HEIGHT TO 400px SO IT DOESN'T DISAPPEAR
    <div style={{ width: '100%', height: '400px' }}>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={priceData} margin={{ top: 20, right: 30, left: 10, bottom: 10 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
          
          <XAxis 
            dataKey="Date" 
            stroke="#94a3b8" 
            fontSize={10} 
            // SAFER FORMATTER: Checks if string exists before splitting
            tickFormatter={(str) => (typeof str === 'string' ? str.split('-')[0] : '')}
            minTickGap={40}
          />
          
          <YAxis stroke="#94a3b8" fontSize={10} domain={['auto', 'auto']} tickFormatter={(v) => `$${v}`} />
          
          <Tooltip 
            contentStyle={{ backgroundColor: '#1e293b', border: '1px solid #475569', borderRadius: '8px', color: '#f1f5f9' }}
            itemStyle={{ color: '#60a5fa' }}
          />
          
          <Legend verticalAlign="top" height={36}/>

          <Line 
            name="Brent Oil Price"
            type="monotone" 
            dataKey="Price" 
            stroke="#3b82f6" 
            strokeWidth={2} 
            dot={false} 
            isAnimationActive={false} 
          />

          {/* PLOTTING RED EVENT FLAGS */}
          {events?.map((event, index) => (
            <ReferenceLine 
              key={index}
              x={event.Date || event.date} 
              stroke="#ef4444" 
              strokeDasharray="4 4"
              label={{ position: 'top', value: '🚩', fill: '#ef4444', fontSize: 14 }} 
            />
          ))}

          {/* PLOTTING THE GREEN AI SIGNAL */}
          {changePointDate && (
            <ReferenceLine 
              x={changePointDate} 
              stroke="#10b981" 
              strokeWidth={3}
              label={{ value: 'AI SWITCH', position: 'insideTopLeft', fill: '#10b981', fontSize: 10, fontWeight: 'bold' }} 
            />
          )}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default HistoricalChart;