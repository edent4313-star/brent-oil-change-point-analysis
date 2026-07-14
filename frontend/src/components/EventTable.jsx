import React from "react";

const EventTable = ({ events = [], onEventClick }) => {
  if (!events || events.length === 0) {
    return <div style={{ padding: '10px', textAlign: 'center', fontSize: '14px', color: '#666' }}>No events found.</div>;
  }

  return (
    <div style={{ 
      marginTop: '15px', 
      backgroundColor: 'white', 
      borderRadius: '6px', 
      overflow: 'hidden', 
      border: '1px solid #ddd',
      boxShadow: '0 2px 4px rgba(0,0,0,0.05)'
    }}>
      <div style={{ backgroundColor: '#1e3a8a', color: 'white', padding: '6px 12px', fontWeight: 'bold', fontSize: '13px' }}>
        Market Event Correlation Analysis (Click for Strategic Action)
      </div>
      
      <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', tableLayout: 'fixed' }}>
        <thead>
          <tr style={{ backgroundColor: '#f8fafc', borderBottom: '1px solid #ddd' }}>
            <th style={{ padding: '4px 8px', border: '1px solid #eee', fontSize: '11px', width: '90px', color: '#475569' }}>DATE</th>
            <th style={{ padding: '4px 8px', border: '1px solid #eee', fontSize: '11px', width: '250px', color: '#475569' }}>EVENT NAME</th>
            <th style={{ padding: '4px 8px', border: '1px solid #eee', fontSize: '11px', color: '#475569' }}>DESCRIPTION</th>
          </tr>
        </thead>
        <tbody style={{ fontSize: '12px' }}>
          {events.map((item, index) => {
            return (
              <tr 
                key={index} 
                onClick={() => onEventClick && onEventClick(item)} 
                style={{ 
                  borderBottom: '1px solid #f1f5f9',
                  cursor: 'pointer',
                  transition: 'background-color 0.15s'
                }}
                onMouseOver={(e) => e.currentTarget.style.backgroundColor = '#f0f7ff'}
                onMouseOut={(e) => e.currentTarget.style.backgroundColor = 'transparent'}
              >
                {/* 1. Date column */}
                <td style={{ padding: '4px 8px', border: '1px solid #eee', whiteSpace: 'nowrap', color: '#64748b' }}>
                  {item.Date || item.date || "N/A"}
                </td>
                
                {/* 2. Event Name column (Supports spaces in Excel headers) */}
                <td style={{ padding: '4px 8px', border: '1px solid #eee', fontWeight: '600', color: '#1e293b' }}>
                  {item["Event Name"] || item.Event_Name || item.event ||  "N/A"}
                </td>
                
                {/* 3. Description column (Supports spaces in Excel headers) */}
                <td style={{ padding: '4px 8px', border: '1px solid #eee', color: '#334155', lineHeight: '1.3' }}>
                  {item.Description || item.description || item.Impact || item.impact || "N/A"}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default EventTable;