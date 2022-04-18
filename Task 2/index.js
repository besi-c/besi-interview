const express = require("express")
const cors = require("cors")

const app = express()
const apiRoot = '/api'
app.use(cors({origin:'*'}));
var getServerTime= new Date().getTime();
var serverDate = new Date(getServerTime)
serverDate = serverDate.toString()

app.get("/",(req,res)=>{
    res.send("Hello World")
})

app.get("/current-server-time",(req,res)=>{
    res.send(serverDate)
})

app.listen(8080)