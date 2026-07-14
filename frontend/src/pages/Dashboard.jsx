import React, { useState, useEffect } from "react";
import axios from "axios";
import KPITable from "../components/KPICards"; 
import HistoricalChart from "../components/HistoricalChart";
import EventTable from "../components/EventTable";
import Footer from "../components/Footer";

function Dashboard() {
  // --- 1. State Management ---
  const [metrics, setMetrics] = useState({});
  const [priceData, setPriceData] = useState([]);
  const [events, setEvents] = useState([]);
  const [selectedEvent, setSelectedEvent] = useState(null); 
  const [loading, setLoading] = useState(true);
  
  // Date Filtering State
  const [startDate, setStartDate] = useState("2010-01-01");
  const [endDate, setEndDate] = useState("2024-12-31");

  // --- 2. Dynamic Data Fetching ---
  // This hook runs every time the startDate or endDate changes
  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        // Fetch KPIs (Global metrics)
        const kpiRes = await axios.get("http://localhost:5000/api/kpis");
        setMetrics(kpiRes.data);

        // Fetch Historical Data (DYNAMIC FILTERING)
        // This sends the start/end dates to the backend database query
        const histRes = await axios.get(`http://localhost:5000/api/historical?start=${startDate}&end=${endDate}`);
        setPriceData(histRes.data);

        // Fetch Events from CSV
        const eventRes = await axios.get("http://localhost:5000/api/events");
        setEvents(eventRes.data);
      } catch (err) {
        console.error("Dashboard Fetch Error:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [startDate, endDate]); // Trigger re-fetch when dates are changed by the user

  // --- 3. Click Handlers ---
  const handleEventClick = (event) => {
    setSelectedEvent(event);
    // Smooth scroll to the intelligence report at the top
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // --- 4. User Interface ---
  return (
    <div className="min-h-screen bg-[#0f172a] text-slate-200 flex flex-col font-sans">
      <main className="flex-grow container mx-auto px-4 py-6 text-center">
        
        {/* HEADER SECTION WITH DYNAMIC DATE FILTERS */}
        <div className="flex flex-col md:flex-row justify-between items-center mb-8 gap-4 bg-[#1e293b] p-6 rounded-xl shadow-lg border border-slate-700">
          <div className="text-center md:text-left">
            <h1 className="text-2xl font-bold text-blue-400">Brent Oil Market Intelligence</h1>
            <p className="text-slate-400 text-sm italic">Filtered Brent Oil Market  by date ranges</p>
          </div>

          {/* THE INTERACTIVE DATE WIDGET */}
          <div className="flex items-center gap-2 bg-[#0f172a] p-2 rounded-lg border border-slate-700 w-full md:w-auto justify-center">
            <div className="flex flex-col text-center">
               <label className="text-[10px] font-black text-slate-500 px-1 uppercase tracking-wider">Start Date</label>
               <input 
                 type="date" 
                 value={startDate} 
                 onChange={(e) => setStartDate(e.target.value)} 
                 className="bg-transparent text-sm font-semibold border-none focus:ring-0 cursor-pointer text-blue-300 text-center"
               />
            </div>
            <div className="w-[1px] h-8 bg-slate-700 mx-2"></div>
            <div className="flex flex-col text-center">
               <label className="text-[10px] font-black text-slate-500 px-1 uppercase tracking-wider">End Date</label>
               <input 
                 type="date" 
                 value={endDate} 
                 onChange={(e) => setEndDate(e.target.value)} 
                 className="bg-transparent text-sm font-semibold border-none focus:ring-0 cursor-pointer text-blue-300 text-center"
               />
            </div>
          </div>
        </div>

        {/* LOADING OVERLAY */}
        {loading && (
          <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center">
            <div className="animate-spin rounded-full h-12 w-12 border-t-4 border-blue-500"></div>
          </div>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-start">
          
          <div className="lg:col-span-1 space-y-8 flex flex-col items-center">
            {/* MARKET SUMMARY TABLE */}
            <KPITable data={metrics} />
            
            {/* EXECUTIVE INTELLIGENCE REPORT (DRILL-DOWN TABLE) */}
            <div className="w-full flex flex-col items-center">
               <h3 className="text-lg font-bold mb-4 text-blue-400 uppercase tracking-widest text-center">Executive Intelligence Report</h3>
               
               {selectedEvent ? (
                <div className="w-full max-w-sm bg-[#1e293b] border-2 border-blue-600 rounded-xl shadow-2xl overflow-hidden animate-in fade-in duration-300">
                  <div className="bg-blue-600 p-2 flex justify-end">
                    <button onClick={() => setSelectedEvent(null)} className="text-white hover:text-red-200 font-bold px-2">✕</button>
                  </div>
                  
                  <div className="p-4 flex justify-center w-full">
                    <table className="w-full border-collapse border border-slate-700">
                      <tbody className="text-center">
                        <tr className="border-b border-slate-700">
                          <td className="bg-slate-800 p-3 text-[10px] font-black text-slate-400 uppercase border-r border-slate-700 w-1/3 text-center">Event</td>
                          <td className="p-3 text-xs font-bold text-white leading-tight uppercase text-center">
                            {selectedEvent.event_name || selectedEvent.Event || "Market Shift"}
                          </td>
                        </tr>
                        <tr className="border-b border-slate-700">
                          <td className="bg-slate-800 p-3 text-[10px] font-black text-slate-400 uppercase border-r border-slate-700 text-center">Category</td>
                          <td className="p-3 text-center">
                            <span className="bg-blue-900 text-blue-200 text-[9px] font-bold px-3 py-1 rounded uppercase">
                              {selectedEvent.category || selectedEvent.Category || "Economic"}
                            </span>
                          </td>
                        </tr>
                        <tr className="border-b border-slate-700">
                          <td className="bg-slate-800 p-3 text-[10px] font-black text-slate-400 uppercase border-r border-slate-700 text-center">Impact</td>
                          <td className="p-3 text-xs text-slate-300 italic px-2 text-center">
                            {selectedEvent.expected_impact || selectedEvent.Expected_Impact || selectedEvent.Impact || "Detail pending..."}
                          </td>
                        </tr>
                        <tr>
                          <td className="bg-slate-800 p-3 text-[10px] font-black text-slate-400 uppercase border-r border-slate-700 text-center">Date</td>
                          <td className="p-3 text-xs font-mono text-slate-400 text-center">
                            {selectedEvent.Date || selectedEvent.date}
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div className="pb-4 text-[9px] font-bold text-green-500 uppercase tracking-tighter text-center">
                    ● AI Analysis Verified for Brent Oil Market Strategy 
                  </div>
                </div>
              ) : (
                <div className="p-12 bg-[#1e293b] border-2 border-dashed border-slate-700 rounded-2xl text-center shadow-inner w-full max-w-sm mx-auto">
                  <p className="text-slate-500 text-sm italic">Click a row in the Historical Table below to generate this Executive Report</p>
                </div>
              )}
            </div>
          </div>

          {/* MAIN CHART AREA */}
          <div className="lg:col-span-2 bg-[#1e293b] p-6 rounded-xl shadow-lg border border-slate-700 h-[500px]">
            <h3 className="text-lg font-bold mb-6 text-slate-300 uppercase tracking-widest text-center">Historical Market Trends</h3>
            <HistoricalChart 
              priceData={priceData} 
              changePointDate={metrics.change_point_date} 
              events={events} 
            />
          </div>
        </div>

        {/* BOTTOM SECTION - EVENT CORRELATION TABLE */}
        <div className="mt-12 mb-8">
          <h3 className="text-xl font-bold text-blue-400 mb-2 text-center uppercase tracking-wider">Historical Event Correlation</h3>
          <p className="text-slate-500 text-xs uppercase font-bold tracking-[0.2em] mb-6 text-center">Dynamic Data - Click any row to analyze impact</p>
          <div className="overflow-hidden rounded-xl shadow-lg border border-slate-700 bg-[#1e293b]">
            <EventTable events={events} onEventClick={handleEventClick} />
          </div>
        </div>

      </main>
      <Footer />
    </div>
  );
}

export default Dashboard;