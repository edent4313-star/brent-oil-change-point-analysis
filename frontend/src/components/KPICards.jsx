import React from "react";

function KPITable({ data }) {
  return (
    <div className="bg-[#1e293b] p-6 rounded-xl shadow-lg border border-slate-700 w-full max-w-sm mx-auto flex flex-col items-center">
      <h3 className="text-lg font-bold mb-6 text-blue-400 border-b border-slate-700 w-full pb-3 text-center uppercase tracking-widest">
        Market Summary
      </h3>
      
      {/* FORCED CENTERING WRAPPER */}
      <div className="w-full flex justify-center">
        <table className="w-full text-center border-collapse">
          <thead>
            <tr className="bg-slate-800 text-slate-500 uppercase text-[10px] font-black tracking-widest">
              <th className="py-3 px-4 border-b border-slate-700">Indicator</th>
              <th className="py-3 px-4 border-b border-slate-700 text-blue-300">Analysis</th>
            </tr>
          </thead>
          <tbody className="text-slate-300 text-sm">
            <tr className="hover:bg-slate-800/50 border-b border-slate-800">
              <td className="py-4 px-4 text-slate-400">Price</td>
              <td className="py-4 px-4 text-white font-bold text-lg">$ {data.current_price || 0}</td>
            </tr>
            <tr className="hover:bg-slate-800/50 border-b border-slate-800">
              <td className="py-4 px-4 text-slate-400">Change</td>
              <td className="py-4 px-4 font-bold" style={{ color: data.percentage_change >= 0 ? '#10b981' : '#f43f5e' }}>
                {data.percentage_change || 0}%
              </td>
            </tr>
            <tr className="hover:bg-slate-800/50 border-b border-slate-800">
              <td className="py-4 px-4 text-slate-400">Volatility</td>
              <td className="py-4 px-4 text-blue-300">{data.volatility || 0}%</td>
            </tr>
            <tr className="bg-blue-900/20">
              <td className="py-4 px-4 font-bold text-blue-400 text-[10px] uppercase">AI Switch</td>
              <td className="py-4 px-4 font-bold text-blue-400 text-[10px] font-mono whitespace-nowrap">
                {data.change_point_date || "2005-05-28"}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default KPITable;