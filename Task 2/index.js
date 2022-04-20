const express = require("express")
const cors = require("cors")

const app = express()
const apiRoot = '/api'
app.use(cors({origin:'*'}));
function makeDate(){
    var getServerTime= new Date().getTime();
    var serverDate = new Date(getServerTime)
    serverDate = serverDate.toUTCString() //wasn't returning proper string initially due to wrong string method. Was
    //returning GMT-400 instead of GMT due to improper use of toString instead of toUTCString.
    return serverDate;
}




app.get("/",(req,res)=>{
    res.send("Hello World")
})

app.get("/api/current-server-time",(req,res)=>{
    res.send(makeDate())
})

app.listen(8080)