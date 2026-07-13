import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
    ResponsiveContainer
} from "recharts";

import {
    useEffect,
    useState
} from "react";

import api from "../services/api";


function HistoricalChart(){

    const [data,setData] = useState([]);


    useEffect(()=>{


        api.get("/historical")

        .then((res)=>{

            setData(res.data);

        })

        .catch((error)=>{

            console.log(
                "Historical data error:",
                error
            );

        });


    },[]);



    return(

        <div className="card">

        <h3>
            Brent Oil Historical Price
        </h3>


        <ResponsiveContainer
            width="100%"
            height={500}
        >

        <LineChart data={data}>


            <CartesianGrid 
                strokeDasharray="3 3"
            />


            <XAxis 
                dataKey="Date"
            />


            <YAxis />


            <Tooltip />


            <Line

                type="monotone"

                dataKey="Price"

                strokeWidth={2}

                dot={false}

            />


        </LineChart>


        </ResponsiveContainer>


        </div>

    )

}


export default HistoricalChart;